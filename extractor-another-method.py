from PIL import Image
import pytesseract
from skimage.io import imread
from skimage.color import rgb2gray
from scipy import signal as sig
import numpy as np



img_path = '/Users/macbookpro/Desktop/Projects/Machine_Learning_Projects/ID_Card_Info_Extractor/Sample Data/Natioanal ID/3.jpg'
img = imread(img_path)
imggray = rgb2gray(img)


def gradient_x(imggray):
    ##Sobel operator kernels.
    kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    return sig.convolve2d(imggray, kernel_x, mode='same')
def gradient_y(imggray):
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    return sig.convolve2d(imggray, kernel_y, mode='same')

I_x = gradient_x(imggray)
I_y = gradient_y(imggray)
Ixx = ndi.gaussian_filter(I_x**2, sigma=1)
Ixy = ndi.gaussian_filter(I_y*I_x, sigma=1)
Iyy = ndi.gaussian_filter(I_y**2, sigma=1)
new_path = "/Users/macbookpro/Desktop/Projects/Machine_Learning_Projects/ID_Card_Info_Extractor/Sample Data/new.jpg"



text = pytesseract.image_to_string(Image.open(new_path), lang="eng")
print(text)