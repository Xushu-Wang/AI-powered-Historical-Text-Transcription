import sys
import os
import PySimpleGUI as sg
import subprocess
from PIL import Image
from kraken import binarization
from kraken import blla
from kraken import serialization
from kraken.lib import models
from kraken import rpred
from kraken import pageseg

#GUI creation

sg.theme('Dark Blue 15')

list_filetype = [".png",".tiff",".jpg"]
list_model = ["English Cursive Handwritten"]


layout =  [[sg.Text('Select image folder: ',tooltip="Select the folder on your computer containing the images to be transcribed."),sg.InputText(),sg.FolderBrowse()],
           
           [sg.Text('Select model:          ',tooltip="Select the most appropriate recognition model based on the language and writing style of your text."),sg.Combo(list_model, size=(25,4))],
           
           
           [sg.Button('Start')]]

window = sg.Window('Transcription Settings',layout)


while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Start':
        break

#if values[2] == ".png":
 # path = values[0] + "/*.png"
#elif values[2] == ".tiff":
 # path = values[0] + "/*.tiff"
#elif values[2] == ".jpg":
 # path = values[0] + "/*.jpg"

if values[1] == "English Cursive Handwritten":
  model = "model_eng_cursive.mlmodel"

process = "kraken -i " + values[0] + " output.txt binarize segment ocr -m " + model
lol = "cd data"

trueprocess = process.split()

# Run transcription console command

# print(process)
# subprocess.run(process, shell=True)

for file in os.listdir(values[0]):

	# API Binarization

	file_loc = values[0] + "/" + file
	im = Image.open(file_loc)
	bw_im = binarization.nlbin(im)

	# API Segmentation

	seg = pageseg.segment(bw_im)
	    
	# API Recognition

	rec_model_path = model
	if values[1] == "English Cursive Handwritten":
		model = models.load_any('model_eng_cursive.mlmodel')
	pred_it = rpred.rpred(model, im, seg)
	txtpart = file.split(".")
	txtname = txtpart[0] + '.txt'
	f = open(txtname,"w")
	for record in pred_it:
		print(record, file=f)
		
	f.close()
