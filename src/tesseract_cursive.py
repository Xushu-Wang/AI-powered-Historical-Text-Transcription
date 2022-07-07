#Graphing packages
from PIL import Image, ImageOps, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt

#Preprocessing, OCR Engine & Evaluation
import pytesseract
import cv2
from thefuzz import fuzz
from asrtoolkit import cer, wer

#Spelling & Word correction Algorithm
import pkg_resources
from symspellpy import SymSpell

#open rtf document 
from striprtf.striprtf import rtf_to_text


#OCR default 
def ocr_default(image):
    text = pytesseract.image_to_string(image, config = r"--psm 6", lang='eng')
    return text

#OCR LSTM neural network with tessdata_best
def ocr_lstm(image):
    #text = pytesseract.image_to_string(image, config = r"--oem 1 --psm 6", lang='eng')
    #text = pytesseract.image_to_string(image, config = r"--tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_fast-main --oem 1 --psm 6 ", lang = 'eng')

    text = pytesseract.image_to_string(image, config = r"--tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_best-main --oem 1 --psm 6", lang = 'eng')
    return text

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


# Alternative image processing by increasing contrast
#------------------------------
#image = Image.open("img.jpg")

#if image.mode == 'RGBA':
    r,g,b,a = image.split()
    image = Image.merge('RGB', (r,g,b))

#image = ImageOps.invert(image)

#contrast = ImageEnhance.Color(image)
#image = contrast.enhance(2)
#---------------------------------




#import images
stewart = cv2.imread(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/images/stewart.jpg")
mcmillan = cv2.imread(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/images/mcmillan.jpg")
martha = cv2.imread(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/images/martha.jpg")

#invoke preprocessing
stewart = get_greyscale(stewart)
stewart = remove_noise5(stewart)
stewart = thresholding(stewart)

mcmillan = get_greyscale(mcmillan)
mcmillan = remove_noise5(mcmillan)
mcmillan = thresholding(mcmillan)

martha = get_greyscale(martha)
martha = remove_noise5(martha)
martha = thresholding(martha)



#mcmillian is vertical handwriting
mcmillan = cv2.rotate(mcmillan, cv2.ROTATE_90_CLOCKWISE)

#cropping
#mcmillan = mcmillan[100:800, 100:900]

#check it
#cv2.imshow("image", mcmillan)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#correction algorithm
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
bigram_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
)
# term_index is the column of the term and count_index is the
# column of the term frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

# lookup suggestions for multi-word input strings (supports compound
# splitting & merging)
trans_s = ocr_lstm(stewart)
trans_mc = ocr_lstm(mcmillan)
trans_ma = ocr_lstm(martha)


# max edit distance per lookup (per single word, not per whole input string)
suggestion_s = sym_spell.lookup_compound(trans_s, max_edit_distance=2)
suggestion_mc = sym_spell.lookup_compound(trans_mc, max_edit_distance=2, transfer_casing=True)
suggestion_ma = sym_spell.lookup_compound(trans_ma, max_edit_distance=2, transfer_casing=True)

trans_stewart = ""
trans_mcmillan = ""
trans_martha = ""

# display suggestion term, edit distance, and term frequency
for suggestion in suggestion_s:
    trans_stewart += suggestion.term

for suggestion in suggestion_mc:
    trans_mcmillan += suggestion.term
    
for suggestion in suggestion_ma:
    trans_martha += suggestion.term

#print(trans_stewart)
#print(trans_mcmillan)
#print(trans_martha)

#ground truth

file_s = open(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/gt/stewart.rtf")
content_s = file_s.read()
gt_stewart = rtf_to_text(content_s)

file_mc = open(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/gt/mcmillan.rtf")
content_mc = file_mc.read()
gt_mcmillan = rtf_to_text(content_mc)

file_ma = open(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/gt/martha.rtf")
content_ma = file_ma.read()
gt_martha = rtf_to_text(content_ma)

stewart_data = (cer(trans_stewart, gt_stewart), wer(trans_stewart, gt_stewart), fuzz.ratio(trans_stewart, gt_stewart))
mcmillan_data = (cer(trans_mcmillan, gt_mcmillan), wer(trans_mcmillan, gt_mcmillan), fuzz.ratio(trans_mcmillan, gt_mcmillan))
martha_data = (cer(trans_martha, gt_martha), wer(trans_martha, gt_martha), fuzz.ratio(trans_martha, gt_martha))


print("Stewart, Harriet Sanderson: ", stewart_data)
print("Mcmillan, Mary : ", mcmillan_data)
print("Crawford, Martha Foster: ", martha_data)


#Side-by-side bar chart

N = 3

fig, ax = plt.subplots()

# Data on X-axis

cer = np.array([cer(trans_stewart, gt_stewart), cer(trans_mcmillan, gt_mcmillan), cer(trans_martha, gt_martha)])
wer = np.array([wer(trans_stewart, gt_stewart), wer(trans_mcmillan, gt_mcmillan), wer(trans_martha, gt_martha)])
distance = (fuzz.ratio(trans_stewart, gt_stewart), fuzz.ratio(trans_mcmillan, gt_mcmillan), fuzz.ratio(trans_martha, gt_martha))

cer = 100 - cer
wer = 100 - wer

# Position of bars on x-axis
ind = np.arange(N)

# Figure size

# Width of a bar 
width = 0.3       

# Plotting
ax.bar(ind + 0.15 - width, cer , width, label='car', color = 'rosybrown')
ax.bar(ind + 0.15, wer, width, label='war', color = 'indianred')
ax.bar(ind + 0.15 + width, distance, width, label='levenstein distance', color = 'maroon')

plt.xlabel('Author', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            ,weight = 'bold')
plt.ylabel('Accuracy (%)', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            ,weight = 'bold')
plt.title('Tesseract Accuracy (Comparing Different Authors)', fontsize = 18, font = "DejaVu Sans",loc = "center", 
            pad = 15, weight = "bold")

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('Stewart', 'Mcmillan', 'Crawford'), font = 'DejaVu Sans', weight = 'bold')

# Finding the best position for legends and putting it
plt.legend(loc='best')
plt.show()