from numpy import exp, array, random, dot
import numpy as np
from PIL import Image as img

# GRIDE

ROW_COUNT = 31
COLUMN_COUNT = 30
WIDTH = 30
HEIGHT = 30

#ROBOTs
MOVEMENT_SPEED = 10

class oUtil():
    def __init__(self):
     
        #GRIDE
        #http://arcade.academy/examples/array_backed_grid.html#array-backed-grid
        #self.grid = np.zeros([ROW_COUNT, COLUMN_COUNT])
        #print(self.grid)
        self.grid =  [  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],                        
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]     

        self.reward =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 5, 5, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 5, 5, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 5, 5, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 5, 5, 5],
                        [10,10,10,10,10,10,10,10,10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 3, 3, 6, 6, 5, 5, 5],
                        [11,11,11,11,10,10,10,10,10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5],
                        [11,11,11,11,10,10,10,10,10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5],
                        [11,11,11,11,11,11,11,11,11, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5],                        [1, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [11,11,11,11,11,11,11,11,11, 9, 9, 9, 9, 9, 9, 9, 9, 7, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5],
                        [11,12,12,12,11,11,11,11,11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                        [11,12,12,12,12,12,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15],
                        [11,12,12,12,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15],
                        [11,12,12,12,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15],
                        [11,12,12,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15],
                        [11,12,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,16,16,16,15,15],
                        [11,12,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,16,16,16,15,15],
                        [17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,16,16,16,16],
                        [18,18,18,18,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,16,16,16,16],
                        [18,18,18,18,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,16,16,16],
                        [18,18,18,18,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,16,16],
                        [18,18,18,18,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,16,16],
                        [18,19,19,18,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,16,16],
                        [19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,22,22,22,22,22,22,22,22],
                        [19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,22,22,22,22,21,21,21,21],
                        [19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,22,22,22,22,22,22,22,22],
                        [19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,22,22,22,22,22,22,22,22],
                        [19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,22,22,22,22,22,22,22,22],
                        [19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,22,22,22,22,22,22,22,22],
                        [19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,22,22,22,22,22,22,22,22]] 
        #self.image2pixelarray('images/map.png')                  

    def image2pixelarray(self,filepath):
        """
        Parameters
        ----------
        filepath : str
            Path to an image file

        Returns
        -------
        list
            A list of lists which make it simple to access the greyscale value by
            im[y][x]
        """
        im = img.open(filepath).convert('L')
        (width, height) = im.size
        greyscale_map = list(im.getdata())
        greyscale_map = np.array(greyscale_map)
        greyscale_map = greyscale_map.reshape((height, width))
        print(greyscale_map)
        return greyscale_map   

    def action_reliase(self, player, action):
        player.change_angle = 0 
        if action == 0:            
            player.change_angle = MOVEMENT_SPEED    
            if player.angle > 90 :
                    player.angle = -280             
        elif action == 1: 
            player.change_angle = -MOVEMENT_SPEED   
            if player.angle * -1 >= 280 :
                    player.angle = 90                            
        elif action == 2:
            player.speed  = MOVEMENT_SPEED                   
        elif action == 3:
            player.speed  = -MOVEMENT_SPEED    

    def calc_angle(self, player):
        top     = int(np.around( ( (player.position[1]+15) )/COLUMN_COUNT ))  # 25 top
        botton  = int(np.around( ( (player.position[1]-40) )/COLUMN_COUNT ))  # 30 botton
        right   = int(np.around( ( (player.position[0]+5) )/ROW_COUNT ))     # 20 right
        left    = int(np.around( ( (player.position[0]-25) )/ROW_COUNT ))     # 25 left
        #return top,botton,right,left

        top    = top if top < 29 else 29
        right  = right if right < 29 else 29
        botton = botton if botton >= 0 else 0
        left   = left if left >= 0 else 0  

        player.topx    = top
        player.rightx  = right
        player.bottonx = botton
        player.leftx   = left   

        ##girar o sensor
        angle = player.angle# * -1 if player.angle < 0 else player.angle   

        if angle < 0 and angle > -181 :
            player.location_side = 1
            player.location_angle = 1

            if (angle <= 0 and angle > -81): #top -75
                player.location_angle = 0
            elif (angle < -100 and angle > -180): #botton  
                player.location_angle = 2

        else :    
            player.location_side = 2
            player.location_angle = 1
            if (angle > 0 ): #top
                target_angle = 40 if player.line_botton > 150 else 85
                if (angle < target_angle): #top 55
                    player.location_angle = 0
            if (angle < -180 and angle > -255): #botton 
                player.location_angle = 2

       
        if player.location_side == 1 :
            line_top    = self.check_wall_top( self.grid, top, left )
            line_botton = self.check_wall_botton( self.grid, botton, left )
            line_left   = self.check_wall_left( self.grid, left, botton )
            line_right  = self.check_wall_right( self.grid, right, botton )     

            if player.location_angle == 0: #top
                line_top    = self.check_wall_left( self.grid, left, botton )
                line_botton = self.check_wall_right( self.grid, right, botton )
                line_left   = self.check_wall_botton( self.grid, botton, left )
                line_right  = self.check_wall_top( self.grid, top, left )
            elif player.location_angle == 2 : #botton  
                line_top    = self.check_wall_right( self.grid, right, botton )
                line_botton = self.check_wall_left( self.grid, left, botton )
                line_left   = self.check_wall_top( self.grid, top, left )
                line_right  = self.check_wall_botton( self.grid, botton, left )
        else:
            line_top    = self.check_wall_botton( self.grid, botton, left )          
            line_botton = self.check_wall_top( self.grid, top, left )
            line_left   = self.check_wall_right( self.grid, right, botton )
            line_right  = self.check_wall_left( self.grid, left, botton )

            if player.location_angle == 0 : #top
                line_top    = self.check_wall_left( self.grid, left, botton )
                line_botton = self.check_wall_right( self.grid, right, botton )
                line_left   = self.check_wall_botton( self.grid, botton, left )
                line_right  = self.check_wall_top( self.grid, top, left )
            elif player.location_angle == 2: #botton  
                line_top    = self.check_wall_right( self.grid, right, botton )
                line_botton = self.check_wall_left( self.grid, left, botton )
                line_left   = self.check_wall_top( self.grid, top, left )
                line_right  = self.check_wall_botton( self.grid, right, left )            

        player.line_top     = line_top
        player.line_botton  = line_botton
        player.line_left    = line_left
        player.line_right   = line_right 

        return line_top, line_botton, line_left, line_right        

    def check_wall_top(self, grid, top, left):
        WALL  = True
        count = 0
        index = top 
        while WALL:            
            if grid[index][left] == 1:
                WALL = False
            else :
                count += 1
                index += 1
        return  count * HEIGHT    

    def check_wall_botton(self, grid, botton, left):
        WALL  = True
        count = 0
        index = botton 
        while WALL:            
            if grid[index][left] == 1:
                WALL = False
            else :
                count += 1
                index -= 1
        return  count * HEIGHT

    def check_wall_left(self, grid, left, top):
        WALL  = True
        count = 0
        index = left 
        while WALL:            
            if grid[top][index] == 1:
                WALL = False
            else :
                count += 1
                index -= 1
        return  count * WIDTH  

    def check_wall_right(self, grid, right, top):
        WALL  = True
        count = 0
        index = right 
        while WALL:            
            if grid[top][index] == 1:
                WALL = False
            else :
                count += 1
                index += 1
        return  count * WIDTH 

    def copy(self, arr) :
        tmp = random.random((len(arr), len(arr[0]) ))
        for i in range(len(arr)) :    
            for x in range(len(arr[i])) :
                tmp[i][x] = arr[i][x]

        return tmp        
               
             
