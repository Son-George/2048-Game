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

Image_Locations = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
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
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Adolf_Cup.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Moy_6.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Ferny_7.JPG").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Danny_8.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\George_9.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Randy_10.jpg").convert_alpha(),
        pygame.image.load("C:\\Users\\georg\\OneDrive\\Desktop\\Testing and Gaming in C++\\Python Games\\2048 Game\\Images\\Hagrid_11.jpg").convert_alpha(),]



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

    Lost_text = FONT.render("Game Over: Press the Spacebar to restart", 1, "white")
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
            Reset_Game()
            return True

def Reset_Game():
    for row in range(4):
        for col in range(4):
            Image_Locations[row][col] = 0
    
    Row = random.randint(0,3)
    Col = random.randint(0,3)

    new_character = Friends_Position(Row, Col, 0)     # (x-position, y-position, old x-position, old y-position, Image of friend)
    Image_Locations[Row][Col] = new_character        # Stores the friend in an array where its [row][col] corresponde to its location on the grid

    Draw()


def Draw(Direction = "Emp"):

    Window.blit(pygame.transform.scale(Background, (WIDTH, Height)), (floor,floor))
    Window.blit(pygame.transform.scale(Grid, (190*4, 190*4)), Tile_space[0][0])

    if Direction == "Emp":
        # Iterate through the array that contains 
        for row in Image_Locations:
            for image in row:
                if image != 0:
                    Window.blit(pygame.transform.scale(Friend[image.Friend], Box_Size), (image.X, image.Y))

    # Iterate through the array that contains 
    elif Direction[pygame.K_LEFT]:
        for row in range(4):
            for col in range(4):
                image = Image_Locations[row][col]
                if image != 0:
                    Window.blit(pygame.transform.scale(Friend[image.Friend], Box_Size), (image.X, image.Y))

    elif Direction[pygame.K_RIGHT]:
        for row in range(4):
            for col in range(3, -1, -1):
                image = Image_Locations[row][col]
                if image != 0:
                    Window.blit(pygame.transform.scale(Friend[image.Friend], Box_Size), (image.X, image.Y))

    elif Direction[pygame.K_UP]:
        for col in range(4):
            for row in range(4):
                image = Image_Locations[row][col]
                if image != 0:
                    Window.blit(pygame.transform.scale(Friend[image.Friend], Box_Size), (image.X, image.Y))

    elif Direction[pygame.K_DOWN]:
        for col in range(4):
            for row in range(3, -1, -1):
                image = Image_Locations[row][col]
                if image != 0:
                    Window.blit(pygame.transform.scale(Friend[image.Friend], Box_Size), (image.X, image.Y))

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


def Game_Movement(key):

    Image_Moved = False         # variable to check if an imaged moved

    if key[pygame.K_LEFT]:          # Only moves the Col position the row position stays the same
        
        for row in range(4):
            position = 0            # since we are moving to the left the most most position is 0 in the col position
            for col in range(4):
                player = Image_Locations[row][col]
                if player != 0:     # check if the position of the Image_location has an image
                    #Image_Moved = True
                    player.Col = position       # moves the left most image to the left most position and goes through the row
                    position += 1               # since an image is already at the left most position we move one position to the right (+1)
                    Image_Locations[player.Row][player.Old_Col] = 0     # changes the image at this current [row][col] place to zero since the image moved to a different position
                    Image_Locations[player.Row][player.Col] = player    # moves the player/image to the new col position
                    if player.Col != player.Old_Col:
                        Image_Moved = True

    elif key[pygame.K_RIGHT]:         # Only moves the Col position the row position stays the same
        
        for row in range(4):
            position = 3            # since we are moving to the Right the most most position is 3 in the col position
            for col in range(3, -1, -1):
                player = Image_Locations[row][col]
                if player != 0:     # check if the position of the Image_location has an image
                    #Image_Moved = True
                    player.Col = position       # moves the left most image to the Right most position and goes through the row
                    position -= 1               # since an image is already at the Right most position we move one position to the left (-1)
                    Image_Locations[player.Row][player.Old_Col] = 0     # changes the image at this current [row][col] place to zero since the image moved to a different position
                    Image_Locations[player.Row][player.Col] = player    # moves the player/image to the new col position
                    if player.Col != player.Old_Col:
                        Image_Moved = True

    elif key[pygame.K_DOWN]:         # Only moves the Col position the row position stays the same

        for col in range(3, -1, -1):
            position = 3
            for row in range(3, -1, -1):
                player = Image_Locations[row][col]
                if player != 0:
                    #Image_Moved = True
                    player.Row = position
                    position -= 1
                    Image_Locations[player.Old_Row][player.Col] = 0
                    Image_Locations[player.Row][player.Col] = player
                    if player.Row != player.Old_Row:
                        Image_Moved = True

    elif key[pygame.K_UP]:         # Only moves the Col position the row position stays the same

        for col in range(4):
            position = 0
            for row in range(4):
                player = Image_Locations[row][col]
                if player != 0:
                    #Image_Moved = True
                    player.Row = position
                    position += 1
                    Image_Locations[player.Old_Row][player.Col] = 0
                    Image_Locations[player.Row][player.Col] = player
                    if player.Row != player.Old_Row:
                        Image_Moved = True

    if Image_Moved:
        Move_Friend(key)
        return True
    return False
                    

