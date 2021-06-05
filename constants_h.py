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
bulletRange = 15                             #distance at which bullet hits someone
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255) 
YELLOW = (128,128,0)
screenSize = [1000, 700]
screen = pygame.display.set_mode(screenSize)
nNpcs = 2                                   #number of npcs
