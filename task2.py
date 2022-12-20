# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 00:47:37 2021

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
plt.figure()
plt.imshow(img, cmap='gray')
plt.title("Input Image")

noisy = img + 0.4 * img.std() * np.random.random(img.shape)
# # adding salt and peper noise to the image 
# # adding salt
num_salt = np.ceil(0.05 * img.size * 0.5)
coords = [np.random.randint(0, i - 1, int(num_salt))
                 for i in img.shape]
out=img
out[coords] = 255

num_pepper = np.ceil(0.05* img.size * (1. - 0.05))
coords = [np.random.randint(0, i - 1, int(num_pepper))
                   for i in img.shape]
out[coords] = 0
out=out.reshape(img.shape)

plt.figure()
plt.imshow(out, cmap='gray')
plt.title("salt and peper noise image")

from skimage import filters
from skimage import restoration

gaussian_filter_out = filters.gaussian(out, sigma=2)
med_filter_out = filters.median(out,np.ones((3, 3)))



# salt-and-pepper noise can
# be applied only to greyscale images
# Reading the color image in greyscale image
plt.figure()
plt.imshow(gaussian_filter_out, cmap='gray')
plt.title("Gaussian filter")
plt.figure()
plt.imshow(med_filter_out,cmap='gray')
plt.title("Median filter")
plt.figure()
plt.imshow(out, cmap='gray')
plt.title("Denoised Image")