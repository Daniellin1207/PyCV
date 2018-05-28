# encoding=UTF-8
# @Author: Daniel
# @Date: 2018/5/28 0028 下午 8:46
# @Name: Function.py
# @IDE: PyCharm Community Edition


from numpy import *
from pylab import *

plot()
pos = ginput(3)  # ginput(n)取n个点的坐标，需要在pylab的plot()函数之后才可以运行
m = array(pos).T
# vstack()函数中还需要一个括号包裹几个叠加的矩阵
# ones()函数中还需要一个括号包裹几个叠加的矩阵
print(vstack((m, ones((1, m.shape[1])))))
