import cv2
from skimage.segmentation import mark_boundaries
import numpy as np
import scipy.io as scio
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
# import matplotlib.pyplot as plt
from skimage.util import img_as_float
# import sys

root = tk.Tk()
root.withdraw()
# if cancel 
folder_path = filedialog.askdirectory(title='Please select a directory containing HH/HV and segmentation results')
root.destroy()

if folder_path == '':
    print("No directory selected!!!")
    exit()
# folder_path = ""
IRGS_path =  folder_path + "/IRGS.mat"
img_path = folder_path + "/imagery_HH4_by_4average.tif"

IRGS = scio.loadmat(IRGS_path)['IRGS']
img = cv2.imread(img_path)
# IRGS = scio.loadmat('IRGS.mat')['IRGS']
# img = cv2.imread('imagery_HH4_by_4average.tif')
# 5 is unknown label
labeled_img_grey = np.ones((img.shape[0], img.shape[1]), dtype=np.uint8)*5
label_temp = 0
display_mode = True # True is showing polygons

img_boundary = mark_boundaries(img_as_float(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), IRGS, color=(140, 180, 210))
# alpha_back = np.ones((img.shape[0], img.shape[1]), dtype=np.uint8)*255
# labeled_img_BGR = np.dstack([img_boundary, alpha_back])
# labeled_img_BGR = img_boundary.copy()
labeled_img_BGR = img.copy()

def save_result():
    # asksaveasfile
    # while True:
    #     root = tk.Tk()
    #     folder_save_path = filedialog.askdirectory(title='Please select a directory to save the labeling results')
    #     if folder_save_path == '':
    #         print("No directory selected!!!")
    #         root.destroy()
    #         continue
    #     cv2.imwrite(folder_save_path+'/labeled_img_RGB.png', labeled_img_BGR)
    #     cv2.imwrite(folder_save_path+'/labeled_img_grey.png', labeled_img_grey)
    #     root.destroy()
    #     break
    root = tk.Tk()
    folder_save_path = filedialog.askdirectory(title='Please select a directory to save the labeling results')
    cv2.imwrite(folder_save_path+'/labeled_img_RGB.png', labeled_img_BGR)
    cv2.imwrite(folder_save_path+'/labeled_img_grey.png', labeled_img_grey)
    messagebox.showinfo(title='Successful!', message='Labeling results have been saved!')
    root.destroy()
    # confirmation

def labelChoose():
    global label_temp

    def label_OW():
        global label_temp
        label_temp = 0
        win.destroy()

    def label_NI():
        global label_temp
        label_temp = 1
        win.destroy()

    def label_YI():
        global label_temp
        label_temp = 2
        win.destroy()

    def label_FYI():
        global label_temp
        label_temp = 3
        win.destroy()

    def label_MYI():
        global label_temp
        label_temp = 4
        win.destroy()
    def label_Unknow():
        global label_temp
        label_temp = 5
        win.destroy()
        

    win = tk.Tk()
    button0 = tk.Button(win, text="Open Water", fg = "white", bg="blue", width=10, padx=10, command=label_OW)
    button0.pack()
    button1 = tk.Button(win, text="New Ice", bg="lightpink", width=10, padx=10, command=label_NI)
    button1.pack()
    button2 = tk.Button(win, text="Yong Ice", bg="purple", width=10, padx=10, command=label_YI)
    button2.pack()
    button3 = tk.Button(win, text="First-year Ice", bg="yellow", width=10, padx=10, command=label_FYI)
    button3.pack()
    button4 = tk.Button(win, text="Multi-year Ice", bg="red", width=10, padx=10, command=label_MYI)
    button4.pack()
    button5 = tk.Button(win, text="Unknown", width=10, padx=10, command=label_Unknow)
    button5.pack()
    win.mainloop()
    return label_temp


def mousePoints(event, x, y, flags, params):
    global labeled_img_BGR, labeled_img_grey, label_temp
    if event == cv2.EVENT_LBUTTONDBLCLK:
        segVal = IRGS[y][x]
        i, j = np.where(IRGS == segVal)
        label = labelChoose()
        # mask = np.zeros(img.shape[:2], dtype = "uint8")
        # mask[i,j] = 255
        # cv2.imshow("Applied", cv2.bitwise_and(img, img, mask = mask))
        # cv2.waitKey(0)
        if label == 0:
            labeled_img_BGR[i, j, :] = (255, 200, 150)
            labeled_img_grey[i, j] = 0
        elif label == 1:
            labeled_img_BGR[i, j, :] = (193, 182, 255)
            labeled_img_grey[i, j] = 1
        elif label == 2:
            labeled_img_BGR[i, j, :] = (240, 40, 170)
            labeled_img_grey[i, j] = 2
        elif label == 3:
            labeled_img_BGR[i, j, :] = (0, 255, 255)
            labeled_img_grey[i, j] = 3
        elif label == 4:
            labeled_img_BGR[i, j, :] = (0, 0, 255)
            labeled_img_grey[i, j] = 4
        elif label == 5:
            labeled_img_BGR[i, j, :] = img[i, j, :]
            labeled_img_grey[i, j] = 5
        cv2.namedWindow('Applied', cv2.WINDOW_NORMAL) 
        cv2.resizeWindow('Applied',500, 500)
        cv2.imshow("Applied",labeled_img_BGR )


cv2.namedWindow('img_boundary', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('img_boundary',1000, 1000)
cv2.imshow("img_boundary",img_boundary)

while 1:
    cv2.setMouseCallback("img_boundary", mousePoints)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('p'):
        if display_mode:
            cv2.imshow("img_boundary",img)
            display_mode = not display_mode
        elif not display_mode:
            cv2.imshow("img_boundary",img_boundary)
            display_mode = not display_mode
    if key == ord('s'):
        save_result()
    # if key == ord('h'):
    #     dfd
    # if key == ord('v'):
    #     dfd
    if key == 27:
        # break
        root = tk.Tk()
        MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
        if MsgBox == 'yes':
            MsgBox_save = messagebox.askquestion ('Exit Application','Do you want to save labeling results before exit?',icon = 'warning')
            if MsgBox_save == 'yes':
                save_result()
                exit()
            else:
                exit()
        else:
            messagebox.showinfo('Return','You will now return to the application screen')
            root.destroy()



