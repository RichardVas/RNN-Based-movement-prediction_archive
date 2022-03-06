import numpy as np
import matplotlib.pyplot as plt

class Grapher():
    def __init__(self):
#        super(Grapher, self).__init__()
        #todo
        #given an 2d array
        #convert ot np array
        #transpose
        #scatter then plot, finally show the whole
#        pass
        self.base=[]
#        self.fig, self.axs = plt.subplots()
        self.dictGroup={}
    def addArray(self,arr):
        self.base.append(arr)

    def displayGraph(self):
        #parse the base of arrays and for each elemnt export the plts
        for i in self.base:
            tmp = np.array(i)
            tmp = tmp.T
            plt.scatter(tmp[0],tmp[1])

            plt.plot(tmp[0],tmp[1])
        #plt.legend(['Plot 1', 'Plot 2'])        
        plt.show()

    def addDict(self,key,value):
        self.dictGroup[key] = value

    def displayFromDict(self):
        arrOfLegends = []
        for i in self.dictGroup:
            tmp = np.array(self.dictGroup[i])
            tmp = tmp.T
            plt.scatter(tmp[0],tmp[1])
            plt.plot(tmp[0],tmp[1])
            arrOfLegends.append(i)
        plt.legend(arrOfLegends)
        plt.show()

    


if __name__ == "__main__":
    displayer = Grapher()

#fig, axs = plt.subplots()
#fig.suptitle('Vertically stacked subplots')
#axs[0].plot(x, y)
#axs[1].plot(x, -y)