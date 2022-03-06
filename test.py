 # vizszintes jobbra*2
import torch
import math
import random

#let it be the default rounding method
def round_up(x):
    return int(x + math.copysign(0.5, x))



def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def lol(seq_len):
    arr =[]
    for i in range(0, seq_len,1):
        print((i*3, 0))
        arr.append([i*3,0])
    print(arr,len(arr))

def lol2(seq_len):
    arr =[]
    for i in range(0, seq_len,1):
        print((i*i, 0))
        arr.append([i*i,0])
    print(arr,len(arr))

#mertani
def mertani(seq_len):
    step = 1
    for i in range(0,seq_len+1,step):
        print((i*i),0)
        step = i*i

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def kerek(double):
    print('with copysign',round_up(double))
    print('with truncate',truncate(double))
    print('with math',normal_round(double))
    print('with round',round(double,0))
#lol(10)
kerek(10.5)
#lol2(10)
mertani(10)

from itertools import accumulate
from operator import mul
length = 6
ratio = 2

progression=(list(accumulate([ratio]*length, mul)))
progression.insert(0,0)
bla = torch.rand(1,2,3)
print(bla)
#prog = torch.DoubleTensor(bla)

print(progression)
#print(prog)
arr =[]
print(random.uniform(1.5, 1.9))
for i in range(0,5):
    curr = random.uniform(1.5, 1.9)
    print(curr)
    arr.append(curr)
docten = torch.DoubleTensor(arr)
print(docten)

qwe = []

print(len(qwe))