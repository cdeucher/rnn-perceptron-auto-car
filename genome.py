from numpy import exp, array, random, dot
import random as rand
import numpy as np
import copy

import tools as T
import utils as U

Util   = U.oUtil()
Tool   = T.oTool()

MAX = 200

class copybetter:
    weights1 = []
    weights1 = []
    position = [0,0]
    reward = 0
    
class oGenome():
    def __init__(self):
        self.genome_list = []

    def get_better(self, better, player_list):      
        if better == None:
            better = player_list[0]                        
            better.position  = better.position if len(Tool.read('better.position.txt')) <= 1 else Tool.read('better.position.txt')
            better.weights1  = better.weights1 if len(Tool.read('better.weights1.txt')) <= 1 else Tool.read('better.weights1.txt')
            better.weights2  = better.weights2 if len(Tool.read('better.weights2.txt')) <= 1 else Tool.read('better.weights2.txt')
            better.reward    = 0 if len(Tool.read('better.reward.txt')) <= 1 else Tool.read('better.reward.txt')[0]
        #get better 
        for i in range( len(player_list) ):        
            if( better.reward < player_list[i].reward ):
                print('better',better.position[1], player_list[i].position[1], player_list[i].reward )
                better = player_list[i]
                Tool.save('better.position.txt', better.position)
                Tool.save('better.reward.txt',   [better.reward, 0])
                Tool.save('better.weights1.txt', better.weights1)
                Tool.save('better.weights2.txt', better.weights2)

        tmp = copybetter()
        tmp.weights1 = better.weights1
        tmp.weights2 = better.weights2 
        tmp.position = better.position       
        tmp.reward   = better.reward

        return copy.deepcopy(tmp)        
                
    def mutate(self, player, better):
        weights1 = Util.copy(player.weights1)
        weights2 = Util.copy(player.weights2)
        count = 0 
        for i in range( len(player.weights1) ): 
            for x in range( len(player.weights1[i]) ):
                if random.uniform(0, 1) < 0.2 or better == None:
                    if random.uniform(0, 1) < 0.5 and  better != None: #considerar o better no sorteio
                        weights1[i][x] = better.weights1[i][x] 
                        #return  weights1, weights2, True 
                        count += 1 
                    else:    
                        weights1[i][x] = random.uniform(0, 1) if random.uniform(0, 1) < 0.5 else random.uniform(0, 1) -1
                        #return  weights1, weights2, True                            
                        count += 1

        for i in range( len(player.weights2) ): 
            for x in range( len(player.weights2[i]) ):
                if random.uniform(0, 1) < 0.2  or better == None:
                    if random.uniform(0, 1) < 0.5  and  better != None: #considerar o better no sorteio
                        weights2[i][x] = better.weights2[i][x] 
                        #return  weights1, weights2, True
                        count += 1
                    else:    
                        weights2[i][x] = random.uniform(0, 1) if random.uniform(0, 1) < 0.5 else random.uniform(0, 1) -1                    
                        #return  weights1, weights2, True
                        count += 1

        return  weights1, weights2, count

    def genome(self, player, better, RANGE):        
        if random.uniform(0, 1) < RANGE :
            #print('genome',player.index)
            weights1, weights2, mutate = self.mutate( player, better ) 
            return weights1, weights2, True, mutate
        else:  
            return Util.copy(player.weights1), Util.copy(player.weights2), 0, False

    def crossover(self, player_list):
        count = 0
        self.genome_list = []
        #start sort        
        arr   = sorted(player_list, key=lambda x: x.reward, reverse=True)
        for i in range(len(arr)) :
            if arr[i].reward > 0 and len(self.genome_list) < MAX:
                tmp = copybetter()
                tmp.weights1 = arr[i].weights1
                tmp.weights2 = arr[i].weights2
                tmp.reward   = arr[i].reward
                self.genome_list.append( copy.deepcopy( tmp ) )

                count += 1
                if count <= 20 :
                   print("Sorted : ", count, arr[i].reward)
                else :
                   break
        print('genome_list count:',len(self.genome_list))           

        #start crossover
        for x in range(len(self.genome_list)) :
            for i in range( (len(self.genome_list[x].weights1) -1) ): 
                rang = rand.randrange(1, (len( self.genome_list[x].weights1[i] ) -1))

                #print(i,len( self.genome_list[x].weights1[i] ), rang, self.genome_list[x].weights1[i] ) 

                j = 0 
                tmp = []
                while j <= rang:
                    tmp.append(self.genome_list[x].weights1[i][j])
                    j += 1
                    #print('did',j)
                
                j = rang+1
                #print(i, 'start did',j)
                while j < (len( self.genome_list[x].weights1[i]) ) : #crossover com o proximo da fila (x+1)
                    #print(x, 'j',j, len( self.genome_list[x].weights1[i]) )
                    try :
                        tmp.append(self.genome_list[ (x+1) ].weights1[i][j])
                    except IndexError :
                        tmp.append(self.genome_list[x].weights1[i][j])

                    j += 1                       

                #print(i,rang, tmp ) 
                self.genome_list[x].weights1[i] = tmp  # aplica crossover
            ## end weights1
            for i in range( len(self.genome_list[x].weights2) ): 
                rang = rand.randrange(1, (len( self.genome_list[x].weights2[i] ) -1))
                j = 0 
                tmp = []
                while j <= rang:
                    tmp.append(self.genome_list[x].weights2[i][j])
                    j += 1
                
                j = rang+1 
                while j < (len( self.genome_list[x].weights2[i]) ) : #crossover com o proximo da fila (x+1)
                    try :
                        tmp.append(self.genome_list[ (x+1) ].weights2[i][j])
                    except IndexError :
                        tmp.append(self.genome_list[x].weights2[i][j])

                    j += 1                       
                self.genome_list[x].weights2[i] = tmp  # aplica crossover  

            ## end weights2    

            #end if
        ## end for              

        return self.genome_list
        ## end crossover



    def neuron(self, arcade, hidden, action, lines):
        actions = ['top','botton','left','right']
        for i in range(6) :
            if i == hidden :
                arcade.draw_text(f"(x)", 250, 500+(i*15),arcade.csscolor.WHITE, 12) 
            else:
                arcade.draw_text(f"( )", 250, 500+(i*15),arcade.csscolor.WHITE, 12)     

        for i in range(4) :
            if i == action :
                arcade.draw_text(f"(x) {actions[i]}", 280, 500+(i*15),arcade.csscolor.WHITE, 12) 
            else:
                arcade.draw_text(f"( ) {actions[i]}", 280, 500+(i*15),arcade.csscolor.WHITE, 12)  

            arcade.draw_text(f"{actions[i]}:{lines[i]}", 150, 500+(i*15),arcade.csscolor.WHITE, 10) 

                                    