import numpy as np
import matplotlib.pyplot as plt

#Side-by-side bar chart

N = 4

# Data on X-axis

cer = np.array([10, 20, 30, 40])
wer = np.array([10, 20, 30, 40])

cer = 100 - cer
wer = 100 - wer


# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,7))

# Width of a bar 
width = 0.3       

# Plotting
plt.bar(ind - width, cer , width, label='car')
plt.bar(ind, wer, width, label='war')

plt.xlabel('Author', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            ,color = '#333333')
plt.ylabel('Accuracy (%)', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            ,color = '#333333')
plt.title('Tesseract Accuracy (Comparing Different Authors)', fontsize = 18, font = "DejaVu Sans",loc = "center", 
          color = 'black', pad = 15, weight = "bold")

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('Google Cloud AI', 'Kraken', 'Transkribus', 'Tesseract'), font = 'DejaVu Sans')

# Finding the best position for legends and putting it
plt.legend(loc='best')
plt.show()