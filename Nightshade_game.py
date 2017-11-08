import pygame
pygame.init()
a=1
black=(0,0,0)
white=(255,255,255)
screen=pygame.display.set_mode((700,500))
#main event loop:
while a==1:
	b=pygame.mouse.get_pos()
	c=b[0]
	d=b[1]
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			a=2
#font=pygame.font.SysFont('Calibri', 25,1,2)
#text=font.render(('text'),1,black)
#screen.blit(text,[150,100])
	screen.fill(white)
	#pygame.draw.rect(screen_name,color,[x coord. of top left corner,y coord. of top left corner,leght of rect.,height of rect]):draws a rectagle on a screen
	#screen.fill(color):fills the screen with one color
	#pygame.display.flip():shows all made changes
	pygame.draw.rect(screen,black,[0,450,700,50],0)
	pygame.display.flip()
