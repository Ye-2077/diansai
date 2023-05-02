import cv2
import numpy as np
import matplotlib.pyplot as plt

from imgProcessing import cv2show, addNoise, gaussian_blur


#addNoise(0.5,0.04,img1,"data\\noisy_img.png")

#img1 = cv2.imread('data\\1.png')


img_test = cv2.imread('data\\test.png')
img2 = gaussian_blur(img_test)

cv2show('img_test',img_test)
cv2show('img2', img2)





