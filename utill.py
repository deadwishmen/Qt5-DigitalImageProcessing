import cv2
import numpy as np
from scipy import ndimage as ndi
import argparse
def adaptiveThreshold(image, types):
    img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if (types == 'cv2.THRESH_BINARY'):
        Type = cv2.THRESH_BINARY
    if(types == 'cv2.ADAPTIVE_THRESH_MEAN_C,\cv2.THRESH_BINARY'):
        img_threshold = cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        return img_threshold
    if(types == 'cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\cv.THRESH_BINARY'):
        img_threshold = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        return img_threshold
    if(types == 'cv2.THRESH_TOZERO'):
        Type = cv2.THRESH_TOZERO
    if(types == 'cv2.THRESH_TOZERO_INV'):
        Type = cv2.THRESH_TOZERO_INV
    img_threshold = cv2.adaptiveThreshold(img_grey, 255, Type , 11, 2)
    return img_threshold
def Threshold(image,thresh, maxval, types):
    if (types == 'cv2.THRESH_BINARY'):
        Type = cv2.THRESH_BINARY
    if(types == 'cv2.THRESH_BINARY_INV'):
        Type = cv2.THRESH_BINARY_INV
    if(types == 'cv2.THRESH_TRUNC'):
        Type = cv2.THRESH_TRUNC
    if(types == 'cv2.THRESH_TOZERO'):
        Type = cv2.THRESH_TOZERO
    if(types == 'cv2.THRESH_TOZERO_INV'):
        Type = cv2.THRESH_TOZERO_INV
    image = cv2.cvtColor(image, 0)
    ret, img_threshold = cv2.threshold(image, 127, 255, Type)
    return img_threshold
def Canny(image,t_lower, t_upper, aperture_size, L2Gradient):
    L2Gradient = bool(L2Gradient)
    edge = cv2.Canny(image, t_lower, t_upper,
                     apertureSize=aperture_size,
                     L2gradient=True)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)
    return edge
def LoG(image,ksize):
    a = (ksize, ksize)
    blur = cv2.GaussianBlur(image, a , 0)
    img_LoG = cv2.Laplacian(blur, ddepth=-1)
    return img_LoG
def Sobel(image,ksize, d):
    if d == 'dx':
        sobel = cv2.Sobel(src=image, ddepth=-1, dx=1, dy=0, ksize=ksize)  # x
    if d == 'dy':
        sobel = cv2.Sobel(src=image, ddepth=-1, dx=0, dy=1, ksize=ksize)  # y
    if d =='dxy':
        sobel = cv2.Sobel(src=image, ddepth=-1, dx=1, dy=1, ksize=ksize)  # xy
    return sobel
def Laplacina(image, ksize):
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_Laplacina = cv2.Laplacian(image , ddepth = -1, ksize = ksize)
    return img_Laplacina
def Gaussian(image, ksize, borderType):
    if (borderType == 'cv2.BORDER_CONSTANT'):
        Types = cv2.BORDER_CONSTANT
    if(borderType == 'cv2.BORDER_REFLECT'):
        Types = cv2.BORDER_REFLECT
    if(borderType == 'cv2.BORDER_REFLECT_101'):
        Types = cv2.BORDER_REFLECT_101
    if(borderType == 'cv2.BORDER_REPLICATE'):
        Types = cv2.BORDER_REPLICATE
    if(borderType == 'cv2.BORDER_WRAP'):
        Types = cv2.BORDER_WRAP
    a = (ksize, ksize)
    img_Median = cv2.GaussianBlur(image, a , Types)
    return img_Median

def Median(image, ksize, borderType):
    if (borderType == 'cv2.BORDER_CONSTANT'):
        Types = cv2.BORDER_CONSTANT
    if(borderType == 'cv2.BORDER_REFLECT'):
        Types = cv2.BORDER_REFLECT
    if(borderType == 'cv2.BORDER_REFLECT_101'):
        Types = cv2.BORDER_REFLECT_101
    if(borderType == 'cv2.BORDER_REPLICATE'):
        Types = cv2.BORDER_REPLICATE
    if(borderType == 'cv2.BORDER_WRAP'):
        Types = cv2.BORDER_WRAP
    img_Median = cv2.medianBlur(image, ksize ,Types)
    return img_Median
def equalizeHist(image):
    colorimage_b = cv2.equalizeHist(image[:, :, 0])
    colorimage_g = cv2.equalizeHist(image[:, :, 1])
    colorimage_r = cv2.equalizeHist(image[:, :, 2])
    colorimage_e = np.stack((colorimage_b, colorimage_g, colorimage_r), axis=2)
    return colorimage_e
################Affine#################
def Translation(image, Tx, Ty):
    height, width = image.shape[:2]
    T = np.float32([[1, 0, Tx], [0, 1, Ty]])
    img_translation = cv2.warpAffine(image, T, (width, height))
    return img_translation
def Rotation(image, angle):
    img_rotation = ndi.rotate(image,angle, mode = 'constant' )
    return img_rotation
def Scaling(image, Sx, Sy):
    # s_x, s_y = 0.75, 1.25
    mat_scale = np.array([[Sx, 0, 0],
                          [0, Sy, 0],
                          [0, 0, 1]])
    img_scaling = ndi.affine_transform(image, mat_scale)
    return img_scaling
def Shearing(image,lambda1):
    mat_shear = np.array([[1, lambda1, 0],
                          [lambda1, 1, 0],
                          [0, 0, 1]])
    img_shearing = ndi.affine_transform(image, mat_shear)
    return img_shearing
def adjust_gamma(image, gamma):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)