from PIL import Image
import numpy as np


def divide_image(image, n):
    groups = [image[i:i + n] for i in range(0, len(image), n)]
    return groups

def discrimination_function(pixel_group):
    return sum(pixel_group)

def reversible_permutation(pixel_group, mask):
    return np.multiply(pixel_group, mask)

def classify_pixel_group(group, threshold):
    if group < -threshold:
        return "Set A"
    elif group > threshold:
        return "Set B"
    else:
        return "Set C"

def F1(pixel_group):
    # Reversible permutation function F1
    return [(pixel + 1) % 256 if pixel % 2 == 0 else (pixel - 1) % 256 for pixel in pixel_group]

def F_minus_1(pixel_group):
    # Reversible permutation function F-1
    return [(pixel + 1) % 256 if pixel < 255 else 0 for pixel in pixel_group]

def F0(pixel_group):
    # Reversible permutation function F0
    return pixel_group

def negate_mask(mask):
    # Calculate the negated mask −M
    return [-pixel for pixel in mask]

img = Image.open('/home/yassg4mer/Project/SAFM/bikes.bmp')

img_gray_scale = img.convert('L')

img_matrix = np.array(img_gray_scale)

rows, cols = img_matrix.shape

n = 4

# Q1
groups = divide_image(img_matrix, n)

# Q2
discriminated_values = [discrimination_function(group) for group in groups]

# Q3
mask = np.random.randint(-1, 2, size=n)  
pixel_group = [i for i in range(0, 256, 2)]

permuted_F1 = F1(pixel_group)
permuted_F_minus_1 = F_minus_1(pixel_group)
permuted_F0 = F0(pixel_group)

negated_mask = negate_mask(mask) 

print(discriminated_values)
