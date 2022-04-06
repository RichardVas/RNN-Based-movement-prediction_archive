import torch.optim
from os.path import exists

from LSTM import *
from dataset import *
# from torch.utils.tensorboard import SummaryWriter
import math
from time import time

from testcases import *

import matplotlib.pyplot as plt

from grapher import *


def roundToInt(x):
    return int(x + math.copysign(0.5, x))

# PATH = 'lstm1029.pth'


class Predictor():
    def __init__(self):
        super(Predictor, self).__init__()
        self.model = LSTM(2, 6, 1).to(dev)
        self.scaler = MinMaxScaler()
        self.dataset = self.scaler.fit_transform(app)
        self.dataset = self.dataset.reshape(-1, seq_len*input_feature)
        
        
        self.PATH = 'lstm1105.pth'
        self.load_model = exists(self.PATH)



        if (self.load_model):
            self.model.load_state_dict(torch.load(self.PATH))
            self.model.eval()

        self.input_tensor = np.array([])
        self.target_tensor = np.array([])
    def train(self):
        if (self.load_model is False):
            n_batches = 10
            seq_len = 10
            input_feature = 2

            losses = []
            # writer = SummaryWriter()
            torch.manual_seed(1)
            inp = np.array(self.dataset[:, :-2]).astype(np.float32)
            print('inp', inp)
            tar = np.array(self.dataset[:, 2:]).astype(np.float32)
            # shape: number of sequences, seqence length, input feature
            self.input_tensor = torch.from_numpy(inp).reshape(n_batches, seq_len, input_feature).to(dev)

            print(self.input_tensor, self.input_tensor.shape)
            self.target_tensor = torch.from_numpy(tar).reshape(n_batches, seq_len, input_feature).to(dev)
            print(self.target_tensor, self.target_tensor.shape)

            optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
            # loss = nn.MSELoss()
            loss = nn.MSELoss()
            epoch = 2101
            self.model.train()
            for i in range(epoch):

                optimizer.zero_grad()
                x = self.model.forward(self.input_tensor)

                single_loss = loss(x, self.target_tensor)
                # print('x',x)
                # print(target_tensor)
                losses.append(single_loss)

                if (i % 100 == 0):
                    print('epoch: ', i, 'loss:', single_loss)

                # print('x',x.shape)
                # print('tar',target_tensor.shape)
                # writer.add_scalar("Loss/Train", single_loss, i)
                # backward, hogy "visszafejti "
                single_loss.backward()
                optimizer.step()
                
            torch.save(self.model.state_dict(), self.PATH)
        else:
            print('Model is already trained!')

  #      plt.plot(losses)
  #      plt.legend()
  #      plt.show()

    def predict(self, input_vector):
        self.model.eval()

        input_vector = self.scaler.transform(input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
            er = self.scaler.inverse_transform(result.cpu().data.view(-1, 2))

           # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
           # print(toreturn)
            return er[-1]
           # return toreturn

    def validation(self):
        #try out how accure the predictions are
        inp = test3[:-1]
        val = test3[-1]
        res = self.predict(inp)

        viz = Grapher()
        viz.addArray(inp)
        viz.addArray(test3)
        viz.addArray(res)
        viz.displayGraph()
        pass



if __name__ == "__main__":
    plwork = Predictor()
    # Predictor.dataloader()
    plwork.train()

    plwork.predict(test1)
    plwork.predict(test2)
    plwork.predict(test3)
    plwork.predict(test4)

    start = time()
    plwork.predict(test5)
    end = time()
    print('time to predict:', (end - start))
    plwork.predict(test6)
    plwork.predict(test7)
    plwork.predict(test8)
    print(' ')
    bruh=np.array(plwork.predict(test9))
    print(hello)

    plwork.validation()


#data = np.array(test9)
#data = data.reshape(-1,2)
#x, y = data.T
#plt.scatter(x,y)
#plt.plot(x,y)
#bx,by = bruh.T

#plt.scatter(bx,by)
#plt.plot(bx,by)
#plt.show()