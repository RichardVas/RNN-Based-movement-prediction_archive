import torch
import cv2
import pandas as pd
from tracker import *
from time import time
from lstm1119 import *

from PDFrame import *

#df.append({'ObjectID':1, 'Obj_track':[1,1,1]},ignore_index=True)
# Model
model = torch.hub.load('RichardVas/yolov5', 'yolov5s', pretrained=True)


tracker = EuclideanDistTracker()
#pred_model = Predictor()

# Images
#imgs = 'C:\Users\Richárd\Desktop\latest_vers\cars.jpg'  # batch of images
#cap = cv2.VideoCapture('NY.mp4')
cap = cv2.VideoCapture('campus.mp4')
#ret, frame = cap.read()

#results.xyxy[0]  # img1 predictions (tensor)
#print(results.pandas().xyxy[0])  # img1 predictions (pandas)
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie

ids = []
while True:

    start = time()

    ret, frame = cap.read()

    #cv2.imshow("Frames",frame) 
    results = model(frame)
    objects_detected = []
    #cv2.imshow('YOLO',results.render())
    df = pd.DataFrame(results.pandas().xyxy[0])
  #  print(df)
    #print(df['xmin'].tolist())
  #  print(df[['xmin','ymin','xmax','ymax']])
    for index, row in df.iterrows():
        objects_detected.append([row['xmin'],row['ymin'], row['xmax'], row['ymax']])
   
   # objects_detected.append(df[['xmin','ymin','xmax','ymax']].iloc().values.tolist())
   # print(objects_detected)

 #   for object in objects_detected:
       #print(object[0])
 #       x = int(object[0])
 #       y= int(object[1])
 #       w = int(object[2]-object[0])
 #       h = int(object[3]-object[1])
 #       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        

    

    boxes_ids,id_set = tracker.update(objects_detected)
  #  print(boxes_ids)
  #  print('#',id_set)
    ids.append(id_set)
  #  print('q',ids)
  #  for id in ids:
  #      print(id)

    OBJs = tracker.detectedOBJ
    for key in OBJs:
        #eloszor nézzük meg minden ID-hez tartozó 2d tömböket
    #    print(key,OBJs[key])
        tmp = []
        for i in OBJs[key]:
      #      print(i)
            tmp.append(i)
        #ilyenkor azért prediktál pontosan egyszer mert ha egyszer beölti a6 5öt, akkor prediktál és soha többet nem lesz öt
        #minden 5. elem utan prediktaljon 1et
        
        #csak azokon az idkon menjen végig, amik a képen is megjelennek
        #if(len(tmp)% 5 == 0 and key in tracker.center_points):
        if(len(tmp)>=5 and key in tracker.center_points):
            tombb,reductionv = tracker.reduction(tmp)
        #    print(reductionv)
            rv1 = reductionv[0]
            rv2 = reductionv[1]
            rv1 = int(rv1)
            rv2 = int(rv2)

            latest5 = tombb[-5:]
            print(key,'latest5',latest5)

            testinp = np.array(latest5)
            testinp = testinp.reshape(-1,2)
            actual = pred.predict(testinp)
            print(key,'next',actual)
            n,m = actual
            n = int(n) 
            m = int(m) 
            actx,acty = tmp[-1]
       #     print(actx,acty)
            actx = int(actx)
            acty = int(acty)
            cv2.putText(frame,str(key),(actx+n,acty+n-15),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
            cv2.rectangle(frame,(actx+n,acty+m),(actx+n+50,acty+m+50),(0,0,255),4)
      #      print('prediction here',actual)

         #   if(len(OBJs[key])):
         #       print('here')
        #cv2.rectangle()




    for object in boxes_ids:
       # x,y,w,h,id = box_id
        x = int(object[0])
        y= int(object[1])
        w = int(object[2]-object[0])
        h = int(object[3]-object[1])
        id = object[4]
       # print(box_id)
        cv2.putText(frame,str(id),(x,y-15),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    #    if(id == 10):
    #        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
  #      if(n is not 0 and id == 9): 
  #          cv2.rectangle(frame,(x+n,y+m),(x+w,y+h),(0,0,255),5)
           #  print('red',n+x,m+y)




       
    #tracker.makePredictiononObj() 
 #   if(n is not 0):                 
 #       cv2.rectangle(frame,(n,m),(n+w,m+h),(0,0,255),3)

    end = time()
    #display FPS
    cv2.putText(frame,'FPS: {}'.format(round(1/(end-start))),(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
    cv2.imshow("Frames",frame)
    key = cv2.waitKey(0)
    if key == 27: 
        tracker.printobjs()
        break

cv2.destroyAllWindows()