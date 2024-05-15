import random
import pygame
import sys
from pygame.locals import *
from const import *
from block import *

class BlockGroup(object):
    def GenerateBlockGroupConfig(rowIdx, colIdx):
        idx = random.randint(0, len(BLOCK_SHAPE) - 1)
        bType = random.randint(0, BlockType.BLOCKMAX - 1)
        configList = []
        for x in range(len(BLOCK_SHAPE[idx])):
            config = {
                'blockType': bType,
                'rowIdx': rowIdx + BLOCK_SHAPE[idx][x][0],
                'colIdx': colIdx + BLOCK_SHAPE[idx][x][1]
            }
            configList.append(config)
        return configList
    
    def __init__(self, width, height, blockGroupConfig, relPos):
        super().__init__()
        self.time = 0
        self.blocks = []
        for config in blockGroupConfig:
            self.blocks.append(Block(config['blockType'], config['rowIdx'], config['colIdx'], width, height, relPos))
    
    def update(self):
        self.time += 1
        if self.time >= 1000:
            self.time = 0
            for block in self.blocks:
                block.drop()
    
    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface)