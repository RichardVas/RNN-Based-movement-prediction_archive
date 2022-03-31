import numpy as np
import matplotlib.pyplot as plt
#fig, axs = plt.subplots(2, 2)
#axs[0, 0].plot(x, y)
#axs[0, 0].set_title('Axis [0, 0]')
#axs[0, 1].plot(x, y, 'tab:orange')
#axs[0, 1].set_title('Axis [0, 1]')
#axs[1, 0].plot(x, -y, 'tab:green')
#axs[1, 0].set_title('Axis [1, 0]')
#axs[1, 1].plot(x, -y, 'tab:red')
#axs[1, 1].set_title('Axis [1, 1]')
#
#for ax in axs.flat:
#    ax.set(xlabel='x-label', ylabel='y-label')
#
## Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in axs.flat:
#    ax.label_outer()
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

    def display2(self):
        #feladat: hozzunk letre dinamikusan iterlhato tengelyeket listajat, annyi tengely legyen mint elem a self.baseben
        # ezt egyszerre iteraljuk vegig a self.basel és az aktuális elemet az aktuális tengelyre rakom
        #ez
        fig, [ax1, ax2, ax3] = plt.subplots(len(self.base))
       # fig, [ax1, ax2] = plt.subplots(len(self.base))
        for i in self.base:
            tmp = np.array(i)
            tmp = tmp.T
            #fig, [ax1, ax2] = plt.subplots(len(self.base))
            ax1.plot(tmp)
          #  ax2.plot(tmp)
          #  ax3.plot(tmp)
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

    qwe = [[1,2],[2,3],[4,5]]
    asd = [[4,5],[5,3],[9,5]]
    bla = [[10, 20], [20, 30], [40, 50]]
    displayer.addArray(qwe)
    displayer.addArray(asd)
    displayer.addArray(bla)
   # displayer.displayGraph()
    displayer.display2()
#fig, axs = plt.subplots()
#fig.suptitle('Vertically stacked subplots')
#axs[0].plot(x, y)
#axs[1].plot(x, -y)