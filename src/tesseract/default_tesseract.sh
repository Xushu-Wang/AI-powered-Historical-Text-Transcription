# Basic command line usage -- "tesseract imagename outputbase"

## Available language for this project -- English (eng) & Middle Ages English (enm)

## psm mode (line segmentation mode): 0 - 13
## oem mode (ml mode): 0 - 3
## output: txt, pdf, hocr

tesseract /Users/andywang/Desktop/Test 1/img.jpg out.txt -l enm --psm 0
tesseract /Users/andywang/Desktop/Test 1/img.jpg out.txt -l eng 
tesseract /Users/andywang/Desktop/Test 1/img.jpg out.txt -l eng --psm 6
tesseract /Users/andywang/Desktop/Test 1/img.jpg out.txt -l enm --psm 6