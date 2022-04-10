import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
        fig, ax = plt.subplots(nrows=12, ncols=2)
        
        plt.tight_layout()
       # fig, [ax1, ax2] = plt.subplots(len(self.base))
        i= 0
        for row in ax:
            for col in row:
                tmp = np.array(self.base[i])
                tmp = tmp.T
            #fig, [ax1, ax2] = plt.subplots(len(self.base))
                col.scatter(tmp[0],tmp[1])
                col.plot(tmp[0],tmp[1])

      #          tmp2 = np.array(self.base[i+1])
      #          tmp2 = tmp2.T
      #          col.scatter(tmp2[0],tmp2[1])
      #          col.plot(tmp2[0],tmp2[1])
#itt csak simán hozzadaom a prediktált értékekeket
#                col.scatter([69],[69])
#                col.plot([69],[69])

                i+= 1
               # i+= 2
          #  ax2.plot(tmp)
          #  ax3.plot(tmp)
                plt.rcParams['pdf.fonttype'] = 42
                plt.rcParams['font.family'] = 'Calibri'
    # with PdfPages('test.pdf') as pdf:
        #fig.savefig("bruh.pdf",bbox_inches = 'tight')

                pp = PdfPages('foo.pdf')
                pp.savefig(col)
        #      pp.savefig(plot2)
        #      pp.savefig(plot3)
                pp.close()

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
    blaasd = [[10, 20], [20, 30], [40, 50]]
    displayer.addArray(qwe)
    displayer.addArray(asd)
    displayer.addArray(bla)
    displayer.addArray(qwe)
   # displayer.displayGraph()
    displayer.display2()
#fig, axs = plt.subplots()
#fig.suptitle('Vertically stacked subplots')
#axs[0].plot(x, y)
#axs[1].plot(x, -y)