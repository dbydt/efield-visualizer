import pygame
from math import *
from container import *
from extmath import *

# class contains charges and renders efield
class ElectricField:
	
	# initialization
	def __init__(self, container):
		self.container = container
		self.charges = []
		
	# render
	def render(self):
		
		# render field lines
		line_color = (10, 10, 240)
		for x in range(-50, 1100, 16):
			for y in range(10, 700, 16):
				e_vec = self.efield_vec((x, y))
				i, j = e_vec.get_normalized().get_values()
				
				pos_1 = (x, y)
				pos_2 = (x + i * 12, y + j * 12)
				
				pygame.draw.line(self.container.get_screen(), line_color, pos_1, pos_2, 1)
		
		# render charges
		for c in self.charges:
			c.render()
	
	# update
	def update(self):
		for c in self.charges:
			c.update()
	
	# add charges to field
	def add_charge(self, charge):
		self.charges.append(charge)
	
	# remove all charges	
	def clear_charges(self):
		self.charges = []
	
	# gives efield vector at location	
	def efield_vec(self, pos):
		vecs = []
		
		# create list of efield vectors
		for c in self.charges:
			x1, y1 = pos
			x2, y2 = c.get_position()
			
			pos_vec = Vector(x2 - x1, y2 - y1)
			r = pos_vec.magnitude()
			
			f_mag = 8.98 * 10 ** 9 * abs(c.get_charge()) / r ** 2
			angle = pos_vec.direction()
			
			vec = Vector(-f_mag * sin(angle), -f_mag * cos(angle))
			vecs.append(vec)
			
		net_vec = Vector(0, 0)
		n = 0
		
		# calculate net efield vector
		for f in vecs:
			if self.charges[n].get_charge() > 0:
				net_vec += f
			elif self.charges[n].get_charge() < 0:
				net_vec -= f
			n += 1

		return net_vec