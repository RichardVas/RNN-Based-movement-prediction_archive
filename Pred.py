import torch.optim
from os.path import exists

from LSTM import *
from dataset import *
# from torch.utils.tensorboard import SummaryWriter
import math
from time import strftime, time
from datetime import datetime



import matplotlib.pyplot as plt




# PATH = 'lstm1029.pth'


class Predictor():
    def __init__(self):
        super(Predictor, self).__init__()
        self.model = LSTM(2, 16, 1).to(dev)
        self.scaler = MinMaxScaler()
        self.dataset = self.scaler.fit_transform(app)
        #  self.dataset = app
        self.dataset = self.dataset.reshape(-1, seq_len * input_feature)

        self.PATH = '20220411_1104443steps.pth'

        # self.PATH = '20220403_15574610steps.pth'
        # self.PATH = '20220402_1923425steps.pth'
        self.load_model = exists(self.PATH)

        if (self.load_model):
            self.model.load_state_dict(torch.load(self.PATH))
            self.model.eval()

        self.input_tensor = np.array([])
        self.target_tensor = np.array([])

    def train(self):
        if (self.load_model is False):
            # mennyi absztrakciot tanuljon meg
            n_batches = 17  # len(app)/ seq_len
            # milyen hosszu egy absztakció
            seq_len = 11
            # mennyi valtozója van egy koordnak
            input_feature = 2

            losses = []
            # writer = SummaryWriter()
            torch.manual_seed(1)
            inp = np.array(self.dataset[:, :-6]).astype(np.float32)
            print('inp', inp)
            tar = np.array(self.dataset[:, 6:]).astype(np.float32)
            # shape: number of sequences, seqence length, input feature
            self.input_tensor = torch.from_numpy(inp).reshape(n_batches, seq_len, input_feature).to(dev)

            print(self.input_tensor, self.input_tensor.shape)
            self.target_tensor = torch.from_numpy(tar).reshape(n_batches, seq_len, input_feature).to(dev)
            print(self.target_tensor, self.target_tensor.shape)

            optimizer = torch.optim.Adam(self.model.parameters(), lr=0.01)
            # loss = nn.MSELoss()
            loss = nn.MSELoss()
            epoch = 2501
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

            # torch.save(self.model.state_dict(), self.PATH)
            timestr = datetime.now().strftime("%Y%m%d_%H%M%S")
            torch.save(self.model.state_dict(), timestr + self.PATH)


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
            inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
            er = self.scaler.inverse_transform(result.cpu().data.view(-1, 2))

            # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
            # print(toreturn)
            return er[-1]
        # return toreturn

    def predict2(self, input_vector):
        self.model.eval()

        scalerr = MinMaxScaler()
        scalerr.fit(input_vector)
        input_vector = self.scaler.transform(input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
            er = scalerr.inverse_transform(result.cpu().data.view(-1, 2))

            # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
            # print(toreturn)
            return er[-1]
        # return toreturn

    def predict3(self, input_vector):
        self.model.eval()

        scalerr = MinMaxScaler()

        scalerr.fit(input_vector)
        input_vector = scalerr.transform(input_vector)

        print('inputvector', input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
            print('result', result)
            er = scalerr.inverse_transform(result.cpu().data.view(-1, 2))

            # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
            # print(toreturn)
            return er[-1]
        # return toreturn

    def predict4(self, input_vector):
        self.model.eval()

        scalerr = MinMaxScaler(feature_range=(0, 10))

        scalerr.fit(input_vector)
        input_vector = scalerr.transform(input_vector)
        input_vector = self.scaler.transform(input_vector)

        # print('inputvector',input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
            #    print('result',result)
            er = self.scaler.inverse_transform(result.cpu().data.view(-1, 2))

            er = scalerr.inverse_transform(er)

            # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
            # print(toreturn)

            # return er[-3:]
            return er[-1]
        # return toreturn



    def roundToInt(self, x):
        return int(x + math.copysign(0.5, x))


if __name__ == "__main__":
    plwork = Predictor()
    # Predictor.dataloader()
    plwork.train()

    print(' ')
    # bruh=np.array(plwork.predict(test9))

    qwe123 = np.array([
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
    exp_test = [[(1.3)**i,0] for i in range(13)]
    print(exp_test)
    print(plwork.predict4(exp_test[:10]))
