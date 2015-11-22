# Description:
# efield.py contains rendering and updating
# functions for the field itself
# 
# Author:
# Calvin Yeung (dbydt)

from math import *
import pygame

from container import *
from charge import *
from petitools.extmath.physics import *
from petitools.extmath.number import *

# class contains charges and renders efield
class ElectricField:
	
	# initialization
	def __init__(self, container):
		self.container = container
		self.field_arr = []
		self.charges = []
		self.remove_buffer = []
		self.avg = 0.0
		
	# render
	def render(self):
		
		# create field values if none
		if len(self.field_arr) == 0 and len(self.charges) > 0:
			self.update_field()
			self.render_field()
	
	# update
	def update(self):
		
		# remove charges if any
		if len(self.remove_buffer) > 0:
			new_charge_list = []
			
			for e in self.charges:
				if not e in self.remove_buffer:
					new_charge_list.append(e)
			
			self.charges = new_charge_list
			self.remove_buffer = []
			
			if len(self.charges) > 0:
				self.update_field()
				self.render_field()
			else:
				self.container.clear_screen()
	
	# render field only when necessary
	def render_field(self):
		screen = self.container.get_screen()
		
		# clear screen
		self.container.clear_screen()
		
		# render field lines		
		for e, pos in self.field_arr:
			
			# avoid division by zero
			if e.get_magnitude() > 0:
				x, y = pos
				i, j = e.get_normalized().get_components()
				
				# find end points of vector
				pos_1 = (x, y)
				pos_2 = (x + i * 16, y + j * 16)
				
				# set whiteness depending on strength of vector
				rgb = e.get_magnitude() / self.avg * 255
				if rgb > 255: rgb = 255
				
				# draw to screen
				line_color = (rgb, rgb, rgb)
				pygame.draw.line(screen, line_color, pos_1, pos_2, 1)
			
		# render charges
		for c in self.charges:
			c.render()
	
	# update field only when necessary
	def update_field(self):
		# add values of individual vectors to list
		self.field_arr = []
		
		for x in range(0, 1024, 20):
			for y in range(0, 640, 20):
				e_vec = self.efield_vec((x, y))
				self.field_arr.append((e_vec, (x, y)))
				
		# find average magnitude of e field vector
		for e, pos in self.field_arr:
			self.avg += e.get_magnitude()
		self.avg /= len(self.field_arr)
	
	# add charges to field
	def add_charge(self, charge):
		self.charges.append(charge)
		
	def remove_charge(self, charge):
		self.remove_buffer.append(charge)
	
	# remove all charges	
	def clear_charges(self):
		self.charges = []
		
	def get_charges(self):
		return self.charges
	
	# gives efield vector at location	
	def efield_vec(self, pos):
		net_vec = Vector(0, 0)
		vecs = []
		n = 0
		
		# create list of efield vectors
		for c in self.charges:
			vecs.append(efield_vector(c.get_charge(), pos, c.get_position()))
		
		# calculate net efield vector
		for f in vecs:
			if self.charges[n].get_charge() > 0:
				net_vec += f
			elif self.charges[n].get_charge() < 0:
				net_vec -= f
			n += 1

		return net_vec