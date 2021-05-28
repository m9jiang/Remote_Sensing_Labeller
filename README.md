# Remote Sensing Labeller

 ## Description
Remote Sensing Labeller is a graphical image annotation tool inspired by  the idea of improving labeling efficiency for remote sensing images.

It is written in Python and uses OpenCV for its graphical interface. Qt will be adopted in the furture versions.

## Requirements

- Ubuntu / macOS / Windows
- Python3

## Installation

You need to install the following dependencies 
- cv2
- skimage
- numpy
- scipy
- tkinter

Run:
```bash
pip install cv2
pip install skimage
pip install numpy
pip install scipy
pip install tkinter
```
Then:
```
python Region_labeling.py
```
### Windows

Simply run Remote_Sensing_Labeller/dist/Region_labeling/Region_labeling.exe

## Tutorial

You need two input files: a reference remote sensing image and its oversegmentation result. After you run Remote Sensing Labeller, the prompt asks for the corresponding directory. The reference image with boundaries of each superpixel will be shown in a window. Double left click the interested superpixl and the boundary will highlight. Assign the label for the superpixel using the prompt dialog. Press 'p' to turn on/off the overlayed boundaries on the reference image. Press 's' to save the labeling result. 