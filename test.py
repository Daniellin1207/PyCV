"""
@author:Daniel
@file: test.py
@time: 2018/11/26
"""

from PIL import Image
from pylab import array,imshow,ginput,show,figure,gray
pil_im_path = "Material/timg.jpg"

# def test5():
#     im=array(Image.open(pil_im_path).convert('L'))
#     gray()
#     figure()
#     print(im.min(),im.max())
#     imshow(im)
#     im1=255-im
#     figure()
#     print(im1.min(),im1.max())
#     imshow(im1)
#     im2=(100.0/255)*im+100
#     figure()
#     print(im2.min(),im2.max())
#     imshow(im2)
#     im3=255.0*(im/255.0)**2
#     figure()
#     print(im3.min(),im3.max())
#     imshow(im3)
#     show()
# test5()
# if __name__ == '__main__':
#     pil_im_path = "Material/timg.jpg"
#     test5()

# def test4(): # 交互式标注
#     im=array(Image.open(pil_im_path))
#     imshow(im)
#     print("输入三个点: ")
#     x=ginput(3)
#     print(x)
    # show()
# test4()

# def test3():
#     im=Image.open(pil_im_path)
#     imshow(im)
#     im=im.convert('L')
#     im=array(im)
#     figure()
#     gray()
#     contour(im,origin='image')
#     axis('equal')
#     axis('off')
#     figure()
#     hist(im.flatten(),128)
#
#     show()
# test3()
# def test2():
#     im = array(Image.open(pil_im_path))
#     imshow(im)
#     x=[100,100,400,400]
#     y=[200,500,200,500]
#     plot(x,y,'r*')
#     plot(x[:2],y[:2])
#     axis('off')
#     title('Plotting:"lena.jpg')
#     show()
# test2()

# def test1():
#     # a=get_imlist("Material")
#     pil_im=Image.open(pil_im_path)
#     box=(100,100,400,400)
#     region=pil_im.crop(box)
#     # region=region.transpose(Image.ROTATE_180)
#     region=region.rotate(180)
#     pil_im.paste(region,box)
#     # pil_im.thumbnail((128,128))
#     pil_im.show()
