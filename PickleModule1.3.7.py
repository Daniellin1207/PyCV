from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters,measurements,morphology
# from scipy.misc import imsave
import scipy.misc

# im_gray=array(Image.open('timg.jpg').convert('L'))
# gray()
# #灰度图的高斯模糊
# im2=filters.gaussian_filter(im_gray,5)

# im=array(Image.open('timg.jpg'))
# #彩色三通道的高斯模糊
# im2=zeros(im.shape)
# for i in range(3):
#     im2[:,:,i]=filters.gaussian_filter(im[:,:,i],5)
# im2=uint8(im2)


im_gray=array(Image.open('Material\\timg.jpg').convert('L'))
gray()

#sobel算子计算边界
imx=zeros(im_gray.shape)
filters.sobel(im_gray,1,imx)
imy=zeros(im_gray.shape)
filters.sobel(im_gray,0,imy)
magnitude=sqrt(imx**2+imy**2)

# #高斯模糊
# sigma=5
# imx=zeros(im_gray.shape)
# filters.gaussian_filter(im_gray,(sigma,sigma),(0,1),imx)
# imy=zeros(im_gray.shape)
# filters.gaussian_filter(im_gray,(sigma,sigma),(1,0),imy)

# im_gray=(1*(im_gray>200))
# labels,nbr_objects=measurements.label(im_gray)
# print("Number of bojects:",nbr_objects)
#
# imshow(imx)
# figure(2)
# imshow(imy)
# figure(3)

# lena1=scipy.misc.ascent()#调用scipy.misc中自带图片
# gray()
# imshow(lena1)
# show()

sobel=[1,0,-1]
lena1=-np.convolve([0,1,2,3], sobel, mode='same')
print(lena1)

