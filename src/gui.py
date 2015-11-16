# Description:
# gui.py contains classes for user interface
# 
# Author:
# Calvin Yeung (dbydt)

import pygame
from container import *

# menu class for adding new charges, setting values, etc
class Menu:
	
	# initialization
	def __init__(self, container):
		self.container = container
		self.gui_items = [ValueDisplay(container)]
	
	# render
	def render(self):
		base_color = (100, 100, 100)
		pygame.draw.rect(self.container.get_screen(), base_color, (0, 0, 1024, 35), 0)
		
		for i in self.gui_items:
			i.render()
	
	# update
	def update(self):
		for i in self.gui_items:
			i.update()
			
# display and selected for charge magnitudes
class ValueDisplay:
	
	# initialization
	def __init__(self, container):
		self.container = container
		self.right = pygame.image.load("../images/right_arrow.png")
		self.left = pygame.image.load("../images/left_arrow.png")
	
	# render
	def render(self):
		screen = self.container.get_screen()
		#screen.blit(self.left, (5, 5))
		#screen.blit(self.right, (100, 5))
		
	# update
	def update(self):
		pass