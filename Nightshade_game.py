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
	pygame.draw.rect(screen,black,[0,450,700,50],0)
	pygame.display.flip()
