import random
import pygame
import sys
from pygame.locals import *
from block import *
from const import *
from blockGroup import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 1000))

blockGroups = []
for x in range(GAME_ROW):
    conf = BlockGroup.GenerateBlockGroupConfig(x*4, x)
    blockGroups.append(BlockGroup(40, 40, conf, (0, 0)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    for bg in blockGroups:
        bg.update()
    
    DISPLAYSURF.fill((0,0,0))
    
    for bg in blockGroups:
        bg.draw(DISPLAYSURF)
    
    pygame.display.update()