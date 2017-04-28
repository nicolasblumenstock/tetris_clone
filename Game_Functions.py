import pygame
import sys

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
