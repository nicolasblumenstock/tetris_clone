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
background_color = (255, 255, 255)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("dear god please work")
game_on = True
turn = 0
# test_block = Test_Block('./images/e_starman.gif',screen,400,500)
# test_block2 = Test_Block('./images/e_starman.gif',screen,300,500)
# test_block3 = Test_Block('./images/e_starman.gif',screen,200,500)
test_group = Group()
block_group = Group()
# test_group.add(test_block)


# ** -- MAIN GAME LOOP -- **
while game_on:
# ** -- FRAME COUNTER -- **	
	frame += 1
# ** -- BACKGROUND LOAD -- **	
	screen.fill(background_color)

	if len(block_group) == 0:
		block_types = ['I','J','L','S','Z','T','SQUARE']
		random_number = randint(0, len(block_types) - 1)
		if block_types[random_number] == 'I':
			block = Block(screen,'./images/I_Block.png')
		elif block_types[random_number] == 'J':
			block = Block(screen,'./images/J_Block.png')
		elif block_types[random_number] == 'L':
			block = Block(screen,'./images/L_Block.png')
		elif block_types[random_number] == 'S':
			block = Block(screen,'./images/S_Block.png')
		elif block_types[random_number] == 'Z':
			block = Block(screen,'./images/Z_Block.png')
		elif block_types[random_number] == 'T':
			block = Block(screen,'./images/T_Block.png')
		else:
			block = Block(screen,'./images/Square.png')
		block_group.add(block)		


	for block in block_group:
		button_events(block)
		block.movement(turn)

		for blocks in block_group:
			if blocks.rect.bottom >= 500:
				block_group.remove(blocks)
				test_group.add(blocks)


		for tests in test_group:
			if (block.rect.bottom >= tests.rect.top and block.rect.left <= tests.rect.right):
				block_group.remove(block)
				test_group.add(block)
			elif (block.rect.bottom >= tests.rect.top and block.rect.right >= tests.rect.left):
				block_group.remove(block)
				test_group.add(block)
			if (block.rect.bottom >= 500 and block.rect.left <= tests.rect.right):
				block_group.remove(block)
				test_group.add(block)
			elif (block.rect.bottom >= 500 and block.rect.right >= tests.rect.left):
				block_group.remove(block)
				test_group.add(block)
			if (block.rect.bottom >= 500 and block.rect.left <= 100):
				block_group.remove(block)
				test_group.add(block)
			elif (block.rect.bottom >= 500 and block.rect.left >= 400):
				block_group.remove(block)
				test_group.add(block)
			elif (block.rect.bottom >= 500):
				block_group.remove(block)
				test_group.add(block)

	for test in test_group:
		test.draw_me()



	pygame.display.flip()



