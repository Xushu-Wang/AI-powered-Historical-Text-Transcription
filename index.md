# Data+ 2022: AI-powered Historical Text Transcription

## Introduction

The Rubenstein Library holds millions of pages of handwritten documents ranging from ancient Papyri to records of Southern plantations to 21st century letters and diaries. Only a small subset of these documents have been digitized and made available online, and even fewer have been transcribed. The lack of text transcripts for handwritten documents impairs discovery and use of the materials, and prohibits any kind of computational text analysis that might support new avenues of research, including research related to the histories of racial injustice.
  
  While Optical Character Recognition (OCR) technology has made it possible to derive machine-readable text from typewritten documents in an automated way for several decades, the work of transcribing handwritten documents remains largely manual and labor-intensive. In the last few years, however, platforms like Transkribus have sought to harness the power of machine-learning by using Handwriting Text Recognition (HTR) to extract text from manuscripts and other handwritten documents held in libraries and archives. To date, the Rubenstein Library has conducted a few small-scale HTR experiments with mixed (and mostly disappointing) results. We have a lot to learn about the viability of HTR for our collections and about how to incorporate HTR into our existing workflows.
  
  In this Data+ project, students will test the viability of AI-powered HTR for transcribing digitized handwritten documents in the Rubenstein library and make recommendations for how the library might incorporate HTR into existing workflows, projects, and interfaces. Source material will be drawn from the Duke Digital Collections and will initially focus on a subset of digitized 19th-20th century women’s travel diaries, but could also include yet-to-be digitized materials related to the early history of Duke such as sermons, diaries, and lecture notes of our institution’s first president, Braxton Craven. As we approach Duke’s centennial, HTR-generated transcripts of the Craven materials would help support the university’s ongoing investigation into its institutional connection to slavery.


## Machine-Learning Pipelines

Sample Workflow: 

```mermaid
graph TD;
    A[Pre-processing] --> B[OCR Engine];
    B-->C[Correction Algorithm];
    C--> D[Evaluation];
    D--> B;
```
 

## Four Available OCR Engine
 
## Transkribus

### Introducton

  Transkribus is a comprehensive platform for the digitisation, AI-powered text recognition, transcription and searching of historical documents – from any place, any time, and in any language. Visit the official [Transkribus](https://readcoop.eu/transkribus/?sc=Transkribus) website here. 

Strength
- extremely high accuracy in cursive hand written text recognition
- commercial product with mature software available

Weakness
- Low generalizability
- Not open-sourced, not replicable


### DataSet & Accuracy

|Training Set| Bentham Project |
|Testing Set | Women Traveling Diaries | 

side by side images


## Tesseract

## Introducton

  Tesseract was originally developed at Hewlett-Packard Laboratories Bristol and at Hewlett-Packard Co, Greeley Colorado between 1985 and 1994, with some more changes made in 1996 to port to Windows, and some C++izing in 1998. In 2005 Tesseract was open sourced by HP. From 2006 until November 2018 it was developed by Google. Visit [Tesseract](https://github.com/tesseract-ocr/tesseract) repository here.

Strength
- Extremely high accuracy in recognizing a majority of printed fonts
- Various line segmentation & Recognition mode
- High Generalizability
- Tesseract comes with a python wrapper class called Pytesseract [(https://pypi.org/project/pytesseract/)]
- Support training

Weakness
- extremely tenuous training process (using shell scripts), nearly inable to train
- Inable to recognize cursive fonts, accuracy changes correspondent with cursiveness. 

## DataSet & Accuracy

|Training Set|.|
|Testing Set| |



| Font type | Author | Accuracy |
| --------- | ------ | -------- |
| Non-cursive | N/A  | 98% |
| Cursive | N/A | 10% |
| Cursive | Crawford, Martha | 10% |
| Cursive | McMillan, Mary | 10% |
| Cursive | Harriet, Sanderson | 10% |


image


# Kraken

https://kraken.re/master/index.html

## Introducton

## DataSet & Accuracy


 Strength
 - Easily Trainable [^1]
 
 
 
 [^1]: The training Set of all the OCR Engines require highly consistent and legible hand-written documents, which can provide high quality ground-truth files. 



# Google Cloud AI

## Introducton



## Data & Accuracy













**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Xushu-Wang/AI-powered-Historical-Test-Transcription/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

