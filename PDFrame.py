import pandas as pd
import pickle
#from yolotest import *


#if __name__ == "__main__":

class DataTable():
    def __init__(self):
        self.df = pd.DataFrame(columns = ['ObjectID','Obj_track','Pred_value'])
        self.df = self.df.append({'ObjectID':1, 'Obj_track':[1,1,1]},ignore_index=True)
        self.df = self.df.append({'ObjectID':2, 'Obj_track':[1,1,1]},ignore_index=True)
        self.ex_name = "backup.pkl"
        pass

    def exportPKL(self,name = None):
        if name != None:
            self.df.to_pickle(name)
        else:
            self.df.to_pickle(self.ex_name)

    def importPKL(self,name = None):
        if name != None:
            self.df = pd.read_pickle(name)
        else:
            self.df = pd.read_pickle(self.ex_name)

    def dispalyDF(self):
        print(self.df.to_string())


    def costum(self):
       tmp =  self.df.query('ObjectID == 2')
       print(tmp)

    def query(self):
        try:
            while True:
                QueryString = input ()
                tmp = self.df.query(QueryString)
                print(tmp)
        except KeyboardInterrupt:
            pass
   



if __name__ == "__main__":
    df = DataTable()
#    df.exportPKL()
    df.importPKL("backup.pkl")
    df.dispalyDF()
    df.query()
   # df.costum()