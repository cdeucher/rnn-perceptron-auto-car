from numpy import exp, array, random, dot
import numpy as np
import tools as T
import utils as U
Util   = U.oUtil()
Tool   = T.oTool()

class oGenome():
    #def __init__(self):

    def get_better(self, better, player_list):
        if better == None:
            better = player_list[0]            
            better.position  = better.position if len(Tool.read('better.position.txt')) <= 1 else Tool.read('better.position.txt')
            better.weights1  = better.weights1 if len(Tool.read('better.weights1.txt')) <= 1 else Tool.read('better.weights1.txt')
            better.weights2  = better.weights2 if len(Tool.read('better.weights2.txt')) <= 1 else Tool.read('better.weights2.txt')
            better.reward    = 0 if len(Tool.read('better.reward.txt')) <= 1 else Tool.read('better.reward.txt')[0]

        #get better 
        for i in range( len(player_list) ):
            if( (better.position[1] * better.reward) < (player_list[i].position[1] * player_list[i].reward) ):
                print('better',better.position[1], player_list[i].position[1], player_list[i].reward )
                better = player_list[i]
                Tool.save('better.position.txt', better.position)
                Tool.save('better.reward.txt',   [better.reward, 0])
                Tool.save('better.weights1.txt', better.weights1)
                Tool.save('better.weights2.txt', better.weights2)

        return better        
                
    def mutate(self, player, better):
        count = 0
        weights1 = random.random((len(player.weights1), len(player.weights1[0]) ))
        weights2 = random.random((len(player.weights2), len(player.weights2[0]) ))

        for i in range( len(player.weights1) ): 
            for x in range( len(player.weights1[i]) ):
                if random.uniform(0, 1) < 0.9 or better == None:
                    if random.uniform(0, 1) > 0.3 and  better != None: #considerar o better no sorteio
                        weights1[i][x] = random.uniform(0, 1) if better.weights1[i][x] > 0.1 else random.uniform(0, 1) -1
                    else:    
                        weights1[i][x] = random.uniform(0, 1) if random.uniform(0, 1) < 0.5 else random.uniform(0, 1) -1
                    count += 1                            
                else:
                        weights1[i][x] = better.weights1[i][x]    

        for i in range( len(player.weights2) ): 
            for x in range( len(player.weights2[i]) ):
                if random.uniform(0, 1) < 0.9  or better == None:
                    if random.uniform(0, 1) > 0.3  and  better != None: #considerar o better no sorteio
                        weights2[i][x] = random.uniform(0, 1) if better.weights2[i][x] > 0.1 else random.uniform(0, 1) -1                    
                    else:    
                        weights2[i][x] = random.uniform(0, 1) if random.uniform(0, 1) < 0.5 else random.uniform(0, 1) -1                    
                    count += 1
                else:                    
                        weights2[i][x] = better.weights2[i][x] 

        print('mutations', count)
        return  weights1, weights2

    def genome(self, player, better):        
        if random.uniform(0, 1) < 0.9 :
            #print('genome',player.index)
            weights1, weights2 = self.mutate( player, better ) 
            return weights1, weights2, True
        else:
            if(better == None):
                return 0, 0, False
            else:    
                return Util.copy(better.weights1), Util.copy(better.weights2), True

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

                                    