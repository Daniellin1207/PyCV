"""
@author:Daniel
@file: imtools.py.py
@time: 2018/11/26
"""

import os
from PIL import Image
from pylab import *

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
def imresize(im,sz):
    pil_im=Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))
