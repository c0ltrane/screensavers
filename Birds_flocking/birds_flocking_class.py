from random import *
import pygame
from pygame.locals import *


class Walker:
	
	screenSize = (1700,1000)
	setDisplay = pygame.display.set_mode(screenSize)
	singlePixel = pygame.PixelArray(setDisplay)
	
	def __init__(self):
		self.x, self.y = randrange(300,500),randrange(300,350)
		self.direction = (-1,3,-1,2)
		self.color = (255,255,255)

		
	def fly(self):
		x_step, y_step = 0, 0
		while x_step == 0 and y_step == 0:
			x_step = randrange(self.direction[0],self.direction[1])
			y_step = randrange(self.direction[2],self.direction[3])

	
		self.x = (self.x + x_step) % 1550
		self.y = (self.y + y_step) % 850
		
	
		self.singlePixel[self.x][self.y] = ((self.color[0],self.color[1],self.color[2]))
		self.singlePixel[self.x+1][self.y] = ((self.color[0],self.color[1],self.color[2]))
		self.singlePixel[self.x][self.y+1] = ((self.color[0],self.color[1],self.color[2]))
		self.singlePixel[self.x-1][self.y] = ((self.color[0],self.color[1],self.color[2]))
		self.singlePixel[self.x][self.y-1] = ((self.color[0],self.color[1],self.color[2]))

		self.singlePixel[self.x+1][self.y+1] = ((self.color[0],self.color[1],self.color[2]))
		self.singlePixel[self.x-1][self.y+1] = ((self.color[0],self.color[1],self.color[2]))
		self.singlePixel[self.x+1][self.y-1] = ((self.color[0],self.color[1],self.color[2]))
		self.singlePixel[self.x-1][self.y-1] = ((self.color[0],self.color[1],self.color[2]))

	def change_direction(self, direction, color):
		self.direction = direction
		self.color = color



		
	
	
