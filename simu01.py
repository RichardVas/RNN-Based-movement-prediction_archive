import pygame
import sys

from Pred import *


class Board():

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.blockSize = 20 #Set the size of the grid block
        self.WHITE = (200, 200, 200)
        self.WINDOW_HEIGHT = 400
        self.WINDOW_WIDTH = 400
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    def drawHead(self,head):

        rect = pygame.Rect(head[0]*self.blockSize,head[1]*self.blockSize, self.blockSize, self.blockSize)
        #draw rect faszság: Képernyő, szín, forma, kitöltés vagy nem
        pygame.draw.rect(self.SCREEN, (255,0,255), rect,0)


    def drawGrid(self):
        #Board.blockSize = 20 #Set the size of the grid block
        for x in range(0, self.WINDOW_WIDTH, self.blockSize):
            for y in range(0, self.WINDOW_HEIGHT, self.blockSize):
                rect = pygame.Rect(x, y, self.blockSize,self. blockSize)
                pygame.draw.rect(self.SCREEN, self.WHITE, rect, 1)
        
            self.drawHead([3,3])


if __name__ == "__main__":
    Field = Board()
    ##while(True):
    while True:
        Field.drawGrid()            
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()