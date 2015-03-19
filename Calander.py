import pygame, random, sys, os, platform, pickle, time, os.path, shutil, re
from pygame.locals import *
pygame.init()

zoom = 1.3
Info = pygame.display.Info()
WIDTH = int(Info.current_w / zoom)
HEIGHT = int(Info.current_h / zoom)
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#defining functions
def recta(color,X,Y,X2,Y2):
	pygame.draw.rect(screen, color, (X, Y, X2, Y2))

def ScreenText(screen,text="TEXT GOES HERE",X=0,Y=0,color=(0,0,0),size=25,Letter = "monospace"):
    myfont = pygame.font.SysFont(Letter, size, True)
    var = myfont.render(str(text), 25, color)
    screen.blit(var, (X, Y))

#defining classes
class Button:
	def __init__(self):
		self.pressed = False
	def display(self,X,Y,X2,Y2,BColor,MouseX,MouseY,MouseDown):
		recta(BColor,X,Y,X2,Y2)
		if MouseDown:
			if MouseX > X and MouseX < X2:
				if MouseY > Y and MouseY < Y2:
					self.pressed = True
				else:
					self.pressed = False
			else:
				self.pressed = False
		else:
			self.pressed = False

		return(self.pressed)
	def check(self):
		return self.pressed


add = Button()
subtract = Button()
MouseX = 0
MouseY = 0
while True:
	#setting variables in loop
	MouseDown = False

	#action catching stage 1/2
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			MouseDown = True
			MouseX = pygame.mouse.get_pos()[0]
			MouseY = pygame.mouse.get_pos()[1]
		if event.type == QUIT:
			sys.exit()

	#displaying stage 1/2

	add.display(0,0,WIDTH,HEIGHT/4,(50,255,0),MouseX,MouseY,MouseDown)
	subtract.display(0,HEIGHT-HEIGHT/4,WIDTH,HEIGHT,(255,0,0),MouseX,MouseY,MouseDown)

	#checking for button updates:
	if add.check() == True:
		print("click")
	if subtract.check() == True:
		print("click2")

	#action catching stage 2/2


	#displaying stage 2/2

	pygame.display.flip()