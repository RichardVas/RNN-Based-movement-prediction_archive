import numpy as np
from sklearn.preprocessing import MinMaxScaler
from grapher import *


# generate dataset from 0 koord
def generateSeq(seq_len):
    arr = []
    # vizszintes jobbra
    for i in range(0, seq_len + 1):
        arr.append((i, 0))
    # vizszintes balra
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, 0))
    # fuggoleges felfelé
    for i in range(0, seq_len + 1):
        arr.append((0, i))
    # fuggoleges lefele
    for i in range(0, -seq_len - 1, -1):
        arr.append((0, i))

    # diganoally +,+
    for i in range(0, seq_len + 1):
        arr.append((i, i))

    # diagonally -,-
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, i))

    # diagnoally +,-
    for i in range(0, seq_len + 1):
        arr.append((i, -i))

    # diagonally -,+
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, -i))
#incremented
#    for i in range(0, seq_len*2 + 2,2):
#        arr.append((i, 0))

#    for i in range(0, seq_len+1,1):
       #print((i*3, 0))
#        arr.append((i*3,0))

##### /2 bracket
    #diagonally -,+ / 2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, -i/2))

    #diagonally -,+ / 2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i/2, -i))

    # diganoally +,+ /2
    for i in range(0, seq_len + 1):
        arr.append((i, i/2))
        # diganoally +,+
    for i in range(0, seq_len + 1):
        arr.append((i/2, i))


        # diagonally -,- /2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, i/2))
        # diagonally -,- /2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i/2, i))

    # diagnoally +,-
    for i in range(0, seq_len + 1):
        arr.append((i, -i/2))
        # diagnoally +,-
    for i in range(0, seq_len + 1):
        arr.append((i/2, -i))

    return arr





app = generateSeq(20)
#print(app)


app = np.array(app)
seq_len = 21
#num_batches = 2
input_feature = 2
#print(app)



if __name__ == "__main__":
    app = np.array(generateSeq(15))
    viz = Grapher()
    viz.addArray(app)
    viz.displayGraph()

    #           (198,2)      198      2
    print(app, app.shape, len(app),len(app[0]))
    scaler = MinMaxScaler()

    dataset = scaler.fit_transform(app)
    dataset = dataset.reshape(-1, seq_len*input_feature)
    print(dataset)
 #   er = scaler.inverse_transform(dataset.data.view(-1, 2))

    inp = dataset[:, :-2]
    print('inp', inp)
    tar = dataset[:, 2:]
    print('tar',tar)
  #  print(er)