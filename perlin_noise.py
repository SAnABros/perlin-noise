import pygame
from random import randint as rand
from time import time
import threading

pygame.init()
WIDTH = 600
HEIGHT = 600
sc= pygame.display.set_mode((WIDTH,HEIGHT))
layer = 20
def Layer(scr, k):
	screen= pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
	for x in range(0, WIDTH//2**k+1):
		for y in range(0, HEIGHT//2**k+1):
			X = x*(2**k)-(2**(k/2)) if x>0 else 0
			Y = y*(2**k)-(2**(k/2)) if y>0 else 0
			W = 2**k if X+2**k<=WIDTH else X-(X+k-WIDTH)
			H = 2**k if Y+2**k<=HEIGHT else Y-(Y+k-HEIGHT)
			if rand(0,100)/100>=0.5:
				pygame.draw.rect(screen, (0,0,0,255/layer+1), [X,Y , W,H])
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
	pygame.display.update()
	print(time()-timing)