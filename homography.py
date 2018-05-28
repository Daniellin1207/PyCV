# encoding=UTF-8
# @Author: Daniel
# @Date: 2018/5/28 0028 下午 3:12
# @Name: homography.py.py
# @IDE: PyCharm Community Edition

from numpy import *


def normalize(points):
    for row in points:
        row /= points[-1]
    return points


def make_homog(points):
    return vstack(points, ones(1, points, shape[1]))


def H_from_points(fp, tp):
    #图像变换求解8未知数H矩阵
    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')

    m = mean(fp[:2], axis=1)
    maxstd = max(std(fp[:2], axis=1)) + 1e-9
    C1 = diag([1 / maxstd, 1 / maxstd, 1])
    C1[0][2] = -m[0] / maxstd
    C1[1][2] = -m[1] / maxstd
    fp = dot(C1, fp)

    m = mean(tp[:2], axis=1)
    maxstd = max(std(tp[:2], axis=1)) + 1e-9
    C2 = diag([1 / maxstd, 1 / maxstd, 1])
    C2[0][2] = -m[0] / maxstd
    C2[1][2] = -m[1] / maxstd
    tp = dot(C2, tp)

    nbr_correspondences = fp.shape[1]
    A = zeros((2 * nbr_correspondences, 9))
    for i in range(nbr_correspondences):
        A[2 * i] = [-fp[0][i], -fp[1][i], -1, 0, 0, 0, tp[0][i] * fp[0][i], tp[0][i] * fp[1][i], tp[0][i]]
        A[2 * i + 1] = [0, 0, 0, -fp[0][i], -fp[1][i], -1, tp[1][i] * fp[0][i], tp[1][i] * fp[1][i], tp[1][i]]
    U, S, V = linalg.svd(A)
    H = V[8].reshape((3, 3))

    H = dot(linalg.inv(C2), dot(H, C1))

    return H / H[2, 2]


def Haffine_from_points(fp, tp):
    #仿射变换求解H矩阵6未知数
    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')
    m = mean(fp[:2], axis=1)
    maxstd = max(std(fp[:2], axis=1)) + 1e-9
    C1 = diag([1 / maxstd, 1 / maxstd, 1])
    C1[0][2] = -m[0] / maxstd
    C1[1][2] = -m[1] / maxstd
    fp_cond = dot(C1, fp)

    m = mean(tp[:2], axis=1)
    C2 = C1.copy()
    C2[0][2] = -m[0] / maxstd
    C2[1][2] = -m[1] / maxstd
    tp_cond = dot(C2, tp)

    A = concatenate((fp_cond[:2], tp_cond[:2]), axis=0)
    U, S, V = linalg.svd(A.T)

    tmp = V[:2].T
    B = tmp[:2]
    C = tmp[2:4]

    tmp2 = concatenate((dot(C, linalg.pinv(B)), zeros((2, 1))), axis=1)
    H = vstack((tmp2, [0, 0, 1]))

    H = dot(linalg.inv(C2), dot(H, C1))

    return H / H[2, 2]

from PIL import Image
from scipy import ndimage
from pylab import *

'''
ndimage.affine_transform函数进行图像的仿射变换

# im1=Image.open('Material/lena.jpg')
im = array(Image.open('Material/lena.jpg'))
H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
im2 = ndimage.affine_transform(im, H[:2, :2], (H[0,2], H[0, 2]))   #H[0,2]代表H矩阵第0行第2列元素的值，先纵向，后横向
figure()
gray()
imshow(im2)
show()
'''

'''
测试svd奇异值分解的USV分别对应

points = array([[1, 2, 3, 4], [2, 3, 4, 5]])
U, S, V = linalg.svd(points)

# print('U',U) #A.T*A
# print('S',S) #sqrt(特征值)
# print('V', V)  # A*A.T

print(points.shape)
m = mean(points, axis=0)
print(m)
print(diag([1, 2, 3]))

'''

def image_in_image(im1,im2):
    m,n=im1.shape[:2]
    fp=array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])

    #从图像上点击四点获取tp
    imshow(im2)
    tp=ginput(4)
    tp = vstack((array(tp).T[::-1], ones((1, array(tp).shape[0]))))

    H=Haffine_from_points(tp,fp)
    im1_t=ndimage.affine_transform(im1,H[:2,:2],(H[0,2],H[1,2]),im2.shape[:2])
    alpha=(im1_t>0)

    return (1-alpha)*im2+alpha*im1_t

im1=array(Image.open('Material/lena.jpg').convert('L'))
im2=array(Image.open('Material/timg.jpg').convert('L'))
gray()
im3=image_in_image(im1,im2)

figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()