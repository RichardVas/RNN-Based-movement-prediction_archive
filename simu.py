import pygame
import sys

from Pred import *

BLACK = (0, 0, 0)
blockSize = 20 #Set the size of the grid block
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1000

#20 x 20 as palya

snake = [(0,0), (0,1), (1,1), (1,2), (1,3)]

head = [4,4]

resetP = [4,4]

#if(len(resetP)==0):
#    resetP.append(head)

movement = [[0,0]]
#movement.append((0,0))

def foretell(pred_modul):
    if(len(movement)%5==0):
        next= pred_modul.predict(movement[-5:])
        print('PREDIKTALAS',next)
        
        #print('last',last)
        drawCell(next[0]+resetP[0],next[1]+resetP[1])
        print(resetP)
        #start = movement[-1]
        last = movement[-1]
        resetP[0]+=last[0]
        resetP[1]+=last[1]
       # resetP.append(movement[-1])
       # print(resetP)
        movement.clear()
        movement.append([0,0])

    

def main():
    #starting point bugot megfixálni
    #amikor prediktálás történik, mentse el az aktuális keződ pontot külön.
    sp=head
    print(sp)
    #reset_point

    global SCREEN, CLOCK

    pred_modul = Predictor()

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()            
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print("Down")
                    dir = [0,1]
                    tmp = movement[-1]
                    tmp = tmp[0]+dir[0],tmp[1]+dir[1]
                    head[1] = head[1]+1
                    drawHead()
                    movement.append(tmp)
                    print(movement)
                    foretell(pred_modul)


                if event.key == pygame.K_UP:
                    print("Up")
                    dir = [0,-1]
                    tmp = movement[-1]
                    tmp = tmp[0]+dir[0],tmp[1]+dir[1]
                    head[1] = head[1]-1
                    drawHead()
                    movement.append(tmp)
                    print(movement)
                    foretell(pred_modul)

                if event.key == pygame.K_LEFT:
                    print("Left")
                    dir = [-1,0]
                    tmp = movement[-1]
                    tmp = tmp[0]+dir[0],tmp[1]+dir[1]
                    head[0] = head[0]-1
                    drawHead()
                    movement.append(tmp)
                    print(movement)
                    foretell(pred_modul)

                if event.key == pygame.K_RIGHT:
                    print("Right")
                    dir = [1,0]
                    tmp = movement[-1]
                    tmp = tmp[0]+dir[0],tmp[1]+dir[1]
                    head[0] = head[0]+1
                    drawHead()
                    movement.append(tmp)
                    print(movement)
                    foretell(pred_modul)









                  #  rect = pygame.Rect(head[0]*blockSize,head[1]*blockSize, blockSize, blockSize)
                  #  pygame.draw.rect(SCREEN, (255,0,255), rect,1)

           # if event.key == pygame.K_LEFT:
           # if event.key == pygame.K_RIGHT:


        pygame.display.update()

def drawCell(pX,pY):
    rect = pygame.Rect(pX*blockSize,pY*blockSize, blockSize, blockSize)
    #draw rect faszság: Képernyő, szín, forma, kitöltés vagy nem
    pygame.draw.rect(SCREEN, (0,255,0), rect,0)  

def drawHead():

    rect = pygame.Rect(head[0]*blockSize,head[1]*blockSize, blockSize, blockSize)
    #draw rect faszság: Képernyő, szín, forma, kitöltés vagy nem
    pygame.draw.rect(SCREEN, (255,0,255), rect,0)


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
    drawHead()


if __name__ == "__main__":
    main()