from PIL import Image
import numpy as np

def divide_image(image, group_size):
    pixel_groups = []
    for i in range(0, rows, group_size):
    # Iterate over the columns
        for j in range(0, cols, group_size):
            # Extract a 4x4 pixel group
            group = img_matrix[i:i + group_size, j:j + group_size]
            # Append the group to the list
            pixel_groups.append(group)
    return pixel_groups

# absulute value of the sum of the pixels in the group
def f(x):
    return np.abs(np.sum(x))

def discrimination_function(pixel_group):
    return np.sum(pixel_group)  # Use np.sum to sum all elements in the pixel group

def F1(pixel_group):
    permuted_pixels = []
    for pixel in pixel_group:
        if pixel % 2 == 0:
            permuted_pixels.append((pixel + 1) % 256)
        else:
            permuted_pixels.append((pixel - 1) % 256)
    return np.array(permuted_pixels)

def F_minus_1(pixel_group):
    permuted_pixels = []
    for pixel in pixel_group:
        if pixel < 255:
            permuted_pixels.append((pixel + 1) % 256)
        else:
            permuted_pixels.append(0)
    return np.array(permuted_pixels)

def F0(pixel_group):
    return pixel_group

def negate_mask(mask):
    return np.array([-pixel for pixel in mask])

img = Image.open('/home/yassg4mer/Project/SAFM/decoded_image.png')
img_gray_scale = img.convert('L')
img_matrix = np.array(img_gray_scale)

rows, cols = img_matrix.shape
n = 4

print(rows, cols)

groups = divide_image(img_matrix, n)
discriminated_values = [discrimination_function(group) for group in groups]


print(discriminated_values)

mask = np.random.randint(-1, 2, size=n)
negate_mask = negate_mask(mask)

# apply mask to each group

    

vector = []
vector_minus_m = []
R = []
S = []
U = []

R_m = []
S_m = []
U_m = []

for i in range(len(groups)):
    block = groups[i]
    block_minus_m = groups[i]

    vector.append(f(block))
    vector_minus_m.append(f(block_minus_m))

    fx = f(block)
    fx_minus_m = f(block_minus_m)

    for s in range(4): 
        if mask[s] == 1:
            block[s] = F1(block[s])
        elif mask[s] == -1:
            block[s] = F_minus_1(block[s])
        else:
            block[s] = F0(block[s])

        if negate_mask[s] == 1:
            block_minus_m[s] = F1(block[s])
        elif negate_mask[s] == -1:
            block_minus_m[s] = F_minus_1(block[s])
        else:
            block_minus_m[s] = F0(block[s])

    vector.append(f(block))
    vector_minus_m.append(f(block_minus_m))

    ffx = f(block)
    ffx_minus_m = f(block_minus_m)

    if ffx > fx:
        R.append(1)
    elif ffx < fx:
        S.append(-1)
    else:
        U.append(0)
    
    if ffx_minus_m > fx_minus_m:
        R_m.append(1)
    elif ffx_minus_m < fx_minus_m:
        S_m.append(-1)
    else:
        U_m.append(0)


print('R R_m ', len(R), len(R_m))
print('S S_m ', len(S), len(S_m))
print('U U_m ', len(U), len(U_m))
    
    
