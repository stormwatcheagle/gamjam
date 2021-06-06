# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:09:47 2021

@author: iviti
"""

import pygame
import time
import random
import math
from constants_h import *
from utilities_h import *


class bullet:                       #bullet class
    direction = 0
    x = 0
    y = 0
    bSpeed = 6             #default bullet speed is 3
    team = 0
    color = BLUE
    def __init__(self, xPos,yPos,direction,team):
        self.x = xPos    # instance variable unique to each instance
        self.y = yPos    # instance variable unique to each instance
        self.direction = direction
        self.team = team
        self.color = teamToColor(team)
        
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
         pygame.draw.ellipse(screen, self.color, [self.x,self.y, 5, 5], 0)

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
    def checkPlayerKill(self,x_player,y_player):
        if self.team != 0:
            deltaX = self.x - (x_player + 5)                              #should just make a separate function for finding euclidean distance
            deltaY = self.y - (y_player + 5)
            r = math.sqrt(deltaX*deltaX + deltaY*deltaY)                            
            if r < bulletRange:
                return True
            else:
                return False

def fireBullet(x,y,direction,team,bulletList):
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
