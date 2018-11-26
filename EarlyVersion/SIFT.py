from numpy import *
from matplotlib import pyplot
# list=array([[1,1],[2,3],[4,5]]).T
# print(list)
# print([m[1] for m in list],[m[0] for m in list])


from scipy.ndimage import filters
from scipy.ndimage import filters, measurements, morphology
from PIL import Image
from pylab import *

def compute_harris_response(im, sigma=1):
    imx = zeros(im.shape)
    # filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)
    figure(1)
    gray()
    imshow(im)#原图
    print(im)
    ll=filters.sobel(im) #原图sobel
    print(ll)
    figure(2)
    gray()
    imshow(ll)
    imy = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)#原图模糊
    figure(3)
    gray()
    imshow(imy)
    print(imy)
    figure(4)
    lk=filters.sobel(imy)#原图模糊sobel
    imshow(lk)
    gray()
    Wxx = filters.gaussian_filter(imx * imx, sigma)
    Wxy = filters.gaussian_filter(imx * imy, sigma)
    Wyy = filters.gaussian_filter(imy * imy, sigma)

    Wdet = Wxx * Wyy - Wxy ** 2
    Wtr = Wxx + Wyy
    # imshow(Wdet)
    # show()
    return Wdet / Wtr

im1 = array(Image.open('Material\\lena.jpg').convert('L'))
# im2 = array(Image.open('Material\\lena1.jpg').convert('L'))
#
# wid = 5

# harrisim = compute_harris_response(im1, 5)
# filtered_coords1 = get_harris_points(harrisim, wid + 1)
# d1 = get_descriptors(im1, filtered_coords1, wid)

# harrisim = compute_harris_response(im2, 5)
# filtered_coords2 = get_harris_points(harrisim, wid + 1)
# d2 = get_descriptors(im2, filtered_coords2, wid)

# print('starting matching')
# matches = match_twosided(d1, d2)

# gray()
# plot_matches(im1, im2, filtered_coords1, filtered_coords2, matches[:100])
# show()

#
# im_gray = array(Image.open('Material\\lena.jpg').convert('L'))
# harrisim = compute_harris_response(im_gray)
# filtered_coords=get_harris_points(harrisim,6)
# plot_harris_points(im_gray,filtered_coords)

