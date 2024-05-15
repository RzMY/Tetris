GAME_ROW = 17
GAME_COL = 10

class BlockType:
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    PURPLE = 5
    BLOCKMAX = 6
    
BLOCK_RES = {
    BlockType.RED: 'Python/pic/red.png',
    BlockType.ORANGE: 'Python/pic/orange.png',
    BlockType.YELLOW: 'Python/pic/yellow.png',
    BlockType.GREEN: 'Python/pic/green.png',
    BlockType.BLUE: 'Python/pic/blue.png',
    BlockType.PURPLE: 'Python/pic/purple.png'
}

BLOCK_SHAPE = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # 方形
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # 长条
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # z字形
    [(0, 1), (0, 2), (1, 0), (1, 1)],  # 反z字形
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # 山形
    [(0, 1), (1, 0), (1, 1), (1, 2)],  # 7字形
    [(0, 0), (1, 0), (1, 1), (1, 2)]   # 反7字形
]