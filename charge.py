# Description:
# charge.py contains the class for
# individual charge objects
# 
# Author:
# Calvin Yeung (dbydt)

import pygame
from container import *

# class for individual charges
class Charge:
	def __init__(self, container, pos, charge):
		self.container = container
		self.pos = pos
		self.charge = charge
		
	# render
	def render(self):
		color = (0, 0, 0)
		
		# draw red if positive and blue if negative
		if self.charge > 0:
			color = (255, 0, 0)
		elif self.charge < 0:
			color = (0, 0, 255)
		else:
			color = (150, 150, 150)
		
		# draw point charge
		pygame.draw.circle(self.container.get_screen(), color, self.pos, 10, 0)
	
	# update
	def update(self):
		pass
	
	# returns charge	
	def get_charge(self):
		return self.charge
	
	# returns position in tuple
	def get_position(self):
		return self.pos