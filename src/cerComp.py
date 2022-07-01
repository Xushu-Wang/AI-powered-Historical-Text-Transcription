import numpy as np
import matplotlib.pyplot as plt

#Side-by-side bar chart

N = 4

# Data on X-axis

cer = np.array([28.69, 20, 1.84, 66.09])
wer = np.array([46.77, 20, 5.56, 92.95])
distance = np.array([80, 20, 96, 50])


# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,7))

# Width of a bar 
width = 0.3       

# Plotting
plt.bar(ind + 0.15 - width, cer , width, label='CER')
plt.bar(ind + 0.15, wer, width, label='WER')
plt.bar(ind + 0.15 + width, distance, width, label='Levenshtein distance')

plt.xlabel('OCR Engine', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            ,color = '#333333')
plt.ylabel('Accuracy (%)', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            ,color = '#333333')
plt.title('Different OCR Engines', fontsize = 18, font = "DejaVu Sans",loc = "center", 
          color = 'black', pad = 15, weight = "bold")

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('Google Cloud AI', 'Kraken', 'Transkribus', 'Tesseract'), font = 'DejaVu Sans')

# Finding the best position for legends and putting it
plt.legend(loc='best')
plt.show()