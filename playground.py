from time import time
from datetime import *
from grapher import *
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from testcases import *
from Pred import *


import cv2

timestr = datetime.now().strftime("%Y%m%d_%H%M%S")
#print(timestr)

vir = Grapher()

tracker = cv2.TrackerKCF_create()

#for i in di:
#    if(len(di[i])>=5):
#        vir.addArray(di[i])
#    print (i,di[i])
#vir.displayGraph()
virr = Grapher()


prediction_modul = Predictor()
input_v = [
    [1000,0],
    [2000,0],
    [3000,0],
    [4000,0],
    [5000,0],
    [6000,0],
    [7000,0],
    [8000,0],
    [9000,0],
    [10000,0],


]


start = time()
predicted = prediction_modul.predict4(input_v)
end = time()
print(end-start)
print(input_v)
print(predicted)
