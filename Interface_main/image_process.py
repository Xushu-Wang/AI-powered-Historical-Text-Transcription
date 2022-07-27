import cv2

#Preprocessing - greyscale
def get_greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Preprocessing - background removal
def remove_noise5(image):
    return cv2.bilateralFilter(image, 5, 75, 75)
    #return cv2.medianBlur(image, 5)
    
    
def remove_noise3(image):
    return cv2.bilateralFilter(image, 3, 75, 75)
    #return cv2.medianBlur(image, 3)

#Preprocessing - thresholding
def thresholding(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 9)

def pre_processing(image):
    image = get_greyscale(image)
    image = remove_noise5(image)
    image = thresholding(image)
    return image