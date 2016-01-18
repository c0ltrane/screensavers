from random import *
import pygame
from pygame.locals import *

#COLORS
red = ((255,0,0))
green = ((0,255,0))
blue = ((0,0,255))
black = ((0,0,0,))
white = ((255,255,255))
yellow = ((255,217,0))
purple = ((69,0,68))
black = ((0,0,0))

colors = [white, blue, green, yellow, purple, red]



class Walker:
	
	screenSize = (1700,1000)
	setDisplay = pygame.display.set_mode(screenSize)
	singlePixel = pygame.PixelArray(setDisplay)
	
	def __init__(self):
		self.x, self.y = randrange(300,500),randrange(300,350)
		((self.r,self.g,self.b)) = colors[0]
		self.direction = (-1,3,-1,2)

		
	def fly(self):
		x_step, y_step = 0, 0
		while x_step == 0 and y_step == 0:
			x_step = randrange(self.direction[0],self.direction[1])
			y_step = randrange(self.direction[2],self.direction[3])

	
		self.x = (self.x + x_step) % 1550
		self.y = (self.y + y_step) % 850
		
	
		self.singlePixel[self.x][self.y] = ((self.r,self.g,self.b))
		self.singlePixel[self.x+1][self.y] = ((self.r,self.g,self.b))
		self.singlePixel[self.x][self.y+1] = ((self.r,self.g,self.b))
		self.singlePixel[self.x-1][self.y] = ((self.r,self.g,self.b))
		self.singlePixel[self.x][self.y-1] = ((self.r,self.g,self.b))

		self.singlePixel[self.x+1][self.y+1] = ((self.r,self.g,self.b))
		self.singlePixel[self.x-1][self.y+1] = ((self.r,self.g,self.b))
		self.singlePixel[self.x+1][self.y-1] = ((self.r,self.g,self.b))
		self.singlePixel[self.x-1][self.y-1] = ((self.r,self.g,self.b))

	def change_direction(self, direction):
		self.direction = direction



		
	
	
