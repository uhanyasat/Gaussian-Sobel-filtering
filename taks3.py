# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 01:04:38 2021

@author: Sathish
"""

import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image
from numpy import *
from scipy.ndimage import filters
from scipy import ndimage

img = imageio.imread('1.jpg',as_gray=True)
img_45 = ndimage.rotate(img, 45, reshape=True)
plt.figure()
plt.imshow(img_45, cmap='gray')
plt.title("Rotated Image")


im2 = filters.gaussian_filter(img_45,20)
plt.figure()
plt.imshow(im2, cmap='gray')
plt.title("Blurred Gaussian Image")

im=img_45
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = np.hypot(dx, dy)  # magnitude
mag *= 255.0 / np.max(mag) 
print(mag)