import math
import numpy as np
from lstm1119 import *

pred = Predictor()

class EuclideanDistTracker:
    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 0

        self.objtoTrack = []
        self.reductionvalue=[]

        #dict that stores obj and their pos based on ids
        self.detectedOBJ = {}

    def printobjs(self):
        with open("output.txt", "a") as f:
            print(self.detectedOBJ, file=f)
            
    
    

    def update(self, objects_rect):
        # Objects boxes and ids
        objects_bbs_ids = []
        unique_ids = []

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 100:
                    self.center_points[id] = (cx, cy)
                    #print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    self.detectedOBJ[id].append([x,y])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                #dic obj
                self.detectedOBJ[self.id_count]=[[x,y]]
                self.id_count += 1
                unique_ids.append(self.id_count)

        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()
        return objects_bbs_ids, unique_ids


    #ismételje meg a pred tensort minden egyedi ID-re a return értékére hívjuk meg a predictor prediction függvényét
    def getpredTensor(self, objects):
        #ahol az id ugyan az, keszitsen egy vector, amivel prediktalhat.
        # a kigyujtott adatok legyenek egy (-1,2) shapeben
     #   object_koords = []
        for obj in objects:
            #if(obj[4] == id):
            self.objtoTrack.append([obj[0],obj[1]])
            if(len(self.objtoTrack)==5):
                #print(self.objtoTrack)
                #print(self.reduction(self.objtoTrack))
                testinp = np.array(self.reduction(self.objtoTrack))
                testinp = testinp.reshape(-1,2)

                pred.predict(testinp)
                return testinp
                # I need x and y 
                #print(obj)
        #print(self.objtoTrack)
        
    #def getdict(self, )

    
    def makePredictiononObj(self):
        #5 koord páronként prediktáljon egyet 
        arrtoreturn = []

        for pairs in self.objtoTrack:
            i = 0
            arrtoreturn.append((pairs[0],pairs[1]))
            #talaltam 5 part
            if(len(arrtoreturn)==5):
               # print(arrtoreturn)
                return arrtoreturn


    def reduction(self,arr):
        tmp =[]
        for i in arr:
            #print(i[0]-arr[0][0])
            #print(i)
            tmp.append([i[0]-arr[0][0],i[1]- arr[0][1]])

        #print(tmp)
        reductionvalue = [arr[0][0],arr[0][1]]
     #   print(reductionvalue)
        return tmp,reductionvalue
            


