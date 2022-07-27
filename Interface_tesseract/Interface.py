#tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

#image
from PIL import Image, ImageTk
import numpy as np
from image_process import pre_processing

#Spelling & Word correction Algorithm
import pkg_resources
from symspellpy import SymSpell

#kraken





#tesseract
import pytesseract

#initialize the interface
root = Tk()

root.title("Transcription GUI")

#place GUI at x=350, y=10
root.geometry('+%d+%d'%(250,10))

#global variable
page_content = []

    
#OCR Core
def ocr_core(image):
    text = pytesseract.image_to_string(image, config = r"--psm 6", lang='eng')
    return text

#OCR LSTM neural network with tessdata_best
def ocr_lstm(image):
    #text = pytesseract.image_to_string(image, config = r"--oem 1 --psm 6", lang='eng')
    #text = pytesseract.image_to_string(image, config = r"--tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_fast-main --oem 1 --psm 6 ", lang = 'eng')

    text = pytesseract.image_to_string(image, config = r"--tessdata-dir /Users/andywang/Desktop/Data+/tesseract-5.1.0/tessdata/tessdata_best-main --oem 1 --psm 6", lang = 'eng')
    return text

#resize image function
def resize_image(img):
    width, height = int(img.size[0]), int(img.size[1])
    if width > height:
        height = int(360/width*height)
        width = 480
    elif height > width:
        width = int(480/height*width)
        height = 360
    else:
        width, height = 300,300
    img = img.resize((width, height))
    return img



img_label = Label(root, image = "")

#transcription process
def open_file():
    browse_text.set("loading")
    file = askopenfile(parent = root, mode = "rb", title = "Select a File", filetypes = [("image files", "*.png"), 
                                                                                         ("image files", "*.jpg"), 
                                                                                         ("image files", "*.jpeg")])
    global img_label

    if file:
        
        img_label.grid_forget()
        text_box.delete("1.0", END)
        
        img = Image.open(file)
        
        if model_name.get() == "Default Model":
            content = ocr_core(img)
        if model_name.get() == "LSTM Model":
            content = ocr_lstm(pre_processing(np.asarray(img)))
        
        result = ""
        
        if correction.get() == "Symspell Algorithm":
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

            # max edit distance per lookup (per single word, not per whole input string)
            suggestions = sym_spell.lookup_compound(content, max_edit_distance=2)

            # display suggestion term, edit distance, and term frequency
            for suggestion in suggestions:
                result += suggestion.term
        else:
            result = content


        page_content.append(result)
        
        img = resize_image(img)
        img = ImageTk.PhotoImage(img)
        
        
        img_label = Label(image = img)
        img_label.image = img
        
        img_label.grid(column = 0, row = 4, rowspan = 2)

        
        text_box.insert(1.0, page_content[-1])
        
        
        browse_text.set("Select a File")
    

        #function
        function = Frame(root, width=1100, height=60, bg="#c8c8c8")
        function.grid(columnspan=3, rowspan=1, row=3)

        copytext_btn = Button(root, text = "copy text", command = lambda:copy_text(page_content), font = ("Cormorant SC", 20),
                      height = 1, width = 15, bg="#c8c8c8")
        copytext_btn.grid(row = 3, column = 0)

        save_btn = Button(root, text = "save text", command = lambda:save_text(page_content), font = ("Cormorant SC", 20), 
                        height = 1, width = 15, bg="#c8c8c8")
        save_btn.grid(row = 3, column = 2)

    
#copy text function    
def copy_text(content):
    root.clipboard_clear()
    root.clipboard_append(content[-1])
    
#save text function
def save_text(content):
    files = [('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    file.write(content[-1])
  





#header
header = Frame(root, width=1100, height=250, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

#Title 
title = Label(root, text = "AI-powered Historical Text Transcription", font = ("Cormorant SC", 25), bg = "white")
title.grid(columnspan = 4, row = 0)

#Author
name = Label(root, text = "Team 4", font = ("Cormorant SC", 20), bg = "white")
name.grid(column = 1, row = 1)

#add logo
logo = Image.open("Data-Plus-Logo.png")
logo = logo.resize((204, 96))
logo = ImageTk.PhotoImage(logo)

logo_label = Label(image = logo, bg = "white")
logo_label.image = logo

logo_label.grid(column = 0, row = 0, rowspan = 2)


#instruction
instructions = Label(root, text = "Select an Image to Transcribe", font = ("Cormorant SC", 20), bg = "white", fg = "black")
instructions.grid(column = 2, row = 0, sticky = S)


#browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable = browse_text, bg = "#F67280", fg = "#F67280", height = 2, width = 15, 
                       command = open_file)
browse_btn.grid(column = 2, row = 1, sticky = N)
browse_text.set("Select a File")





#model menu

model_menu = Frame(root, width=1100, height=60)
model_menu.grid(column = 0, row = 2, columnspan = 3)

#Engine name

engine_opt = [
    "Kraken",
    "Tesseract"
]

engine_name = StringVar()
engine_name.set("Choose an Engine")


def choice(name):
    global correction
    global model_name
    
    if name == "Kraken":
        post_opt = [
            "Default Algorithm", 
            "Symspell Algorithm"    #More algorithms can be added. I suggest BERT (ml model) personally
        ]

        correction = StringVar()
        correction.set("Choose a post-OCR algorithm")

        correct = OptionMenu(root, correction, *post_opt)
        correct.grid(row = 2, column = 2)
        
        
    if name == "Tesseract":
        #choose a model
        model_opt = [
            "Default Model", 
            "LSTM Model"
        ]

        model_name = StringVar()
        model_name.set("Choose a Model")

        model = OptionMenu(root, model_name, *model_opt)
        model.grid(row = 2, column = 1)

        #choose a correction algorithm
        post_opt = [
            "Default Algorithm", 
            "Symspell Algorithm"    #More algorithms can be added. I suggest BERT (ml model) personally
        ]

        correction = StringVar()
        correction.set("Choose a post-OCR algorithm")

        correct = OptionMenu(root, correction, *post_opt)
        correct.grid(row = 2, column = 2)


engine = OptionMenu(root, engine_name, *engine_opt, command = choice(engine_name.get()))
engine.grid(column = 0, row = 2)




def open_new_page():
    newpage = Toplevel()
    newpage.title("How to choose a model?")
    string = "Normally, Tesseract engine & default algorithm are more suitable for printed text; \n Kraken engine & symspell algorithm are for handwritten text transcription."
    explanation = Label(newpage, text = string, font = ("Arial", 15), bg = "white", fg = "black").pack()


question_mark = Image.open(r"/Users/andywang/Desktop/AI-powered-Historical-Test-Transcription/Interface_tesseract/questionmark.png")
question_mark = question_mark.resize((18, 18))
question_mark = ImageTk.PhotoImage(question_mark)


#explanation button
explain_btn = Button(root, font = ("Cormorant SC", 10), image = question_mark, 
                     bg = "#F67280", fg = "#F67280", height = 1, width = 13, command = open_new_page)
explain_btn.grid(column = 0, row = 2, sticky = E)






#main content area - text and image extraction
main_content = Frame(root, width=1100, height=400, bg="#F8B195")
main_content.grid(columnspan=3, rowspan=2, row=4)

text_box = Text(root, width = 40, height = 20, padx = 15, pady = 15, yscrollcommand = True, bg = "white")
text_box.grid(rowspan = 2, column = 2, row = 4)








root.mainloop()