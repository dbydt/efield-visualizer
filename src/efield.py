import pygame
from math import *
from container import *
from petitools.extmath.physics import *
from petitools.extmath.vector import *

# class contains charges and renders efield
class ElectricField:
	
	# initialization
	def __init__(self, container):
		self.container = container
		self.charges = []
		
	# render
	def render(self):
		screen = self.container.get_screen()
		e_vecs = []
		avg = 0.0
		
		# add values of individual vectors to list
		for x in range(-50, 1100, 16):
			for y in range(10, 700, 16):
				e_vec = self.efield_vec((x, y))
				e_vecs.append((e_vec, (x, y)))
		
		# find average magnitude of e field vector
		for e, pos in e_vecs:
			avg += e.get_magnitude()
		avg /= len(e_vecs)
		
		# render field lines		
		for e, pos in e_vecs:
			x, y = pos
			i, j = e.get_normalized().get_components()
			
			# find end points of vector
			pos_1 = (x, y)
			pos_2 = (x + i * 12, y + j * 12)
			
			# set whiteness depending on strength of vector
			rgb = e.get_magnitude() / avg * 255
			if rgb > 255: rgb = 255
			
			# draw to screen
			line_color = (rgb, rgb, rgb)
			pygame.draw.line(screen, line_color, pos_1, pos_2, 1)
		
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