import numpy as np
import matplotlib.pyplot as plt

def autolabel(rectangle):
    for rect in rectangle:
        height = rect.get_height()
        
        ax.annotate(str(height), xy = (rect.get_x() + 0.05, height + 0.3), font = 'Arial', weight = 'bold')

fig, ax = plt.subplots()


#Side-by-side bar chart

N = 5

# Data on X-axis

cer = np.array([28.69, 15, 1.84, 66.09, 19.83])
wer = np.array([46.77, 20, 5.56, 92.95, 42.13])
distance = np.array([80, 85, 96, 50, 87])


# Position of bars on x-axis
ind = np.arange(N)

# Width of a bar 
width = 0.3       

# Plotting
rect1 = ax.bar(ind + 0.15 - width, cer , width, label='CER', color = 'rosybrown')
rect2 = ax.bar(ind + 0.15, wer, width, label='WER', color = 'indianred')
rect3 = ax.bar(ind + 0.15 + width, distance, width, label='Levenshtein distance', color = 'maroon')

plt.xlabel('OCR Engine', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            ,weight = 'bold')
plt.ylabel('Accuracy (%)', font = "DejaVu Sans", fontsize = 14, labelpad = 15
            , weight = 'bold')
ax.set_title('OCR Engines Comparison', fontsize = 18, font = "DejaVu Sans",loc = "center", 
          color = 'black', pad = 15, weight = "bold")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)

ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

#fig.tight_layout()


autolabel(rect1)
autolabel(rect2)
autolabel(rect3)

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('Google Cloud AI', 'Kraken', 'Transkribus', 'Tesseract', 'AWS Textract'), font = 'DejaVu Sans', weight = 'bold')

# Finding the best position for legends and putting it
ax.legend(loc='best')
plt.show()