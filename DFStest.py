import numpy as np

def parse():

    i = 0
    visited = set()
    directions = [[0,1],#fel
                  [1,0],#jobb
                  [1,1],#diag+
                  [0,-1],#le
                  [-1,0],#bal
                  [-1,-1]]#diag-
   # válasszo
    start = [0,0]
    #válasszon egy dir-t, abban az iranyba menjen vegig, vegig er ha 5 egyseg hosszu lesz
    prev = start
   # for i in directions:
    for i in directions:

        for dir in directions:
            tmp = []

            while(len(tmp) != 4):
                start = start[0] + dir[0], start[1]+dir[1]
                tmp.append(start)
            start = prev
            print(tmp)

    #print(visited)


parse()