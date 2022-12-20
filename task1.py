# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 00:34:05 2021

@author: Sathish
"""
import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image
from numpy import *
from scipy.ndimage import filters
from PIL import Image, ImageFilter


image = Image.open(r"1.jpg")
#Image Smoothening using gradient and gaussian filter
im=image

plt.figure()
plt.imshow(im, cmap='gray')
plt.title("Input Image")

im2 = filters.gaussian_filter(im,20)
gf=np.gradient(im,2)
plt.figure()
plt.imshow(im2, cmap='gray')
plt.title("smooth Image")


# Sobel derivative filters

image = image.convert("L")
image = image.filter(ImageFilter.FIND_EDGES)

plt.figure()
plt.imshow(image, cmap='gray')
plt.title("Extracted Edge Image")