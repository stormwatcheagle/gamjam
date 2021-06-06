# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:58:19 2021
TODO:
    fill out npc class
    give team traits (offense,defense,flakyness)
    create npc ai (micro and macro)
    
    figure out why bullets dont hit sometimes
    create player reload time
    move in spawn points
    make player not leave map

@author: iviti
"""

import pygame
import time
import random
import math
from npc_h import *
from bullet_h import *
from flagBase_h import *
from constants_h import *




#bulletList = []                                     #list of bullets
#npcList = []                                        #list of npcs





   
def spawnNpc(team,npcAI,x,y):
    npcList.append(npc(x,y,team,npcAI ))
 
def spawnBase(team):
    baseList.append(flagBase(random.randint(50,screenSize[0]-50),random.randint(50,screenSize[1]-50),team%nTeams))
 
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 13 + y], [13 + x,  y - 7], 2)
    pygame.draw.line(screen, RED, [5 + x, 13 + y], [ x - 3,  y - 7], 2)





if __name__ == "__main__":    
    # Setup
    pygame.init()
    global bulletList                                                   #may not be necessary to global these anymore
    global npcList
    global baseList
    gameCounter = 0
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Hide the mouse cursor
    pygame.mouse.set_visible(0)
         
    bulletList = []                                     #list of bullets
    npcList = []   
    baseList = []
    playerDeathToggle = 0
    # Set the width and height of the screen [width,height]
    gamesWon = 0
    gamesLost = 0
    lastOwner = 0
    titleText = "the game"
    pygame.display.set_caption(titleText)
    gameCounter = gameCounter + 1
    lastTimeShot = 0
    # Loop until the user clicks the close button.
    done = False
    while not done:
    
    
         
        # Speed in pixels per frame
        x_speed = 0
        y_speed = 0
         
        # Current position
        x_coord = 10
        y_coord = 10
        for i in range(nNpcs):
            spawnNpc(1,"rando",random.randint(0,screenSize[0]),random.randint(0,screenSize[1]))
        for i in range(nBases):
            spawnBase(i)
        # -------- Main Program Loop -----------
        wonOrLost = False
        while not wonOrLost:
            # --- Event Processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    wonOrLost = True
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
                        if time.time() - lastTimeShot > playerReloadTime:
                            lastTimeShot = time.time()
                            fireBullet(x_coord,y_coord,0,0,bulletList)   
                    elif event.key == pygame.K_d:
                        if time.time() - lastTimeShot > playerReloadTime:
                            lastTimeShot = time.time()
                            fireBullet(x_coord,y_coord,1,0,bulletList)
                    elif event.key == pygame.K_a:
                        if time.time() - lastTimeShot > playerReloadTime:
                            lastTimeShot = time.time()
                            fireBullet(x_coord,y_coord,3,0,bulletList)
                    elif event.key == pygame.K_s:
                        if time.time() - lastTimeShot > playerReloadTime:
                            lastTimeShot = time.time()
                            fireBullet(x_coord,y_coord,2,0,bulletList)                    
                        
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
                if bulletList[i].checkPlayerKill(x_coord,y_coord):
                    print("player shot")
                    playerDeathTimer = time.time()
                    playerDeathToggle = 1
                    x_coord = -99999
                    y_coord = -99999
     #               pygame.quit()                                  #leave quit out until we get a gentler way of exiting
                if not bulletList[i].checkInBounds():
                    bulletList.pop(i)
            if playerDeathToggle == 1:
                if time.time() - playerDeathTimer > playerSpawnRate:
                    playerDeathToggle = 0
                    for i in range(len(baseList)):
                        if baseList[i].team == 0:
                            x_coord = baseList[i].x
                            y_coord = baseList[i].y
                    
            for i, n in reversed(list(enumerate(npcList))):
                npcList[i].updateNpc()
                npcList[i].drawNpc()
                if npcList[i].npcAI == "rando":
                    npcList[i].randomDirection()
                    if time.time() - npcList[i].timeOfLastShot > reloadTime:
                        npcList[i].npcShoot(random.randint(0,3),bulletList)
                        npcList[i].timeOfLastShot = time.time()
                    if npcList[i].checkCollision(bulletList):
                        npcList.pop(i) 
            checkWin = True
            for i, f in reversed(list(enumerate(baseList))):
                baseList[i].updateTeam(npcList,x_coord,y_coord)
                baseList[i].drawBase()
                if time.time() - baseList[i].timeOfLastSpawn > spawnRate:
                    spawnNpc(baseList[i].team,"rando",baseList[i].x,baseList[i].y)
                    baseList[i].timeOfLastSpawn = time.time()
                if checkWin == True:
                    baseOwner = baseList[i].team
                    if baseOwner != lastOwner:
                        checkWin = False
                    lastOwner = baseOwner
            if checkWin == True:
                wonOrLost = True
                if baseList[0].team == 0:
                    gamesWon = gamesWon + 1
                else:
                    gamesLost = gamesLost + 1
                npcList.clear()
                baseList.clear()
                bulletList.clear()
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
            # Limit frames per second
            clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
