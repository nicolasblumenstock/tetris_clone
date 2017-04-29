import pygame
import sys
from random import randint
from Block import Block

def button_events(block):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == 97:
				block.should_move('left', True)
			elif event.key == 100:
				block.should_move('right', True)
			elif event.key == 115:
				block.should_move('drop_down', True)
			elif event.key == 113:
				block.should_move('turn_left', True)
			elif event.key == 101:
				block.should_move('turn_right', True)
		elif event.type == pygame.KEYUP:
			if event.key == 97:
				block.should_move('left', False)
			if event.key == 100:
				block.should_move('right', False)
			if event.key == 115:
				block.should_move('drop_down', False)
			if event.key == 113:
				block.should_move('turn_left', False)
			if event.key == 101:
				block.should_move('turn_right', False)

# def random_blocks(screen,block):
# 	block_types = ['I','J','L','S','Z','T','SQUARE']
# 	random_number = randint(0, len(block_types) - 1)
# 	if block_types[random_number] == 'I':
# 		block = Block(screen,'./images/I_Block.png')
# 	elif block_types[random_number] == 'J':
# 		block = Block(screen,'./images/J_Block.png')
# 	elif block_types[random_number] == 'L':
# 		block = Block(screen,'./images/L_Block.png')
# 	elif block_types[random_number] == 'S':
# 		block = Block(screen,'./images/S_Block.png')
# 	elif block_types[random_number] == 'Z':
# 		block = Block(screen,'./images/Z_Block.png')
# 	elif block_types[random_number] == 'T':
# 		block = Block(screen,'./images/T_Block.png')
# 	else:
# 		block = Block(screen,'./images/Square.png')

