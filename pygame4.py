# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:58:19 2021
TODO:
    fill out npc class
    give team traits (offense,defense,flakyness)

    make bullets kill
    npc spawn
    
    player respawn

    create bases
    spawn npcs at bases
    allow bases to change teams

@author: iviti
"""

import pygame
import time
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255) 
YELLOW = (128,128,0)

bulletList = []                                     #list of bullets
npcList = []                                        #list of npcs
 
screenSize = [1000, 700]
screen = pygame.display.set_mode(screenSize)

 
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

def drawNpc(screen,x,y,color):
    # Head
    pygame.draw.ellipse(screen, color, [1 + x, y, 10, 10], 0)

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
    bSpeed = 6             #default bullet speed is 3
    team = 0

    def __init__(self, xPos,yPos,direction,team):
        self.x = xPos    # instance variable unique to each instance
        self.y = yPos    # instance variable unique to each instance
        self.direction = direction
        self.team = team

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
         pygame.draw.ellipse(screen, BLUE, [self.x,self.y, 5, 5], 0)

    def checkInBounds(self):
        inBounds = 1
        if self.x > screenSize[0]:
            inBounds = 0
        if self.y > screenSize[1]:
            inBounds = 0
        if self.x < 0:
            inBounds = 0
        if self.y < 0 :
            inBounds = 0
        return inBounds


class npc:
    x = 0
    y = 0
    team = 0
    qstateMatrix = []
    color = YELLOW                          #just one color for now until we generalize teams
    speed = 2
    direction = 0

    def __init__(self,x,y,team):
        self.x = x
        self.y = y
        self.team = team
    
    def drawNpc(self):
        # Head
        pygame.draw.ellipse(screen, self.color, [1 + self.x, self.y, 10, 10], 0)

    # Legs
        pygame.draw.line(screen, BLACK, [5 + self.x, 17 + self.y], [10 + self.x, 27 + self.y], 2)
        pygame.draw.line(screen, BLACK, [5 + self.x, 17 + self.y], [self.x, 27 + self.y], 2)

    # Body
        pygame.draw.line(screen, RED, [5 + self.x, 17 + self.y], [5 + self.x, 7 + self.y], 2)

    # Arms
        pygame.draw.line(screen, RED, [5 + self.x, 7 + self.y], [9 + self.x, 17 + self.y], 2)
        pygame.draw.line(screen, RED, [5 + self.x, 7 + self.y], [1 + self.x, 17 + self.y], 2)


    def updateNpc(self):
        if self.direction == 0:
            self.y = (self.y - self.speed)%screenSize[1]
        if self.direction == 1:
            self.x = (self.x + self.speed)%screenSize[0]
        if self.direction == 2:
            self.y = (self.y + self.speed)%screenSize[1]
        if self.direction == 3:
            self.x = (self.x - self.speed)%screenSize[0]

    def randomDirection(self):
        self.direction = random.randint(0,3)


def spawnNpc():
    npcList.append(npc(random.randint(0,screenSize[0]),random.randint(0,screenSize[1]),1 ))

def fireBullet(x,y,direction,team):
    fire = bullet(x,y,direction,team)
    bulletList.append(fire)


def fireUp(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,0))
def fireRight(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,1))
def fireDown(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,2))
def fireLeft(x,y):                       #firing upwards function (could just have a general firing function too)
    bulletList.append(bullet(x,y,3))


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
    spawnNpc()
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
                    fireBullet(x_coord,y_coord,0,0)
                elif event.key == pygame.K_d:
                    fireBullet(x_coord,y_coord,1,0)
                elif event.key == pygame.K_a:
                    fireBullet(x_coord,y_coord,3,0)
                elif event.key == pygame.K_s:
                    fireBullet(x_coord,y_coord,2,0)                    
                    
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
        for i, b in reversed(list(enumerate(bulletList))):              #go backwards so it doesnt break when you destroy an element in the middle of going through the list
            bulletList[i].updateBullet()
            bulletList[i].drawBullet()
            if not bulletList[i].checkInBounds():
                bulletList.pop(i)

        for i, n in reversed(list(enumerate(npcList))):
            npcList[i].updateNpc()
            npcList[i].drawNpc()
            npcList[i].randomDirection()
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # Limit frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
