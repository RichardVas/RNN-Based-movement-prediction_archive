import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('oriaskerek_vonat_rendszer.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb,interpolation='nearest')
plt.show()
#plt.savefig('opencvaxes.jpg')