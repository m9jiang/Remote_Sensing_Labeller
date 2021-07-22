
import cv2
from skimage.segmentation import mark_boundaries, slic
# import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scio
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from skimage.util import img_as_float
from skimage import io, color

# TODO:
# Read in irgs results from MAGIC. Assign a unique label for each region. It's been done in Matlab for now

root = tk.Tk()
root.withdraw()
# if cancel 
img_path = filedialog.askopenfilenames(title='Please select the irgs result (.bmp) need to be segmented')
land_path = filedialog.askopenfilenames(title='Please select the landmask')
root.destroy()
if len(img_path) > 1:
    print("Error! Only one image should be selected each time!!!")
    exit()

irgs = io.imread(img_path[0])

if len(land_path) == 0:
    landmask = np.ones((irgs.shape[0], irgs.shape[1]), dtype=np.uint8)
else:
    landmask = io.imread(land_path[0])
    landmask = np.where(landmask, 1, 0)

irgs_remap = np.zeros((irgs.shape[0], irgs.shape[1]), dtype=np.uint8)
num_class_irgs = len(np.unique(irgs)) + 1

stride_remap = int(255/(num_class_irgs+1))

for i in range(num_class_irgs):
    irgs_remap[irgs==i] = stride_remap*(i+1) # 0 is land in the remapped image

irgs_remap = irgs_remap*landmask

irgs = (irgs + 1)*landmask
# io.imshow(irgs_remap)
# io.show()

# irgs_remap_color = color.gray2rgb(irgs_remap)
irgs_remap_color = cv2.applyColorMap(irgs_remap.astype(np.uint8), cv2.COLORMAP_JET)

# io.imshow(irgs_remap_color)
# io.show()

labeled_resut = np.ones((irgs.shape[0], irgs.shape[1]), dtype=np.uint8)
labeled_resut_color = np.ones((irgs.shape[0], irgs.shape[1], 3), dtype=np.uint8)

print('Done!')


def save_result():
    root = tk.Tk()
    folder_save_path = filedialog.askdirectory(title='Please select a directory to save the labeling results')
    cv2.imwrite(folder_save_path+'/Ground_truth_IRGS_RGB.png', labeled_resut_color)
    cv2.imwrite(folder_save_path+'/Ground_truth_IRGS_grey.png', labeled_resut)
    messagebox.showinfo(title='Successful!', message='Labeling results have been saved!')
    root.destroy()
    # confirmation

def labelChoose():
    global label_temp

    def label_OW():
        global label_temp
        label_temp = 4
        win.destroy()

    # def label_NI():
    #     global label_temp
    #     label_temp = 1
    #     win.destroy()

    def label_YI():
        global label_temp
        label_temp = 1
        win.destroy()

    def label_FYI():
        global label_temp
        label_temp = 2
        win.destroy()

    def label_MYI():
        global label_temp
        label_temp = 3
        win.destroy()

    # def label_Lead():
    #     global label_temp
    #     label_temp = 5
    #     win.destroy()

    # def label_Mixed():
    #     global label_temp
    #     label_temp = 6
    #     win.destroy()

    def label_Unknow():
        global label_temp
        label_temp = 0
        win.destroy()

    win = tk.Tk()
    button0 = tk.Button(win, text="Open Water", fg = "white", bg="blue", width=10, padx=10, command=label_OW)
    button0.pack()
    # button1 = tk.Button(win, text="New Ice", bg="lightpink", width=10, padx=10, command=label_NI)
    # button1.pack()
    button2 = tk.Button(win, text="Yong Ice", bg="purple", width=10, padx=10, command=label_YI)
    button2.pack()
    button3 = tk.Button(win, text="First-year Ice", bg="yellow", width=10, padx=10, command=label_FYI)
    button3.pack()
    button4 = tk.Button(win, text="Multi-year Ice", bg="red", width=10, padx=10, command=label_MYI)
    button4.pack()
    # button5 = tk.Button(win, text="Lead", bg="mediumslateblue", width=10, padx=10, command=label_Mixed)
    # button5.pack()
    button6 = tk.Button(win, text="Unknown", width=10, padx=10, command=label_Unknow)
    button6.pack()
    # button7 = tk.Button(win, text="Mixed region", bg="lightgreen", width=10, padx=10, command=label_Mixed)
    # button7.pack()
    win.geometry("220x220")
    win.mainloop()
    return label_temp


def mousePoints(event, x, y, flags, params):
    global img, labeled_resut, labeled_resut_color, label_temp
    if event == cv2.EVENT_LBUTTONDBLCLK:
        irgs_class = irgs[y][x]
        i, j = np.where(irgs == irgs_class)
        
        # cv2.imshow("HH/HV",highlight_boundary)
        # cv2.namedWindow('Selected Region', cv2.WINDOW_NORMAL) 
        # cv2.resizeWindow('Selected Region',1000, 1000)
        # cv2.imshow("Selected Region", focused_highlight_img)


        label = labelChoose()

        if label == 0:
            irgs_remap_color[i, j, :] = (0, 0, 0)
            labeled_resut_color[i, j, :] = (0, 0, 0)
            labeled_resut[i, j] = 0
        elif label == 1:
            irgs_remap_color[i, j, :] = (240, 40, 170)
            labeled_resut_color[i, j, :] = (240, 40, 170)
            labeled_resut[i, j] = 1
        elif label == 2:
            irgs_remap_color[i, j, :] = (0, 255, 255)
            labeled_resut_color[i, j, :] = (0, 255, 255)
            labeled_resut[i, j] = 2
        elif label == 3:
            irgs_remap_color[i, j, :] = (0, 0, 255)
            labeled_resut_color[i, j, :] = (0, 0, 255)
            labeled_resut[i, j] = 3
        elif label == 4:
            irgs_remap_color[i, j, :] = (255, 200, 150)
            labeled_resut_color[i, j, :] = (255, 200, 150)
            labeled_resut[i, j] = 4
        # elif label == 5:
        #     labeled_resut_color[i, j, :] = (93,41,48)
        #     labeled_resut[i, j] = 5  
        # elif label == 6:
        #     labeled_resut_color[i, j, :] = (144,238,144)
        #     labeled_resut[i, j] = 6
        # elif label == 7:
        #     labeled_resut_color[i, j, :] = img[i,j]
        #     labeled_resut[i, j] = 7   
        # cv2.namedWindow('Applied', cv2.WINDOW_NORMAL) 
        # cv2.resizeWindow('Applied',500, 500)
        # cv2.imshow("Applied",labeled_img_BGR )
        if cv2.getWindowProperty('IRGS', 0) >= 0:
            cv2.imshow("IRGS",irgs_remap_color)

cv2.namedWindow('IRGS', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('IRGS',1000, 1000)
cv2.imshow("IRGS",irgs_remap_color)

while 1:
    cv2.setMouseCallback("IRGS", mousePoints)
    key = cv2.waitKey(0) & 0xFF
    # if key == ord('p'):
    #     if display_mode:
    #         cv2.imshow("HH/HV",img)
    #         display_mode = not display_mode
    #     elif not display_mode:
    #         cv2.imshow("HH/HV",img_boundary)
    #         display_mode = not display_mode
    if key == ord('s'):
        save_result()
    # if key == ord('h'):
    #     dfd
    # if key == ord('v'):
    #     dfd
    if key == 27 or not cv2.getWindowProperty('IRGS', cv2.WND_PROP_VISIBLE):
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



