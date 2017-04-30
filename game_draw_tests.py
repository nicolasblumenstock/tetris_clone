# ** -- IMPORTS -- **
import pygame
import sys

# ** -- INITIALIZE PYGAME -- **
pygame.init()

# ** -- VARIABLES -- **
frame = 0
screen_size = (400, 600)
background_color = (255, 255, 255)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("dear god please work")
game_on = True
turn = 0

class Draw_Test(object):
	def __init__(self,screen):
		self.x = 25
		self.y = 25
		self.fall = 25
		self.color = (120,108,245)
		# self.pointlist = pointlist
		self.pointlist = (((self.x,self.y),((self.x + 75),self.y),((self.x + 75),(self.y + 25)),((self.x + 50),(self.y + 25)),((self.x + 50),(self.y + 50)),((self.x + 25),(self.y + 50)),((self.x + 25),(self.y + 25)),(self.x,(self.y + 25))))
		self.screen = screen

	def draw_block(self):
		# pygame.draw.polygon(self.screen,self.color,self.pointlist)
		if (self.y > 500):
			self.y += self.fall
			pygame.draw.polygon(self.screen,self.color,self.pointlist)

	def draw_update(self):
		self.y += self.fall


pointlist_T = (((0,0),(75,0),(75,25),(50,25),(50,50),(25,50),(25,25),(0,25)))
point_color = (120,108,245)	

while game_on:
	frame += 1
	screen.fill(background_color)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	block = Draw_Test(screen)
	# block.draw_update()
	block.draw_block()



		# elif pygame.KEYDOWN:
		# 	if event.key == K_UP:
		# 		draw_block.should_move('clockwise',True)
		# 	elif event.key == K_LEFT:
		# 		draw_block.should_move('left',True)
		# 	elif event.key == K_DOWN:
		# 		draw_block.should_move('down',True)
		# 	elif event.key == K_RIGHT:
		# 		draw_block.should_move('right',True)
		# elif pygame.KEYUP:
		# 	if event.key == K_UP:
		# 		draw_block.should_move('clockwise',False)
		# 	elif event.key == K_LEFT:
		# 		draw_block.should_move('left',False)
		# 	elif event.key == K_DOWN:
		# 		draw_block.should_move('down',False)
		# 	elif event.key == K_RIGHT:
				# draw_block.should_move('right',False)
	pygame.display.flip()