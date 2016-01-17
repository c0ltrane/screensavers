##!/usr/bin/pyhton2.7

import math
import pygame
from pygame.locals import *
from random import randrange


class Circle:
    
    screenSize = (1700,1000)
    setDisplay = pygame.display.set_mode(screenSize)
    singlePixel = pygame.PixelArray(setDisplay)
    
    
    def __init__(self):
        self.radius = 1
    	self.x_origin, self.y_origin = randrange(100,1500), randrange(100,800)
        self.count = 0
        self.r, self.g, self.b = randrange(0,255), randrange(0,255), randrange(0,255)
   	self.max_radius = randrange(5,50)

    def generate_pixel(self):
        while True:
            x, y = randrange(self.radius*-1,self.radius), randrange(self.radius*-1,self.radius)
            if x**2 + y**2 < self.radius**2:
                self.count += 1
                break
        self.singlePixel[self.x_origin+x][self.y_origin+y] = ((self.r,self.g,self.b))
        while self.radius < self.max_radius:
        	self.radius += 1

    def is_complete(self):
        if self.count > 1500:
            self.setDisplay.fill((0,0,0))
            return True
      
              
