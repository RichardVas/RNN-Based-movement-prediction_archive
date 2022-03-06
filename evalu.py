from lstm1119 import *

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
    #   [0,12],
    #   [0,14]
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
    [3,0],
    [5,0],
    [9,0],
    [9,0],
    [15,0],
    [18,0],
    [21,0],
    [24,0],
]

#diffper(100,90)


evaluationset = [test1,test2, test3, test4, test5, test6, test7, test8, test9]
evaluation_model = Predictor()
for i in evaluationset:
    start = time()
    out = evaluation_model.predict(i[:-1])
    ##print(out)
   # print(out[0],i[-1][0])
    end = time()
    print('tar',i[-1])
    print('out',out)
    print('Accuracy in %','X:',perdiff(out[0],i[-1][0]),'Y:',perdiff(out[1],i[-1][1]),'in: ',end-start,' sec')
    print('-----------')


#print(perdiff(23,24))
