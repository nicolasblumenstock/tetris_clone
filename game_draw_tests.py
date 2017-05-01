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
		self.move_left = False
		self.move_right = False
		self.drop_down = False
		self.rotate = False

	def buttons(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif (event.type == pygame.KEYDOWN):
				if event.key == pygame.K_LEFT:
					self.should_move('left', True)
				elif (event.key == pygame.K_RIGHT):
					self.should_move('right', True)
				elif (event.key == pygame.K_DOWN):
					self.should_move('drop_down', True)
				elif (event.key == pygame.K_UP):
					self.should_move('turn_left', True)
				# elif event.key == 101:
				# 	self.should_move('turn_right', True)
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.should_move('left', False)
				if event.key == pygame.K_RIGHT:
					self.should_move('right', False)
				if event.key == pygame.K_DOWN:
					self.should_move('drop_down', False)
				if event.key == pygame.K_UP:
					self.should_move('turn_left', False)

	def should_move(self,direction,true_or_false):
		if direction == 'left':
			self.move_left = true_or_false
		elif direction == 'right':
			self.move_right = true_or_false
		elif direction == 'drop_down':
			self.drop_down = true_or_false
		if direction == 'turn_left':
			self.rotate = true_or_false

	def draw_block(self):
		if (self.move_left and self.x > 0 and self.x < 250):
			self.x += 25
		elif (self.move_right and self.x > 0 and self.x < 250):
			self.x -= 25
		if (self.y > 0  and self.y < 500):
			self.y += self.fall
		if (self.drop_down and self.y > 0 and self.y < 500):
			self.y += 2 * self.fall
		pygame.draw.polygon(self.screen,self.color,self.pointlist)




# pointlist_T = (((0,0),(75,0),(75,25),(50,25),(50,50),(25,50),(25,25),(0,25)))
# point_color = (120,108,245)
while game_on:
	frame += 1
	screen.fill(background_color)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	block = Draw_Test(screen)
	block.buttons()
	block.draw_block()







	pygame.display.update()