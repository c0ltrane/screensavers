##!/usr/bin/python2.7

from random import randrange
import pygame
import sys
from pygame.locals import *
from circles_class import *


def main():

	pygame.init()
	pygame.display.set_caption("Markov Circle!!")
	clock = pygame.time.Clock()


	while True:
	    circles = []
	    for i in range(randrange(50,100)):
	    	circle = Circle()
		circles.append(circle)    
	   
	    
	    while True:
		for event in pygame.event.get():
		    #print event
		    if event.type == QUIT:
		        pygame.quit()
		        sys.exit()
		for circle in circles:
			circle.generate_pixel()
	       		
	       
		if circles[0].is_complete():
		    for circle in circles:
		    	del circle
		    break
		clock.tick(100)
		
		pygame.display.update()

if  __name__ =='__main__':
    main()
