from numpy import *
from numpy import random
from scipy.ndimage import filters
from scipy.misc import imsave#用于图像保存
import rof
import cv2

im =zeros((500,500))

im[100:400,100:400]=128
im[200:300,200:300]=255
imsave('Material\origin.pdf',im)
im=im+30*random.standard_normal((500,500))

U,T=rof.denoise(im,im)
G=filters.gaussian_filter(im,10)

imsave('Material\synth_rof.pdf',U)
imsave('Material\synth_gaussian.pdf',G)

m=[[3,2,1],[0,5,2],[8,8,8]]
print(m)
k=roll(m,1,0)#中间为+时，将最后的数放到最前
print(k)
hh=linalg.norm([3,4,5])#求取范数
print(hh)