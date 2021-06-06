# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 05:49:37 2021

@author: iviti
"""
import pygame
import time
import random
import math
#bulletList = []
#npcList = []                                        #list of npcs

reloadTime = 4                              #time betwen shots
spawnRate = 30
bulletRange = 15                            #distance at which bullet hits someone
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (128,128,0)
GREY = (100,100,100)
screenSize = [1000, 700]
screen = pygame.display.set_mode(screenSize)
nNpcs = 1                                   #number of npcs
baseRange = 50
nTeams = 2                          #number of npc teams + 1 (player)
nBases = 2
playerSpawnRate = 5
playerReloadTime = 2

DOWN = 0
RIGHT = 1
UP = 2
LEFT = 3
