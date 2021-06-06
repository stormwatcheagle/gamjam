# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:06:15 2021
npc header
@author: iviti
"""

import pygame
import time
import random
import math
from bullet_h import *
# Define some colors
from constants_h import *
from utilities_h import *


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


class npc:
    x = 0
    y = 0
    team = 1
    qstateMatrix = []
    color = YELLOW                          #just one color for now until we generalize teams
    speed = 2
    direction = 0
    npcAI = "nothing"
    timeOfLastShot = 0                   #how long its been since it fired
    
    def __init__(self,x,y,team,npcAI):
        self.x = x
        self.y = y
        self.team = team
        self.npcAI = npcAI
        self.color = teamToColor(team)
        
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

    def npcShoot(self,shootDirection,bulletList):
        bulletList.append(bullet(self.x,self.y,shootDirection,self.team))

    def checkCollision(self,bulletList):
        hit = False
        for i in range(len(bulletList)):
            if bulletList[i].team != self.team:                
                r = getRange(self.x + 5,self.y + 5,bulletList[i].x,bulletList[i].y)
                if r < bulletRange:
                    hit = True
        return hit           
