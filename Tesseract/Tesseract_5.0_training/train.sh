## Adapted from Arabic Handwriting project, availabe from tesseract training doc in github

# Make directory
mkdir -p ~/CursiveHandwriting
cd ~/CursiveHandwriting

# Get the data.
curl -L datadir >Cursive_part_1
curl -L datadir >Cursive_part_2

# Extract the data. 
7za x Cursive_part_1
7za x Cursive_part_2
mkdir -p IMG PAGE
mv *.tif IMG
mv *.xml PAGE

# Remove spaces in filenames (workaround because currently not fully supported by OCR-D).
for i in IMG/* PAGE/*; do mv -v "$i" "${i/ /}"; done
for i in IMG/* PAGE/*; do mv -v "$i" "${i/ /}"; done
perl -pi -e 's/(imageFilename=.*) (.*tif)/$1$2/' PAGE/*
perl -pi -e 's/(imageFilename=.*) (.*tif)/$1$2/' PAGE/*
perl -pi -e 's/(filename=.*) (.*tif)/$1$2/' PAGE/*
perl -pi -e 's/(filename=.*) (.*tif)/$1$2/' PAGE/*

# Fix path for images for further processing.
perl -pi -e 's/imageFilename="/imageFilename="IMG\//' PAGE/*

# Remove alternative image filenames which are not available from PAGE files.
perl -pi -e 's/.*AlternativeImage.*//' PAGE/*

# Create OCR-D workspace and add images and PAGE files.
ocrd workspace init
for i in IMG/*; do base=$(basename "$i" .tif); ocrd workspace add "$i" -G IMG -i "${base}_img" -g "$base" -m image/tiff; done
for i in PAGE/*; do base=$(basename "$i" .xml); ocrd workspace add "$i" -G PAGE -i "${base}_page" -g "$base" -m application/vnd.prima.page+xml; done

# Binarize and denoise images.
ocrd-olena-binarize -I PAGE -O WOLF,WOLF-IMG -m mets.xml -p <(echo '{"impl":"wolf"}')
ocrd-cis-ocropy-denoise -I WOLF -O DENOISE,DENOISE-IMG -m mets.xml -p '{"level-of-operation": "line"}'

# Extract the line images.
ocrd-segment-extract-lines -I DENOISE -O LINES -m mets.xml

# Remove empty texts (files contain only a line feed) which cannot be used for training.
rm -v $(find LINES -size 1c)

# Remove lines with missing transcriptions.
rm -v $(fgrep -l ؟ LINES/*txt)
rm -v $(fgrep -l '[' LINES/*txt)

# Remove images which were written from top to bottom or from bottom to top.
# The heuristics here assumes that such images have a 3 digit width and a 4 digit height.
rm -v $(file *png|grep ", ... x ....,"|sed s/:.*//)


# Create box files needed for Tesseract training.
for t in ~/CursiveHandwriting/GT/LINES/*.txt; do test -f ${t/gt.txt/box} || (echo $t && ./generate_wordstr_box.py -i ${t/gt.txt/bin.png} -t $t -r >${t/gt.txt/box}); done 

nohup make LANG_TYPE=eng MODEL_NAME=CursiveHandwriting GROUND_TRUTH_DIR=/home/stweil/src/ArabicHandwriting/GT/LINES PSM=6 START_MODEL=eng TESSDATA=datadir EPOCHS=20 lists >>data/ArabicHandwritingOCRD.log
nohup make LANG_TYPE=eng MODEL_NAME=CursiveHandwriting GROUND_TRUTH_DIR=/home/stweil/src/ArabicHandwriting/GT/LINES PSM=6 START_MODEL=eng TESSDATA=/home/stweil/src/github/OCR-D/venv-20200408/share/tessdata EPOCHS=20 training >>data/ArabicHandwritingOCRD.log