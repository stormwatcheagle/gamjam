# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 06:27:16 2021

@author: iviti
"""
import math

def getRange(x1,y1,x2,y2):
    deltaX = x2-x1
    deltaY = y2-y1
    r = math.sqrt(deltaX*deltaX + deltaY*deltaY)
    return r
