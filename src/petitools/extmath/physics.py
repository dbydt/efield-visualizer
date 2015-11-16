# Description:
# physics.py contains functions and classes
# for calculating physics related values
# 
# Author:
# Calvin Yeung (dbydt)

from math import *
from number import *

# constants
coulomb_const = 8.98 * 10 ** 9

# returns e vector given charge, position in 
# field, and position of charge
def efield_vector(charge, pos1, pos2):
	x1, y1 = pos1
	x2, y2 = pos2
	
	pos_vec = Vector(x1 - x2, y1 - y2)
	
	r = pos_vec.get_magnitude()
	angle = pos_vec.get_direction()
	e_mag = coulomb_const * abs(charge) / r ** 2
	e_vec = Vector(e_mag * sin(angle), e_mag * cos(angle))
	
	return e_vec