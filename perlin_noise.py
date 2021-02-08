import pygame
from random import randint as rand
from time import time
import threading

pygame.init()
WIDTH = 400
HEIGHT = 400
sc= pygame.display.set_mode((WIDTH,HEIGHT))
layer = 10
def Layer(scr, k):
	scale = 0.5
	screen= pygame.Surface((WIDTH*scale, HEIGHT*scale), pygame.SRCALPHA)
	for x in range(0, int(WIDTH*scale*2/(2**k))+1):
		for y in range(0, int(HEIGHT*scale*2/(2**k))+1):
			X = x*(2**k)-(2**(k/2)) if x>0 else 0
			Y = y*(2**k)-(2**(k/2)) if y>0 else 0
			W = 2**k if X+2**k<=WIDTH*scale*2 else X-(X+k-WIDTH*scale*2)
			H = 2**k if Y+2**k<=HEIGHT*scale*2 else Y-(Y+k-HEIGHT*scale*2)
			if rand(0,1)/1>=0.5:
				pygame.draw.rect(screen, (0,0,0), [X,Y , W,H])
	screen.set_alpha((255/layer))
	screen = pygame.transform.smoothscale(screen, (int(WIDTH*scale/5), int(HEIGHT*scale/5)))
	screen = pygame.transform.smoothscale(screen, (WIDTH, HEIGHT))
	scr.blit(screen, (0,0))
while 1:
	timing = time()
	sc.fill((255,255,255))
	for i in range(1,layer+1):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		potok=threading.Thread(target= Layer(sc, i))
		potok.start()
	#pygame.display.update()
	scale = 1 #коэ-нт разрешения цветной карты
	color = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
	for x in range(0,WIDTH,scale):
		for y in range(0,HEIGHT,scale):
			col = sc.get_at((x, y))
			col[0] = 255-col[0]
			square = [x,y , scale,scale]
			if col[0] <= 250 and col[0] >= 200:
				i = rand(150, 170)
				pygame.draw.rect(color, (i,i,i), square)
			elif col[0] >= 100:
				pygame.draw.rect(color, (0,col[0]//1.25, 0), square)
			elif col[0] >= 95:
				pygame.draw.rect(color, (col[0]*2,col[0]*2,0), square)
			else:
				pygame.draw.rect(color, (0,0,col[0]*2), square)
	#color.set_alpha(128) #можно оставить, как коментарий, но можно не оставлять :)
	sc.blit(color, (0, 0)) #можно сделать, как коментарий, тогда будет ЧБ вариант =)
	pygame.display.update()
	print(time()-timing) #время - за которое создался мир
