import pygame
from pygame.sprite import Sprite

class Block(Sprite):
	def __init__(self,screen,image):
		super(Block,self).__init__()
		self.image = pygame.image.load(image)
		self.x = 250
		self.y = 20
		self.fall = 1
		self.speed = 10
		self.screen = screen
		self.move_left = False
		self.move_right = False
		self.drop_down = False
		self.turn_left = False
		self.turn_right = False
		self.rect = self.image.get_rect()
		self.rect.top = self.x
		self.rect.left = self.y

	def movement(self,turn):
		self.screen.blit(self.image,[self.x,self.y])
		if self.y < 500:
			self.y += self.fall
		if (self.move_left and self.x > 100):
			self.x -= self.speed

		if (self.move_right and self.x < 400):
			self.x += self.speed

		if (self.turn_left and self.y != 500 and self.fall != 0):
			turn += 90
			self.image = pygame.transform.rotate(self.image,turn)
			self.screen.blit(self.image,[self.x,self.y])
			self.turn_left = False
		if (self.turn_right and self.y != 500 and self.fall != 0):
			turn -= 90
			self.image = pygame.transform.rotate(self.image,turn)
			self.screen.blit(self.image,[self.x,self.y])
			self.turn_right = False
		if (self.drop_down and self.y < 500):
			self.y += 2 * self.fall
		if (self.y == 500):
			self.speed = 0
			self.fall = 0
		self.rect.top = self.y
		self.rect.left = self.x

	def should_move(self,direction,true_or_false):
		if direction == 'left':
			self.move_left = true_or_false
		elif direction == 'right':
			self.move_right = true_or_false
		elif direction == 'drop_down':
			self.drop_down = true_or_false
		if direction == 'turn_left':
			self.turn_left = true_or_false
		elif direction == 'turn_right':
			self.turn_right = true_or_false





