"""
@author:Daniel
@file: range conversion.py
@time: 2018/12/02
"""

import cv2
import numpy as np

# p=np.zeros((100,100))
# p[40:60,40:60]=255

im=cv2.imread('test.jpg',0)
# im=im if
# print(im)
# print(im)

cv2.threshold(im, 140, 1, 0, im)
# cv2.imshow('im1',im)
# cv2.waitKey(0)
im2=np.zeros((100,100))
im3=np.zeros((100,100))
for i in range(1,100):
    for j in range(1,100):
        print(im[i-1][j],im[i][j-1])
        if im[i-1][j]!=0 and im[i][j-1]!=0:
            im2[i,j]=min(im[i-1,j],im[i,j-1])+1
for i in range(98,-1,-1):
    for j in range(98,-1,-1):
        if im[i +1, j] and im[i, j + 1]:
            im3[i, j] = min(im[i + 1, j], im[i, j + 1]) + 1

for i in range( 100):
    for j in range( 100):
        im[i, j] = min(im2[i, j], im3[i, j ])
        print(im[i,j])
cv2.imshow('img',im)
cv2.waitKey(0)
        # t=[]
        # if im[i-1,j]!=0:
        #     t.append(im[i-1,j])
        # if im[i,j-1]!=0:
        #     t.append(im[i,j-1])
        # if len(t)==0:
        #     im2[i,j]=0
        # else:
        #     im2[i,j]=min(t)+1
        # im[i,j]=min(im[i-1,j],im[i,j-1])+1
        # im[i,j]=



# im=cv2.imread()