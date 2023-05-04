import time
import sys

import pygame
""" a module is a piece of code that can run indivitually and can run another script as well(inheritance) """
def init():
    pygame.init()
    win = pygame.display.set_mode((500, 400))
    pygame.display.update()

    def getkey(keyname):
        ans = False
        keyInput = pygame.key.get_pressed()
        myKey = getattr(pygame, "K_{}".format(keyname))
        if keyInput[myKey]:
            ans = True
        return ans


            #  fuction to get the key press #

def main():
          if getkey("LEFT"):
             print("Left key is pressed")

          if getkey("Right"):
              print(" Right key pressed")


if __name__== '__main__':
        init ()
while True :
        main()

        #this is the main module#

        #This script is using the Pygame library to check for keyboard inputs and respond to them.
        # The script first initializes Pygame, creates a window with a specific size,
        # and updates the display. It then defines a function getkey() that takes in a keyname
        # and checks if that key is currently being pressed.
        # The function uses the getattr() function to convert the keyname to the corresponding Pygame key constant and
        # checks if that key is currently pressed using the pygame.key.get_pressed() method.

        # so technically It is only checking for the left and right arrow keys
        # and printing a message when they are pressed.