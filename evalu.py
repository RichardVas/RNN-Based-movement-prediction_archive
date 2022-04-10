from Pred import *

# programresz, ahol kiertekelem a predikciot eredmenyet

def perdiff2(num1, num2):
    diff = abs(num1-num2)

 #   if(diff == 0 ):
 #       return 100
    avg = abs((num1+num2)/2)

    return 100-(diff/avg)*100

def perdiff(inp,out):
    diff = abs(inp)-abs(out)
    #szalekos kulombseget ugy szamolok, hogy a vett kulombseget megnehezem hany szalaeke a viszonyított erteknek ami itt inp

    return((diff/inp)*100)



test1 = np.array([
    [0, 0],
    [-1, 0],
    [-2, 0],
    [-3, 0],
    [-4, 0]
])

test2 = np.array([
    [0, 0],
    [0, 2],
    [0, 4],
    [0, 6],
    [0, 8],
    [0, 10],
    [0,12],
    [0,14],
    [0,16],
    [0,18],
])

test3 = np.array([
    [0, 0],
    [-1, -1],
    [-2, -2],
    [-3, -3],
    [-4, -4],
    [-5, -5],
    [-6, -6],
    [-7, -7]
])

test4 = np.array([
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
    [8, 8],
    [9, 9],
    [10, 10],
])

test5 = np.array([
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7],
    [0, 8],
    [0, 9],
    [0, 10],


])

test6 = np.array([
    [0, 0],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-2, -2]
])

test7 = np.array([
    [-0, 0],
    [-1, 1],
    [-2, 2],
    [-3, 3],
    [-3, 4],
    [-3, 5],
    [-3, 6],
    [-3,7],
])

test8 = np.array([
    [0, 0],
    [2, 1],
    [4, 2],
    [6, 3],
    [8,4],
    [10,5],
    [12,6],
])

test9 = [
    [30,0],
    [50,0],
    [90,0],
    [90,0],
    [150,0],
    [180,0],
    [210,0],
    [240,0],
]

test11 = [
    [10,10],
    [20,20],
    [30,30],
    [40,40],
    [50,50],


]

#diffper(100,90)

test10 = [[21.350006103515625, 41.19883728027344],
[23.6851806640625, 46.36952209472656],
[26.6875, 52.70780944824219],
[29.022674560546875, 56.71092224121094],
[29.35626220703125, 61.21446228027344],
[33.025787353515625, 66.71873474121094],
[37.362518310546875, 72.22303771972656],
[40.698455810546875, 78.22773742675781],
[44.368011474609375, 86.23399353027344],
[48.371124267578125, 93.57304382324219]
]

test12 = [
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


evaluationset = [test1,test2, test3, test4, test5, test6, test7, test8, test9,test10,test11,test12]
evaluation_model = Predictor()
vis = Grapher()
for i in evaluationset:
    start = time()
    out = evaluation_model.predict4(i)
    ##print(out)
   # print(out[0],i[-1][0])
    end = time()
    print(i)
   # print('tar',i[-1])
    print('out',out)
   # vis.addArray([i[-1],out])
  #  print('Accuracy in %','X:',perdiff(out[0],i[-1][0]),'Y:',perdiff(out[1],i[-1][1]),'in: ',end-start,' sec')
  #  print('-----------')
#vis.displayGraph()

    vis.addArray(i)
   # print(test10)
    #pro = evaluation_model.predict4(test10)
    #print('pro',pro)
    vis.addArray(i)
  #  vis.addArray(out)
vis.display2()

#print(perdiff(23,24))
