import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


img1 = cv2.imread(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/images/imgComp.jpg")
img2 = cv2.imread(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/images/imgComp.jpg")

def get_greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.bilateralFilter(image, 5, 75, 75)

def thresholding(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 9)

img2 = get_greyscale(img2)
img2 = remove_noise(img2)
img2 = thresholding(img2)
img2 = np.dstack([img2] * 3)

print(img1.shape, img2.shape)

Hori = np.concatenate((img1, img2), axis = 1)

cv2.imshow('HORIZONTAL', Hori)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('pre-processing.jpg', Hori)