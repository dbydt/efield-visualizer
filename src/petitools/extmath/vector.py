# Description:
# vector.py contains functions and classes
# for vector calculations
# 
# Author:
# Calvin Yeung (dbydt)

from math import *

# vector class that supports basic operations
class Vector:
	
	# initialization
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	# get components in tuple
	def get_components(self):
		return (self.x, self.y)
	
	# normalized to unit vector in direction of vector
	def get_normalized(self):
		mag = self.get_magnitude()
		return Vector(self.x / mag, self.y / mag)
	
	# magnitude only
	def get_magnitude(self):
		return sqrt(self.x ** 2 + self.y ** 2)
	
	# angle formed by vector	
	def get_direction(self):
		return atan2(self.x, self.y)
	
	# add function
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	
	# subtract function
	def __sub__(self, other):
		return self + other.negate()
	
	# string representation
	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"
	
	# negate function
	def negate(self):
		return Vector(-self.x, -self.y)