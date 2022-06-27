import pytesseract
import cv2 

def ocr_core(image):
    #text = pytesseract.image_to_string(image, config = r"--psm 6", lang='eng')
    text = pytesseract.image_to_string(image, config = r"--tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_best-main --oem 1 --psm 6 ", lang = 'eng')
    return text

def get_greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.bilateralFilter(image, 5, 75, 75)
    #return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 9)

img = cv2.imread(r"/Users/andywang/Desktop/wtddy11001-8 copy.jpg")
img = get_greyscale(img)
img = remove_noise(img)
img = thresholding(img)

print(ocr_core(img))