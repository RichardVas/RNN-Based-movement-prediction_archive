import numpy as np
from sklearn.preprocessing import MinMaxScaler


nums0 = np.array([
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10],
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0],
    [0, 0], [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9], [0, -10],
    [0, 0], [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0], [-10, 0],

    # incremented diff
    [0, 0], [0, 2], [0, 4], [0, 6], [0, 8], [0, 10], [0, 12], [0, 14], [0, 16], [0, 18], [0, 20]

])

nums = np.array([
    # increment in y
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5],
    # increment in x
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0],
    # decrement in y
    [0, 0], [0, -1], [0, -2], [0, -3], [0, -4], [0, -5],
    # decrement in x
    [0, 0], [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0],

    # diagnoally increment
    [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5],
    # diagnoally decrement
    [0, 0], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5],

    # incremented diff
    [0, 0], [0, 2], [0, 4], [0, 6], [0, 8], [0, 10]

])


# arr[[x,y],[x1,y1],[x2,y2]...[xn,yn]]

# print(nums,nums.shape)

# tmp = []
# arr = np.array(tmp)

# arr = np.append(arr,np.array([3,4]))
# arr = arr.reshape(-1,2)

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
    for i in range(0, seq_len*2 + 2,2):
        arr.append((i, 0))

    for i in range(0, seq_len+1,1):
       #print((i*3, 0))
        arr.append((i*3,0))

    return arr


app = np.array(generateSeq(10))
seq_len = 11
#num_batches = 2
input_feature = 2
hello = "qweqweqqweHellohellohello"


if __name__ == "__main__":
    app = np.array(generateSeq(10))

    hello = "Hellohellohello"

    #           (88,2)      88      2
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