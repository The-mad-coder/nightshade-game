import pygame
import os
pygame.init()
a=1
black=(0,0,0)
white=(255,255,255)
screen=pygame.display.set_mode((700,500))
gameDisplay = pygame.display.set_mode((700,500))
hero=pygame.image.load('hero.png')
_image_library = {}
hero_coords=[20,275]
left=0
right=0
#main event loop:
while a==1:
	b=pygame.mouse.get_pos()
	c=b[0]
	d=b[1]
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			a=2
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				left=1
			if event.key==pygame.K_RIGHT:
				right=1
		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				left=0
			if event.key==pygame.K_RIGHT:
				right=0
#font=pygame.font.SysFont('Calibri', 25,1,2)
#text=font.render(('text'),1,black)
#screen.blit(text,[150,100])
	#pygame.draw.rect(screen_name,color,[x coord. of top left corner,y coord. of top left corner,leght of rect.,height of rect]):draws a rectagle on a screen
	#screen.fill(color):fills the screen with one color
	#pygame.display.flip():shows all made changes
	if left==1:
		hero_coords[0]-=1
	if right==1:
		hero_coords[0]+=1
	screen.fill(white)
	screen.blit(hero, (hero_coords[0],hero_coords[1]))
	pygame.draw.rect(screen,black,[0,450,700,50],0)
	pygame.display.flip()
