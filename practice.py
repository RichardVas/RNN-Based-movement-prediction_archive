from LSTM import *
from lstm1119 import *
from grapher import *

import numpy as np



series = np.sin(0.1*np.arange(1000))
#plt.plot(series)
#plt.show()
for i in series:
    print (i)