import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 1000))
Image = pygame.image.load('pic/yellow.png')
Rect = Image.get_rect()
Rect.center = (300, 500)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(Image, Rect)
    pygame.display.update()