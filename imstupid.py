import random
x = 10
w = 20
y = 10
h = 20         
         
cx = (x + w) / 2 
cy = (y + h) / 2
 
h = 2* cy - y

print(cx,cy)
print('h',h)

def calcDisplacement(actx,acty,pred):
    x1 = actx
    y1 = acty
    x2,y2 = pred
    dx = x2-x1
    dy = y2-y1
    return dx,dy

currx = 10
curry = 10
pred = [12,12]
out = calcDisplacement(currx,curry,pred)
print(out[0],out[1])

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

print(random_color)