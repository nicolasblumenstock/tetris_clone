# ** -- IMPORTS -- **
import pygame
from random import randint
from Game_Functions import *
from Block import Block
from pygame.sprite import Group, groupcollide
from Test_Block import Test_Block

# ** -- INITIALIZE PYGAME -- **
pygame.init()

# ** -- VARIABLES -- **
frame = 0
screen_size = (900, 675)
tetris_zone = {
	'x': 300,
	'y': 500}
background_color = (255, 255, 255)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("dear god please work")
game_on = True
turn = 0
block = Block(screen,'./images/e_mad_duck.gif')
test_block = Test_Block('./images/e_starman.gif',screen,400,500)
test_block2 = Test_Block('./images/e_starman.gif',screen,300,500)
test_block3 = Test_Block('./images/e_starman.gif',screen,200,500)
block_group.add(block)
test_group = Group()
block_group = Group()
test_group.add(test_block,test_block2,test_block3)

# block_types = {
# 	'square':
# 	'i':
# 	'L':
# 	'reverse_L':
# 	'T':
# 	'Z':
# 	'reverse_Z':
# }

# block = Block(screen)


# ** -- MAIN GAME LOOP -- **
while game_on:
# ** -- FRAME COUNTER -- **	
	frame += 1
# ** -- BACKGROUND LOAD -- **	
	screen.fill(background_color)


	button_events(block)

	# if i in block_group:
	if block in block_group:
		block.movement(turn)

	test_block.draw_me()
	test_block2.draw_me()
	test_block3.draw_me()

	for tests in test_group:
		if block.rect.bottom >= tests.rect.top:
			block.fall = 0
			block.speed = 0
			block_group.remove(block)
			test_group.add(block)
		new_block = Block(screen,'./images/e_mad_duck.gif')
		block_group.add(new_block)
		if (new_block in block_group and block in test_group):
			block.fall = 1
			block.speed = 10
			new_block.movement(turn)


	# while new_block in block_group:
	# 	new_block.movement(turn)
	# 	for tests in test_group:
	# 		if new_block.rect.bottom >= tests.rect.top:
	# 			new_block.fall = 0
	# 			new_block.speed = 0
	# 			block_group.remove(new_block)
	# 			test_group.add(new_block)

	# if block.fall == 0 and block.speed == 0:
	# 	block_group.remove(block)
	# 	test_group.add(block)
	# 	block_group.add(Block(screen,'./images/e_mad_duck.gif'))

	pygame.display.flip()



