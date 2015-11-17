# Description:
# ui.py contains controller functions
# 
# Author:
# Calvin Yeung (dbydt)

import pygame
from pygame.locals import *

from efield import *
from container import *
from charge import *
from petitools.extmath.number import *

# class controls adding, removing, and modifying charges
class ChargeController:
	
	# initialization
	def __init__(self, container, efield):
		self.container = container
		self.efield = efield
		self.charge_value = 0
	
	# useless render
	def render(self):
		pass
	
	# update
	def update(self):
		self.check_add()
		self.check_remove()
		self.update_charge_value()
	
	# check to see if charges should be added
	def check_add(self):
		# add charge on click	
		efield = self.efield
		button_pressed, _, _ = pygame.mouse.get_pressed()
		pressed = pygame.key.get_pressed()
		
		if button_pressed and not pressed[K_LCTRL]:
			mx, my = pygame.mouse.get_pos()
			charges = efield.get_charges()
			nearby = False
			
			# make sure added charges do not overlap
			for e in charges:
				x, y = e.get_position()
				
				if Vector(x - mx, y - my).get_magnitude() <= 17:
					nearby = True
					break
			
			# add if they do not overlap
			if not nearby:
				efield.add_charge(Charge(self.container, (mx, my), self.charge_value))
			
				efield.update_field()
				efield.render_field()
	
	# check to see if charges should be removed
	def check_remove(self):
		# remove charge on right click	
		efield = self.efield
		button_pressed, _, _ = pygame.mouse.get_pressed()
		pressed = pygame.key.get_pressed()
		
		# remove charges within range of press
		if button_pressed and pressed[K_LCTRL]:
			mx, my = pygame.mouse.get_pos()
			charges = efield.get_charges()
			
			for e in charges:
				x, y = e.get_position()
				
				if Vector(x - mx, y - my).get_magnitude() <= 10:
					efield.remove_charge(e)
	
	# update charge value if necessary
	def update_charge_value(self):
		pressed = pygame.key.get_pressed()
		
		if pressed[K_UP]:
			self.charge_value += 1
		if pressed[K_DOWN]:
			self.charge_value -= 1