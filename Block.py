import pygame
from pygame.sprite import Sprite
from random import randint

class Block(Sprite):
	def __init__(self,screen,image):
		super(Block,self).__init__()
		self.image = pygame.image.load(image)
		self.x = 100
		self.y = 25
		self.fall = 25
		self.speed = 25
		self.screen = screen
		self.move_left = False
		self.move_right = False
		self.drop_down = False
		self.turn_left = False
		# self.turn_right = False
		self.rect = self.image.get_rect()
		self.rect.left = self.x
		self.rect.top = self.y

	def movement(self,turn,frame):
		self.screen.blit(self.image,[self.x,self.y])
		if (self.rect.bottom < 500 and frame % 30 == 0):
			self.y += self.fall
			self.rect.top = self.y
			self.rect.left = self.x
		if (self.move_left and self.rect.left > 20):
			self.x -= self.speed
			self.move_left = False
			self.rect.top = self.y
			self.rect.left = self.x
		if (self.move_right and self.rect.right < 250):
			self.x += self.speed
			self.move_right = False
			self.rect.top = self.y
			self.rect.left = self.x
		if (self.turn_left and self.rect.bottom != 500 and self.fall != 0):
			turn += 90
			self.image = pygame.transform.rotate(self.image,turn)
			self.screen.blit(self.image,[self.x,self.y])
			# print self.rect.top, self.rect.bottom, self.rect.right, self.rect.left
			self.rect.bottom = self.y
			self.rect.right = self.x
			self.turn_left = False
		# if (self.turn_right and self.y != 500 and self.fall != 0):
		# 	turn -= 90
		# 	self.image = pygame.transform.rotate(self.image,turn)
		# 	self.screen.blit(self.image,[self.x,self.y])
		# 	self.turn_right = False
		if (self.drop_down and self.rect.bottom < 500):
			self.y += 2 * self.fall
			self.drop_down = False
			self.rect.top = self.y
			self.rect.left = self.x				
		if (self.rect.top >= 500):
			self.speed = 0
			self.fall = 0
			self.rect.top = self.y
			self.rect.left = self.x
		# print self.rect.top, self.rect.bottom, self.rect.right, self.rect.left
		# print self.rect.bottom, self.rect.right

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

	def draw_me(self):
		self.screen.blit(self.image, [self.x,self.y])




