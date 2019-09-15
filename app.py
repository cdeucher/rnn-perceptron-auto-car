import arcade
import os
import math
from numpy import exp, array, random, dot
import numpy as np
import copy

import network as rnn
import utils as U
import tools as T
import genome as GE
Util   = U.oUtil()
Genome = GE.oGenome()
Tool   = T.oTool()

DEBUG = True
SPRITE_SCALING = 0.5
GRAVITY = 0
SCREEN_TITLE = "RNN + Genetic algorithm"

# GRIDE
ROW_COUNT = 30
COLUMN_COUNT = 30
WIDTH = 30
HEIGHT = 30
MARGIN = 0
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

#ROBOTs
MOVEMENT_SPEED = 5
MAX = 200 if not DEBUG else 1

class copybetter:
    weights1 = []
    weights1 = []
    position = [0,0]
    reward = 0

class Player(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)

        self.speed    = 0
        self.thrust   = 0
        self.reward   = 0
        self.index    = random.uniform(0, 1)
        self.center_x = 150 + random.uniform(1,10)
        self.center_y = 100 + random.uniform(1,10)  
        self.stop     = 0   
        self.angle    = -90  


    def update(self):
        if(self.stop == 0):
            self.angle_rad = math.radians(self.angle)
            self.angle += self.change_angle
            self.center_x += -self.speed * math.sin(self.angle_rad)
            self.center_y += self.speed * math.cos(self.angle_rad)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """        
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.MAX_TIME = 5
        # Sprite lists
        self.wall_list = None
        self.player_list = None
        self.player_tmp  = []
        self.score = 0
        self.score_timeout = 0
        self.generations = 0
        self.frame = 0

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        # Create layer 1/2 (6 inputs, each with 6 neurons)
        self.layer1 = rnn.NeuronLayer(5, 6)
        self.layer2 = rnn.NeuronLayer(6, 4)
        self.perceptron = rnn.NeuralNetwork(self.layer1, self.layer2)
        self.genoma_list = []

        self.better           = copybetter()       
                                # 6 imputs, 6 neuro, 4 saidas               
        self.better.weights1  = 2 * random.random((5, 6)) - 1 if len(Tool.read('better.weights1.txt')) <= 1 else Tool.read('better.weights1.txt')
        self.better.weights2  = 2 * random.random((6, 4)) - 1 if len(Tool.read('better.weights2.txt')) <= 1 else Tool.read('better.weights2.txt')
        self.better.reward    = 0 if len(Tool.read('better.reward.txt')) <= 1 else Tool.read('better.reward.txt')[0]

        #neuron
        self.better_count = 0
        self.neuron_action = [0, 0]
        self.index = 0
        self.lines_action = [0, 0, 0, 0]

        self.grid   = Util.grid 
        self.reward = Util.reward          

    def newgame(self):
        print('------------------start----------------') 
        self.generations += 1
        count = 0
        while len(self.player_list) < MAX:         
            car_number = int(random.uniform(0,3))    
            self.player_sprite = Player("images/car"+str(car_number)+".png",SPRITE_SCALING)
            self.player_sprite.weights1 = Util.copy(self.better.weights1)
            self.player_sprite.weights2 = Util.copy(self.better.weights2) 
            if count > 1 :
                mutation1, mutation2, mutate, mutcount = Genome.genome(self.player_sprite, self.better, 0.9)
                if( mutate ):
                    old = self.player_sprite.weights1
                    self.player_sprite.weights1 = mutation1
                    self.player_sprite.weights2 = mutation2

            self.player_sprite.physics  = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)                          
            self.player_list.append(self.player_sprite) 
            count += 1              
        #end while    
        print( 'new players',  len(self.player_list) )

    def startnewgame(self):
        print('------------------startnewgame----------------') 
        self.generations += 1
        mutations = 0
        #for x in range( MAX ):
        print( 'new players tmp/list',  len(self.player_tmp) ,len(self.player_list) )
        count = 0
        while len(self.player_list) < MAX:         
            car_number = int(random.uniform(0,3))     
            self.player_sprite = Player("images/car"+str(car_number)+".png",SPRITE_SCALING)
            if count < (len(self.player_tmp) -1) :
                self.player_sprite.weights1 = self.player_tmp[count].weights1
                self.player_sprite.weights2 = self.player_tmp[count].weights2
                mutation1, mutation2, mutate, mutcount = Genome.genome(self.player_sprite, self.better, 0.3)
                if( mutate ):
                    old = self.player_sprite.weights1
                    self.player_sprite.weights1 = mutation1
                    self.player_sprite.weights2 = mutation2 
                    mutations += mutcount                
            else:                                               
                self.player_sprite.weights1 = Util.copy(self.better.weights1)
                self.player_sprite.weights2 = Util.copy(self.better.weights2) 
                self.player_sprite.weights1 = mutation1
                self.player_sprite.weights2 = mutation2    
                mutations += mutcount                                 
                 
            self.player_sprite.physics  = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)                          

            self.player_list.append(self.player_sprite) 
            count += 1              
        #end while    
        print( 'new players',  len(self.player_list) )
        print('mutations',mutations)    

    def setup(self):

        self.score = 0
        self.score_timeout = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()                   

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                # Draw the box
                if self.grid[row][column] == 1:
                    wall = arcade.Sprite("images/platform2.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)                        

        # Set up the player
        self.newgame()
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
            arcade.start_render()

            # Draw all the sprites.
            self.wall_list.draw()
            self.player_list.draw()

            # score
            arcade.draw_text(f"Max Time: {self.MAX_TIME}",50, 610,arcade.csscolor.WHITE, 10)
            arcade.draw_text(f"Time: {self.score}", 50, 630,arcade.csscolor.WHITE, 10)
            arcade.draw_text(f"Generations: {self.generations}", 50, 620,arcade.csscolor.WHITE, 10)        
    
            Genome.neuron(arcade, self.neuron_action[0], self.neuron_action[1], self.lines_action) 

            if DEBUG :
                arcade.draw_text(f"right: {self.player_list[0].rightx} left: {self.player_list[0].leftx}", 50, 450,arcade.csscolor.WHITE, 10) 
                arcade.draw_text(f"top: {self.player_list[0].topx} botton: {self.player_list[0].bottonx}", 50, 440,arcade.csscolor.WHITE, 10)                         
                
                arcade.draw_text(f"line_top:{self.player_list[0].line_top} line_botton:{self.player_list[0].line_botton}", 50, 470,arcade.csscolor.WHITE, 10) 
                arcade.draw_text(f"line_left: {self.player_list[0].line_left} line_right: {self.player_list[0].line_right}", 50, 460,arcade.csscolor.WHITE, 10) 

                front, back = self.draw_debug(self.player_list[0])

                arcade.draw_text(f"front {front}", self.player_list[0].position[0],  self.player_list[0].position[1]+25, arcade.csscolor.WHITE, 10) 
                arcade.draw_text(f"back {back}", self.player_list[0].position[0],    self.player_list[0].position[1]-30, arcade.csscolor.WHITE, 10)


            for player in self.player_list:                
                #arcade.draw_text(f"top",    player.position[0],    player.position[1]+25, arcade.csscolor.WHITE, 10) 
                #arcade.draw_text(f"botton", player.position[0],    player.position[1]-30, arcade.csscolor.WHITE, 10)
                #arcade.draw_text(f"right",  player.position[0]+20, player.position[1], arcade.csscolor.WHITE, 10) 
                #arcade.draw_text(f"left",   player.position[0]-25, player.position[1], arcade.csscolor.WHITE, 10)                
                #{str(player.reward)[:4]} 
                arcade.draw_text(f"R: {str(player.angle)}  {str(player.location_side)} {player.location_angle}", player.position[0],    player.position[1]+40 ,arcade.csscolor.WHITE, 10) 

                if(player.index == self.index) :
                    self.draw_debug(player)

    def draw_debug(self, player):
        xx = player.position[0]
        yy = player.position[1]                  

        try :
            if player.location_side == 1 :
                if player.location_angle == 0 :
                    front = yy+player.line_right 
                    back  = xx+player.line_botton                        
                    arcade.draw_line(xx, yy, xx, front, arcade.color.WOOD_BROWN, 3) 
                    #arcade.draw_line(xx, yy, xx, -back, arcade.color.WOOD_BROWN, 3)

                elif player.location_angle == 1 :
                    front = xx+player.line_right 
                    back  = xx+player.line_botton                        
                    arcade.draw_line(xx, yy, front, yy, arcade.color.WOOD_BROWN, 3) 
                    #arcade.draw_line(xx, yy, -back, yy, arcade.color.WOOD_BROWN, 3)

                elif player.location_angle == 2 :
                    front = yy-player.line_right 
                    back  = yy+player.line_botton                      
                    arcade.draw_line(xx, yy, xx, front, arcade.color.WOOD_BROWN, 3) 
                    #arcade.draw_line(xx, yy, xx, back, arcade.color.WOOD_BROWN, 3)

            elif player.location_side == 2 :   
                if player.location_angle == 0 :
                    front = yy+player.line_right 
                    back  = xx+player.line_botton                        
                    arcade.draw_line(xx, yy, xx, front, arcade.color.WOOD_BROWN, 3) 

                elif player.location_angle == 1 :
                    front = xx+player.line_right 
                    back  = xx+player.line_botton                                        
                    arcade.draw_line(xx, yy, -front, yy, arcade.color.WOOD_BROWN, 3) 

                elif player.location_angle == 2 :
                    front = yy-player.line_right 
                    back  = yy+player.line_botton                      
                    arcade.draw_line(xx, yy, xx, front, arcade.color.WOOD_BROWN, 3)              


        except ZeroDivisionError:
            arcade.draw_line(xx, yy, 0, yy, arcade.color.WOOD_BROWN, 3)  

        return  front, back   

           
    def kill(self, player):
        player.change_angle = 0
        player.speed    = 0
        player.thrust   = 0
        player.stop     = 1  
                   

    def update(self, delta_time):
        self.score_timeout += delta_time
        self.frame += delta_time
        self.score = int(self.score_timeout) % 60
        
        self.player_list.update()
        for player in self.player_list :  
            #fix angle 
            if player.angle > 90 :
               player.angle = -280
            if player.angle * -1 > 280 : 
               player.angle = 91                


            collision = arcade.check_for_collision_with_list(player, self.wall_list)
            if len(collision) > 0 and not DEBUG:
                self.kill(player)            

            line_top, line_botton, line_left, line_right = Util.calc_angle(player)

            #fitness func
            player.reward = self.reward[player.bottonx][player.rightx] * player.position[1]
            

            hidden_state, output = self.perceptron.run([ player.speed, line_top, line_botton, line_left, line_right  ], player.weights1, player.weights2)                         
            A = np.array(output)
            H = np.array(hidden_state)
            hidden = np.where(H==max(hidden_state))[0][0]
            action = np.where(A==max(output))[0][0] 

            if  player.reward >= self.better_count :
                self.index         = player.index
                self.better_count  = player.reward

            if(player.index == self.index) :                                          
                self.neuron_action = [hidden, action]
                self.lines_action  = [line_top, line_botton, line_left, line_right]

            if not DEBUG and player.stop == 0:                 
                Util.action_reliase(player,action)           

        if(self.score > self.MAX_TIME  and not DEBUG) :
            self.score_timeout = 0
            print('---------   MAX_TIME OVER --------')
            print('start genoma - player_list:', len(self.player_list))
            self.better = Genome.get_better(self.better, self.player_list )   
            #apply crossover
            self.genoma_list = []
            self.genoma_list.append( self.better )
            GEN = True
            while GEN :
                tmp = Genome.crossover( self.player_list )                                 
                self.genoma_list.extend( tmp ) 
                if len(tmp) > 0 and len(self.genoma_list) < MAX and len(self.player_list) > 3 :
                    GEN = True
                else:
                    GEN = False    

            print('end genoma - genoma_list:', len(self.genoma_list))

            count_final = 0
            while len(self.player_list) > 0:                
                for player in self.player_list:  
                    if player.reward >= self.better_count :
                        count_final += 1    
                    player.kill() 

            self.player_tmp = []
            self.player_tmp.append( self.better )
            for player in self.genoma_list:
                self.player_tmp.append( player )

            print( 'new players crossover',  len(self.player_tmp) )    

            print('follow', count_final)
            self.better_count = 0 
            self.startnewgame()                       

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_list[0].speed = MOVEMENT_SPEED
            self.MAX_TIME += 5
        elif key == arcade.key.DOWN:
            self.player_list[0].speed = -MOVEMENT_SPEED
            self.MAX_TIME -= 5

        elif key == arcade.key.LEFT:
            self.player_list[0].change_angle = MOVEMENT_SPEED  
        elif key == arcade.key.RIGHT:            
            self.player_list[0].change_angle = -MOVEMENT_SPEED  

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_list[0].speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_list[0].change_angle = 0          

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()