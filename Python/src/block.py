import pygame
import sys
from pygame.locals import *
from const import *

class Block(pygame.sprite.Sprite):
    def __init__(self, blockType, rowIdx, colId, width, height, relPos):
        super().__init__()
        self.blockType = blockType
        self.rowIdx = rowIdx
        self.colId = colId
        self.width = width
        self.height = height
        self.relPos = relPos
        self.loadImage()
        self.updateImagePos()
    
    def loadImage(self):
        self.image = pygame.image.load(BLOCK_RES[self.blockType])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    def updateImagePos(self):
        self.rect = self.image.get_rect()
        self.rect.left = self.relPos[0] + self.width * self.colId
        self.rect.top = self.relPos[1] + self.height * self.rowIdx
    
    def drop(self):
        self.rowIdx += 1
        self.updateImagePos()
    
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-1, 0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(1, 0)
        elif pressed[K_UP]:
            self.rect.move_ip(0, -1)
        elif pressed[K_DOWN]:
            self.rect.move_ip(0, 1)
            
    def draw(self, surface):
        self.updateImagePos()
        surface.blit(self.image, self.rect)