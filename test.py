"""
@author:Daniel
@file: test.py
@time: 2018/11/26
"""

from PIL import Image
from pylab import *
pil_im_path = "Material/timg.jpg"

a=np.array([[[1,1],[1,1]],[[1,2],[1,2]]])
b=np.array([[1,0],[1,0]])
print(np.multiply(a,b))



def hist():
    im=array(Image.open(pil_im_path).convert('L'))
    figure(1)
    imshow(Image.fromarray(im))
    print(im.shape)
    dic={i:0 for i in range(256)}
    for i in im.flatten():
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    for k in dic.keys():
        dic[k]=dic[k]/len(im.flatten())
    sorted(dic.items(),key=lambda x:x[0])
    figure(2)
    plot(dic.keys(),dic.values())
    # show()
    return dic
# hist()
def cdf():
    dic=hist()
    y=[]
    sum=0
    for k in dic.keys():
        sum+=dic[k]
        y.append(sum)
    return dic,y
    # plot([i for i in range(256)],y)
    # show()
# cdf()
def hist_ave():
    im=array(Image.open(pil_im_path).convert('L'))
    dic,y=cdf()
    for i in range(1200):
        for j in range(1920):
            im[i,j]=im[i,j]*y[im[i,j]]

    figure(3)
    dic = {i: 0 for i in range(256)}
    for i in im.flatten():
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    for k in dic.keys():
        dic[k] = dic[k] / len(im.flatten())
    sorted(dic.items(), key=lambda x: x[0])
    plot(dic.keys(), dic.values())

    figure(4)
    imshow(Image.fromarray(im))
    show()

# hist_ave()


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
