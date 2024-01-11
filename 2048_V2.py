import pygame
import time
import random


#Font
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 40)
FONT_Game = pygame.font.SysFont("comicsans", 30)

WIDTH, Height, Starting, floor = 1200, 850, 1000, 0    # setting the size for the window rize

Box_Size = (190, 190)
Image_Size = (150, 150)
Game_Border = [(220, 45),(980, 45),(220, 805),(980, 805)]    # Border for 2048 [Top left, Top right, Bottom Left, Bottome Left] , (x-position, y-position)

# Poaition for each tile space
# There is a total of 16 tiles space going from 
Tile_space = [[(220, 45),(410, 45), (600, 45), (790, 45)],
              [(220, 235),(410,235), (600,235), (790, 235)],
              [(220, 425), (410,425), (600, 425), (790, 425)],
              [(220, 615), (410, 615), (600, 615), (790, 615)]]

# Values to move the friends tiles
Speed = 10
Frames = 19
Spaces = 15


Window = pygame.display.set_mode((WIDTH, Height))      #Creates the window display with corresponding hwight and width

pygame.display.set_caption("2048 With Friends")


# Define the images as variables
Background = pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Forest.jpg").convert_alpha()
Grid = pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\grid.png").convert_alpha()
Starting_Screen = pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Friends_2.JPG").convert_alpha()

#Friends
Friend = [pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Chris_1.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Alex_2.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Gandalf_3.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Kevin_4.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Adolf_5.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Moy_6.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Ferny_7.JPG").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Danny_8.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\George_9.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Randy_10.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Hagrid_11.jpg").convert_alpha(),]

#State Key [1: Starting Screen, 2: Game Play, 3: End Screen, 4: Pause Screen]
Game_State = 1



class Friends_Position:
    def __init__(self, Row, Col, Friend_Number):
        self.Row = Row
        self.Col = Col
        self.X = Tile_space[Row][Col][0]
        self.Y = Tile_space[Row][Col][1]
        self.Old_Row = Row
        self.Old_Col = Col
        self.Friend = Friend_Number       #Image of which friend it is





def pause():
    Lost_text = FONT.render("Pause", 1, "red")
    Window.blit(Lost_text,(WIDTH/2 - Lost_text.get_width()/2, Height/2 - Lost_text.get_height()/2))
    clock = pygame.time.Clock()
    pygame.display.update()
    pygame.time.delay(100)

    while True:
        clock.tick(30)  #a clock objects that run/hold the code to run # per second 
        
        for event in pygame.event.get():   # pygame.event.get() gets any key pressed
            if event.type == pygame.QUIT:
                return False
            
        Exit =  pygame.key.get_pressed() # assign keys to store any key pressed
        if Exit[pygame.K_SPACE]:
            return True
        elif Exit[pygame.K_DELETE]:
            return False
        



def Game_Over():

    Lost_text = FONT.render("Game Over", 1, "white")
    Window.blit(Lost_text,(WIDTH/2 - Lost_text.get_width()/2, Height/2 - Lost_text.get_height()/2))
    clock = pygame.time.Clock() 
    pygame.display.update()
    pygame.time.delay(100)

    while True:
        clock.tick(30)  #a clock objects that run/hold the code to run # per second 
        
        for event in pygame.event.get():   # pygame.event.get() gets any key pressed
            if event.type == pygame.QUIT:
                return False
            
        Exit =  pygame.key.get_pressed() # assign keys to store any key pressed
        if Exit[pygame.K_SPACE]:
            return True


def Movement():
    False

def Draw(Characters):
    
    Window.blit(pygame.transform.scale(Background, (WIDTH, Height)), (floor,floor))
    Window.blit(pygame.transform.scale(Grid, (190*4, 190*4)), Tile_space[0][0])

    # Test Screen to check if all frined come out
    #Window.blit(pygame.transform.scale(Friend_1, Box_Size), Tile_space[0])
    #Window.blit(pygame.transform.scale(Friend_2, Box_Size), Tile_space[1])
    #Window.blit(pygame.transform.scale(Friend_3, Box_Size), Tile_space[2])
    #Window.blit(pygame.transform.scale(Friend_4, Box_Size), Tile_space[3])
    #Window.blit(pygame.transform.scale(Friend_5, Box_Size), Tile_space[4])
    #Window.blit(pygame.transform.scale(Friend_6, Box_Size), Tile_space[5])
    #Window.blit(pygame.transform.scale(Friend_7, Box_Size), Tile_space[6])
    #Window.blit(pygame.transform.scale(Friend_8, Box_Size), Tile_space[7])
    #Window.blit(pygame.transform.scale(Friend_9, Box_Size), Tile_space[8])
    #Window.blit(pygame.transform.scale(Friend_10, Box_Size), Tile_space[9])
    #Window.blit(pygame.transform.scale(Friend_11, Box_Size), Tile_space[10])
    #Window.blit(pygame.transform.scale(Friend_1, Box_Size), Tile_space[11])
    #Window.blit(pygame.transform.scale(Friend_2, Box_Size), Tile_space[12])
    #Window.blit(pygame.transform.scale(Friend_3, Box_Size), Tile_space[13])
    #Window.blit(pygame.transform.scale(Friend_4, Box_Size), Tile_space[14])
    #Window.blit(pygame.transform.scale(Friend_5, Box_Size), Tile_space[15])
    #

    # Iterate through the object and prints them to the screen
    for image in Characters:
        Window.blit(pygame.transform.scale(Friend[image.Friend], Box_Size), (image.X, image.Y))
       # Window.blit(pygame.transform.scale(Friend[image.Friend], Box_Size), Tile_space[image.Row][image.Col])   # Tile_Space[Row][Col]

    pygame.display.update()





