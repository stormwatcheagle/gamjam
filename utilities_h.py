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

def teamToColor(team):
    redPart =abs((team*11719  )%255 - 40)               #first make it pseudorandom then subtract 40 so its not too white  then abs so its not negative
    greenPart = abs((team*12451  )%255 - 40)
    bluePart = abs((team*12953  )%255 - 40)
    color = (redPart,greenPart,bluePart)
    return color
