import pygame
import os
pygame.init()
a=1
black=(0,0,0)
white=(255,255,255)
screen=pygame.display.set_mode((700,500))
gameDisplay = pygame.display.set_mode((700,500))
hero=pygame.image.load('hero1.png')
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
print get_image('hero.png')
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
	#pygame.draw.rect(screen_name,color,[x coord. of top left corner,y coord. of top left corner,leght of rect.,height of rect]):draws a rectagle on a screen
	#screen.fill(color):fills the screen with one color
	#pygame.display.flip():shows all made changes
	screen.fill(white)
	screen.blit(hero, (20,20))
	pygame.draw.rect(screen,black,[0,450,700,50],0)
	pygame.display.flip()
