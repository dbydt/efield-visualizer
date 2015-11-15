# Description:
# container.py contains all objects
# to be rendered and updated on the screen
# 
# Author:
# Calvin Yeung (dbydt)

import pygame

# container class
class Container:
	
	# initialization
	def __init__(self, screen):
		self.screen = screen
		self.render_objects = []
	
	# get screen to render
	def get_screen(self):
		return self.screen
	
	# add objects to screen
	def add_object(self, object):
		self.render_objects.append(object)
	
	# get all added objects
	def get_objects(self):
		return self.render_objects
	
	# render the objects
	def render(self):
		for r in self.render_objects:
			r.render()
	
	# update the objects		
	def update(self):
		for r in self.render_objects:
			r.update()