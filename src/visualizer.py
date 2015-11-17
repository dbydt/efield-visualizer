# Description:
# visualizer.py starts the program
# 
# Author:
# Calvin Yeung (dbydt)

import pygame, sys
from pygame.locals import *

from container import *
from efield import *
from charge import *
from ui import *

# initialization
pygame.init()
screen = pygame.display.set_mode((1024, 640))
pygame.display.set_caption("Electric Field Visualizer")
clock = pygame.time.Clock()

container = Container(screen)
efield = ElectricField(container)
controller = ChargeController(container, efield)

# test charges (for experimental purposes)
efield.add_charge(Charge(container, (400, 250), 1))
efield.add_charge(Charge(container, (600, 250), -3))
efield.add_charge(Charge(container, (400, 450), -3))
efield.add_charge(Charge(container, (600, 450), 1))

# add objects to container
container.add_object(efield)
container.add_object(controller)

# game loop
while True:
	# game tick
	clock.tick(30)
	
	# print fps (testing purposes)
	print int(clock.get_fps()), "fps"
	
	# render and update container
	container.render()
	container.update()
	
	pygame.display.update()
	
	# check for exit
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()