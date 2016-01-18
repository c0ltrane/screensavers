#! usr/bin/python
from random import randrange
import pygame
import sys 
from pygame.locals import *
from birds_flocking_class import *

pygame.init()

screenSize = (1700,1500)
setDisplay = pygame.display.set_mode(screenSize, RESIZABLE)
pygame.display.set_caption("Random Walk!")
singlePixel = pygame.PixelArray(setDisplay)
fps = 100
five_seconds_interval = 5*fps
total_frames = 0

clock = pygame.time.Clock()

#DIRECTIONS
east = (-1,3,-1,2)
west = (-3,1,-1,2)
north = (-1,2,-3,1)
south = (-1,2,-1,3)
northwest = (-2,1,-2,1)
northeast = (-1,3,-2,1)
southeast = (-1,3,-1,3)
southwest = (-3,1,-1,3)

directions = [east, west, north, south, northeast, northwest, southeast, southwest]

birds = []
for i in range(100):
	bird = Walker()
	birds.append(bird)
	
while True:
	
	for event in pygame.event.get():
		#print event
		if event.type == QUIT or event.type == KEYDOWN:
			pygame.quit()
			sys.exit()
	
	for bird in birds:
		bird.fly()

	clock.tick(fps)
	pygame.display.flip()
	setDisplay.fill((0,0,0))

	total_frames += 1

	if total_frames % five_seconds_interval == 0:
		direction = choice(directions)
		for bird in birds:
			bird.change_direction(direction)


	
