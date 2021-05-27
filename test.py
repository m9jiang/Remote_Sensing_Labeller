# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

import scipy.io as scio

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# args = vars(ap.parse_args())
# image = cv2.imread(args["image"])
# segments = slic(img_as_float(image), n_segments = 100, sigma = 5)
# # show the output of SLIC
# fig = plt.figure("Superpixels")
# ax = fig.add_subplot(1, 1, 1)
# ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments))
# plt.axis("off")
# plt.show()
# # loop over the unique segment values
# for (i, segVal) in enumerate(np.unique(segments)):
# 	# construct a mask for the segment
# 	print "[x] inspecting segment %d" % (i)
# 	mask = np.zeros(image.shape[:2], dtype = "uint8")
# 	mask[segments == segVal] = 255
# 	# show the masked region
# 	cv2.imshow("Mask", mask)
# 	cv2.imshow("Applied", cv2.bitwise_and(image, image, mask = mask))
# 	cv2.waitKey(0)

# IRGS = scio.loadmat('IRGS.mat')['IRGS']
# img = cv2.imread('imagery_HH4_by_4average.tif')
# alpha_back = np.ones((img.shape[0], img.shape[1]), dtype=np.uint8)*255
# # image = np.zeros(img.shape + (4,), dtype=np.uint8)
# img = np.dstack([img, alpha_back])
# image = np.zeros(img.shape, dtype=np.uint8)
# i, j = np.where(IRGS == 3524)
# image[i, j, :] = (0, 255, 255, 255)
# cv2.namedWindow('img', cv2.WINDOW_NORMAL) 
# cv2.resizeWindow('img',500, 500)
# cv2.namedWindow('image', cv2.WINDOW_NORMAL) 
# cv2.resizeWindow('image',500, 500)
# cv2.imshow('img',img)
# cv2.imshow('image',image)

# i, j = np.where(image[:,:,3] == 255)
# img[i, j, :] = image[i, j, :]

# cv2.namedWindow('res', cv2.WINDOW_NORMAL) 
# cv2.resizeWindow('res',500, 500)
# cv2.imshow('res',img)
# cv2.waitKey(0)


# import tkinter as tk
# from tkinter import messagebox

# top = tk.Tk()

# def helloCallBack():
#    messagebox.showinfo( "Hello Python", "Hello World")

# A = tk.Button(top, text ="A", command = helloCallBack)
# B = tk.Button(top, text ="Hello", command = helloCallBack)
# A.pack()
# B.pack()
# top.mainloop()

from tkinter import *
def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

widget = Button(None, text='Mouse Clicks')
B = Button(None, text='B Clicks')
B.pack()
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
widget.mainloop()