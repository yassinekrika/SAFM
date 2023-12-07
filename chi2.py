from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

img = Image.open('/home/yassg4mer/Project/SAFM/bikes.bmp')
img_gray_scale = img.convert('L')
img_matrix = np.array(img_gray_scale)

rows, cols = img_matrix.shape

group_size = 8

pixel_groups = []
for i in range(0, rows, group_size):
    # Iterate over the columns
    for j in range(0, cols, group_size):
            # Extract a 4x4 pixel group
        group = img_matrix[i:i + group_size, j:j + group_size]
            # Append the group to the list
        pixel_groups.append(group)

# calulate histogram for group one 
histograms = []
for group in pixel_groups:
    histogram = np.histogram(group.flatten(), bins=range(256), range=(0, 256))
    histograms.append(histogram)

# show histogram for group one
# plt.plot(histograms[0][0])    
# plt.show()

# print(histograms)

# calculate chi2 for each group
stat, p, do, expected = chi2_contingency(histograms)

alpha = 0.05
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')