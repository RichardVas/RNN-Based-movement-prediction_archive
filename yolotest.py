import torch
import cv2
import pandas as pd
from tracker import *
from time import time
from Pred import *

import random
from PDFrame import *



class VideoProcessor():
  def __init__(self):
    self.video_source = 'rosszut.mp4'
    self.yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)
    self.tracker = EuclideanDistTracker()
    self.cap = cv2.VideoCapture(self.video_source)
    self.datatable = DataTable()
   # self.wer = cv2.TrackerCSRT_create()

   # self.io = cv2.legacy.TrackMOOSE_create()

  def random_color(self):
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    return [a,b,c]
  def DisplayDetectedOBJs(self,frame,detectedOBJs):
        for object in detectedOBJs:
      # x,y,w,h,id = box_id
          x = int(object[0])
          y = int(object[1])
          w = int(object[2]-object[0])
          h = int(object[3]-object[1])
          id = object[4]
          a,b,c = self.random_color()
          cv2.putText(frame,str(id),(x,y-15),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

  def DisplayPredictedOBJs(self,frame,preddict):

    for obj in preddict:
      key = obj
      n,m = preddict[obj]

      cv2.putText(frame,str(key),(n-5,m-5),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
      #cv2.circle(frame,(actx,acty), radius=10, color=(0, 0, 255), thickness=4)
      cv2.rectangle(frame,(n,m),(n+50,m+50),(0,0,255),2)

  def calcDisplacement(self,actx,acty,predx,predy):
      x1 = actx
      y1 = acty
      x2 = predx
      y2 = predy
      dx = x2-x1
      dy = y2-y1
      return dx,dy



# legyen egy prediktáló függvény, ami végig megy a detektált objektumokon és adja vissza az egyes objektumok jövőbeli helyzetét.
  def CreatePredictions(self,frame,frame_counter, detectedOBJs,preddict):

            #start of prediction loop
       # preddict = {}
        #if(frame_counter%3 == 0):
          for key in detectedOBJs:
              #eloszor nézzük meg minden ID-hez tartozó 2d tömböket
             # print(key,detectedOBJs[key])
              tmp = []
              for i in detectedOBJs[key]:
            #      print(i)
                  #cx,cy = self.tracker.calCenterPoint(i[0],i[1],i[2],i[3])
                  #tmp.append([cx,cy])
                  #print(i)
                
                  tmp.append([i[0],i[1]])
               #   print('i',i)
              #ilyenkor azért prediktál pontosan egyszer mert ha egyszer beölti a6 5öt, akkor prediktál és soha többet nem lesz öt
              #minden 5. elem utan prediktaljon 1et
              
              #csak azokon az idkon menjen végig, amik a képen is megjelennek
              #if(len(tmp)% 5 == 0 and key in tracker.center_points):
              
              if(len(tmp)>=10 and key in self.tracker.center_points):
                 # print(tmp)
                 # preddict = {}
                  latest5 = tmp[-10:]
          #       print(key,'latest5',latest5)

                  

                  
                  actx = latest5[-1][0]
                  acty= latest5[-1][1]
            #      print(actx,acty)
                  testinp = np.array(latest5)
                  #itt kúródik el 
                  testinp = testinp.reshape(-1,2)
                  actual = pred.predict4(testinp)
                  
                  n,m = actual
                  n = pred.roundToInt(n) 
                  m = pred.roundToInt(m)

                  dx,dy = self.calcDisplacement(actx,acty,n,m)

            #      print(dx,dy)

                  o,p =self.tracker.center_points[key]
                  # el van cseszve, mert a prediktálás előtti középpontot használja, el kell tólni az o,p-t annyival
                  # mint az n,m változott az x,y tól
                  corner_x = 2* o - n + dx*2
                  corner_y = 2* p - m  + dy*2
                  #print('latest10',latest5,'pred',n,m)
             #     preddict[key] = [n,m]
                  #print('pred',key,preddict[key])
                  predCenter_x, predCenter_y = self.tracker.calCenterPoint(n,m,corner_x,corner_y)
                  cv2.putText(frame,str(key),(n-5,m-5),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
                  cv2.circle(frame,(int(predCenter_x),int(predCenter_y)), radius=5, color=(0, 0, 255), thickness=2)
                  cv2.rectangle(frame,(n,m),(pred.roundToInt(corner_x),pred.roundToInt(corner_y)),(0,0,255),2)
                  cv2.line(frame,(int(o),int(p)),(int(predCenter_x),int(predCenter_y)),(0,0,255),2) 

            #  else:
            #    preddict[key] = [0,0]

  def MainLoop(self):

    ids = []
    frame_counter = 0
    pred_dict = {}
    while True:
        
        start = time()

        ret, frame = self.cap.read()
        frame_counter += 1
       
        #cv2.imshow("Frames",frame) 
        results = self.yolo_model(frame)
        objects_detected = []
        #cv2.imshow('YOLO',results.render())
        df = pd.DataFrame(results.pandas().xyxy[0])
        

        for index, row in df.iterrows():
            #megadja a bal felso sarkat és a jobb alsó sarkat
            # X - Y - W - H
            # cx = (x - w)/2
            objects_detected.append([row['xmin'],row['ymin'], row['xmax'], row['ymax']])
      

        boxes_ids,id_set = self.tracker.update(objects_detected)
      #  print(boxes_ids)
      #  print('#',id_set)
        ids.append(id_set)
      #  print('q',ids)
      #  for id in ids:
      #      print(id)


        OBJs = self.tracker.detectedOBJ

        
        self.DisplayDetectedOBJs(frame,boxes_ids)
        self.CreatePredictions(frame,frame_counter,OBJs,pred_dict)
       # self.DisplayPredictedOBJs(frame,pred_dict)

        end = time()
        #display FPS
        cv2.putText(frame,'FPS: {}'.format(round(1/(end-start))),(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        cv2.imshow("Frames",frame)
        key = cv2.waitKey(1)
        if key == 27: 
            self.tracker.printobjs()
            #self.datatable.exportPKL('test0313_01.pkl')
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
  main = VideoProcessor()
  main.MainLoop()