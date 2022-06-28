import pytesseract
import cv2 
from asrtoolkit import cer,wer
from striprtf.striprtf import rtf_to_text

img = cv2.imread(r"/Users/andywang/Desktop/97cfa1fd-6f77-4a92-ab86-ec7f41810208-84.jpg")


def get_greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.bilateralFilter(image, 5, 75, 75)
    #return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 9)

img = get_greyscale(img)
img = remove_noise(img)
img = thresholding(img)

file = open(r"/Users/andywang/Desktop/stewart.rtf")
con = file.read()
gt = rtf_to_text(con)

print(pytesseract.image_to_string(img, config = "--tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_best-main --oem 1 --psm 6", lang = 'eng'))
print(cer(pytesseract.image_to_string(img, config = "--tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_best-main --oem 1 --psm 6", lang = 'eng'), gt))
print(wer(pytesseract.image_to_string(img, config = "--tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_best-main --oem 1 --psm 6", lang = 'eng'), gt))