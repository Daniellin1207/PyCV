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

    H=dot(linalg.inv(C2),dot(H,C1))

    return H/H[2,2]

def Haffine_from_points(fp,tp):


points = array([[1, 2, 3, 4], [2, 3, 4, 5]])
U, S, V = linalg.svd(points)
# print('U',U) #A.T*A
# print('S',S) #sqrt(特征值)
print('V',V) #A*A.T
print(points.shape)
m = mean(points, axis=0)
print(m)
print(diag([1, 2, 3]))