def Move_Friend(Direction):
    
    for row in Image_Locations[:]:              # iterates through each row of the image_location
        for image in row:   # iterates through each element in the row of image_location

            if image != 0:                      # checks if the current item is an image
                Tiles_Moved = abs(image.Col - image.Old_Col) + abs(image.Row - image.Old_Row)   # checks how many tiles the image change from its old position
                image.Old_Row = image.Row
                image.Old_Col = image.Col
                for i in range(10 * Tiles_Moved):    # the loop iterates 10 times for one tile space and is multiplied by how many 
                    if Direction[pygame.K_LEFT]:     # if the left key was detected it moves the image 19 frames to the left
                        image.X -= Frames
                        Draw(Direction)

                    elif Direction[pygame.K_RIGHT]:    # if the Right key was detected it moves the image 19 frames to the right
                        image.X += Frames
                        Draw(Direction)

                    elif Direction[pygame.K_UP]:    # if the Up key was detected it moves the image 19 frames up
                        image.Y -= Frames
                        Draw(Direction)

                    elif Direction[pygame.K_DOWN]:    # if the Down key was detected it moves the image 19 frames down
                        image.Y += Frames
                        Draw(Direction)

def Open_Space():# used to detect if there are free spaces on the board

    for row in range(4):
        for col in range(4):
            if Image_Locations[row][col] == 0:
                return True
    return False
   
def Add_Image():
    #Open_Space = False

    #for row in range(4):
        #for col in range(4):
        #    if Image_Locations[row][col] == 0:
        #        Open_Space = True
        #        break
    free = Open_Space()
    while free:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if Image_Locations[row][col] == 0:
            Image_Locations[row][col] = Friends_Position(row, col, 5)
            return False

    return True

def main():
    
    # Initialized variables
    
    clock = pygame.time.Clock()     # Initialized the clock to keep a specific frame rate

    Run = Start_Screen()    # Creates the starting screen and waits for the user to start 

    Row = random.randint(0,3)
    Col = random.randint(0,3)

    new_character = Friends_Position(Row, Col, 4)     # (x-position, y-position, old x-position, old y-position, Image of friend)
    Image_Locations[Row][Col] = new_character        # Stores the friend in an array where its [row][col] corresponde to its location on the grid
 

    Draw()

    while Run:

        clock.tick(30)          # Runs 30 frames per second   clock.tick(Frames per second)

        for event in pygame.event.get():   # pygame.event.get() gets any key pressed
            if event.type == pygame.QUIT:
                Run = False
                break
        
                
        # Gets the Keyboard Input
        key_input = pygame.key.get_pressed()

        # Checks if an arrow key is pressed to move the friends
        if key_input[pygame.K_DOWN] or key_input[pygame.K_UP] or key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT]:
            ADD = Game_Movement(key_input)
            OPEN = Open_Space()
            if ADD and OPEN:
                Game_Reset = Add_Image()
                if Game_Reset:
                    Game_Over()
                Draw()
                time.sleep(0.3)
            elif not OPEN:
                Game_Over()
                Draw()
                time.sleep(0.1)

        # Excape is pressed and pauses the game
        elif key_input[pygame.K_ESCAPE]:
            Run = pause()
        # DElete is pressed and exits out the game
        elif key_input[pygame.K_DELETE]:
            return False

        
        Draw()


    pygame.quit()  ## after player pressed the close window this command closes the window and the python code


if __name__ == "__main__":  # checks if this the main file/ main file that started running the code and if yes starts the program/game
    main()