from PIL import Image
import numpy as np
from scipy.stats import chi2_contingency

# Load the image and convert it to grayscale
img = Image.open('/home/yassg4mer/Project/SAFM/plane.bmp')
img_gray_scale = img.convert('L')
img_matrix = np.array(img_gray_scale)

flattened_img = img_matrix.flatten()

histogram, bin_edges = np.histogram(flattened_img, bins=range(256), range=(0, 256))

expected = np.full_like(histogram, len(flattened_img) / 256)

stat, p,_, _= chi2_contingency([histogram, expected])
 
alpha = 0.05
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
