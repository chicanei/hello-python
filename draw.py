import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype ='uint8')
cv.imshow('Blank',blank)


'''
#Reading Images:

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
'''

#1 paint the image a certain color
blank[200:300,300:400] = 0,255,255  #在畫板上畫方塊
#blank[:] = 0,255,0
#blank[:] = 0,0,255 會出現紅色的畫板

cv.imshow('Green',blank)

cv.waitKey(0)