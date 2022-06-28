nohup make training MODEL_NAME=eng_fast START_MODEL=eng TESSDATA=/Users/andywang/Desktop/eng_fast.traineddata MAX_ITERATIONS=10000 > /Users/andywang/Desktop/tesseract-5.1.0/tesstrain-main/plot/TESSTRAIN.LOG



tesseract /Users/andywang/Desktop/Data+/img.jpg - --tessdata-dir /Users/andywang/Desktop/tesseract-5.1.0/tessdata/tessdata_fast-main/eng.traineddata --oem 1 --psm 6 -l eng