def Start_Screen():

    Window.blit(pygame.transform.scale(Starting_Screen, (WIDTH, Height)), (0,0))

    Starting_Text = FONT.render("Welcome to the Friend Game", 1, "Red")
    Window.blit(Starting_Text,(WIDTH/2 - Starting_Text.get_width()/2, Starting_Text.get_height()/8))

    Game_Text = FONT_Game.render(" Combine Friends using the Arrow Key", 1, "white")
    Window.blit(Game_Text, (WIDTH/2 - Starting_Text.get_width()/2, Starting_Text.get_height()))

    pygame.display.update()

    while True:

        for event in pygame.event.get():   # pygame.event.get() gets any key pressed
            if event.type == pygame.QUIT:
                return False
            
        Exit =  pygame.key.get_pressed() # assign keys to store any key pressed
        if Exit[pygame.K_SPACE]:
            return True
        elif Exit[pygame.K_DELETE] or Exit[pygame.K_ESCAPE]:
            return False




def Game_Movement(key, Friend):
    if key[pygame.K_LEFT]:
        for me in Friend:
            if (me.Col - 1) >= 0:
                temp_Pos = me.Col
                me.Old_Col= temp_Pos
                me.Col -= 1

                Move_Friend(Friend, me, key)

                # me.X += 1 
                # for later: make an algorithem that moves each item at the highest pos one up 
                # and proceed down the list
                # then the next item checks if there is a box in front of it
                # if they are the same size the block at the edge/wall changes to next friend and erased the other friend
                

    elif key[pygame.K_RIGHT]:
        for me in Friend:
            if (me.Col + 1) <= 3:
                temp_Pos = me.Col
                me.Old_Col = me.Col
                me.Col += 1

                Move_Friend(Friend, me, key)
                
            # while Tile_space[me.Col][me.Row] != (me.X, me.Y):


    elif key[pygame.K_UP]:
        for me in Friend:
            if (me.Row - 1) >= 0:
                temp_Pos = me.Row
                me.Old_Row = me.Row
                me.Row -= 1

                Move_Friend(Friend, me, key)

    elif key[pygame.K_DOWN]:
        for me in Friend:
            if (me.Row + 1) <= 3:
                temp_Pos = me.Row
                me.Old_Row = me.Row
                me.Row += 1

                Move_Friend(Friend, me, key)

    
def Move_Friend(Friend, me, Direction):
    # while Tile_space[Friend.Col][Friend.Row] != (Friend.X, Friend.Y):
    for i in range(10):
        if Direction[pygame.K_LEFT]:     # if the left key was detected it moves the image 19 frames to the left
            me.X -= Frames
            Draw(Friend)


        elif Direction[pygame.K_RIGHT]:    # if the Right key was detected it moves the image 19 frames to the right
            me.X += Frames
            Draw(Friend)
            
        elif Direction[pygame.K_UP]:    # if the Up key was detected it moves the image 19 frames up
                me.Y -= Frames
                Draw(Friend)

        elif Direction[pygame.K_DOWN]:    # if the Down key was detected it moves the image 19 frames down
                me.Y += Frames
                Draw(Friend)

def main():
    
    # Initialized variables
    
    clock = pygame.time.Clock()     # Initialized the clock to keep a specific frame rate

    

    Run = Start_Screen()    # Creates the starting screen and waits for the user to start 

    Characters = []
    Moved = False
    
    # new_position = random.randint(floor, Spaces) # Gets a random number from 0 - 15 

    #new_character = Friends_Position((floor, floor),(floor, floor), floor) # Friends_Position (Current Position, Old Position, Image of friend)

    Row = random.randint(0,3)
    Col = random.randint(0,3)

    new_character = Friends_Position(Row, Col, 3)     # (x-position, y-position, old x-position, old y-position, Image of friend)
    Characters.append(new_character)

    Draw(Characters)

    while Run:

        clock.tick(10)          # Runs 30 frames per second   clock.tick(Frames per second)

        for event in pygame.event.get():   # pygame.event.get() gets any key pressed
            if event.type == pygame.QUIT:
                Run = False
                break
        
        #Checks if there is avalid position to print 
        
        while Moved:

            #new_position = random.randint()
            for tile in Characters:
                if tile == 1:
                    checking_position = False
                
        # Gets the Keyboard Input
        key_input = pygame.key.get_pressed()

        # Checks if an arrow key is pressed to move the friends
        if key_input[pygame.K_DOWN] or key_input[pygame.K_UP] or key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT]:
            Game_Movement(key_input, Characters)

        # Excape is pressed and pauses the game
        elif key_input[pygame.K_ESCAPE]:
            Run = pause()
        # DElete is pressed and exits out the game
        elif key_input[pygame.K_DELETE]:
            return False

        







    pygame.quit()  ## after player pressed the close window this command closes the window and the python code


if __name__ == "__main__":  # checks if this the main file/ main file that started running the code and if yes starts the program/game
    main()