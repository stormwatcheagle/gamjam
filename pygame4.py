# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:58:19 2021

@author: iviti
"""

import pygame
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
bulletList = []                                     #list of bullets

 
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
 
class bullet:                       #bullet class
    direction = 0
    x = 0
    y = 0
    bSpeed = 3             #default bullet speed is 3
    
    def __init__(self, xPos,yPos,direction):
        self.x = xPos    # instance variable unique to each instance    
        self.y = yPos    # instance variable unique to each instance
        self.direction = direction
    
    def updateBullet(self):
        if self.direction == 0:
            self.y = self.y - self.bSpeed
        if self.direction == 1:
            self.x = self.x + self.bSpeed
        if self.direction == 2:
            self.y = self.y + self.bSpeed
        if self.direction == 3:
            self.x = self.x - self.bSpeed
        
    def drawBullet(self):
         pygame.draw.ellipse(screen, BLACK, [self.x,self.y, 10, 10], 0)


    
    
def fireUp(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,0))
def fireRight(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,1))
def fireDown(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,2))
def fireLeft(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,3))



size = [2000, 1000]    
screen = pygame.display.set_mode(size)   
if __name__ == "__main__":    
    # Setup
    pygame.init()
     
    # Set the width and height of the screen [width,height]

     
    pygame.display.set_caption("My Game")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    # Hide the mouse cursor
    pygame.mouse.set_visible(0)
     
    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0
     
    # Current position
    x_coord = 10
    y_coord = 10
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # User pressed down on a key
     
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
                elif event.key == pygame.K_w:
                    fireUp(x_coord,y_coord)
                elif event.key == pygame.K_d:
                    fireRight(x_coord,y_coord)
                elif event.key == pygame.K_a:
                    fireLeft(x_coord,y_coord)
                elif event.key == pygame.K_s:
                    fireDown(x_coord,y_coord)                    
                    
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
     
        # --- Game Logic
     
        # Move the object according to the speed vector.
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed
     
        # --- Drawing Code
     
        # First, clear the screen to WHITE. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
     
        draw_stick_figure(screen, x_coord, y_coord)
        for i in range(len(bulletList)):
            bulletList[i].updateBullet()
            bulletList[i].drawBullet()
            
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # Limit frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
