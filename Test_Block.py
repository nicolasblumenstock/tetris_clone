import pygame
from pygame.sprite import Sprite


class Test_Block(Sprite):
	def __init__(self,image,screen,start_x,start_y):
		super(Test_Block,self).__init__()
		self.image = pygame.image.load(image)
		self.screen = screen
		self.x = start_x
		self.y = start_y
		self.fall = 25
		self.rect = self.image.get_rect()
		self.rect.bottom = self.y
		self.rect.right = self.x

	def draw_me(self):
		self.screen.blit(self.image, [self.x,self.y])
		# if self.y < 500:
		# 	self.y += self.fall
		# elif self.y > 500:
		# 	self.fall = 0
		# print self.rect

	


