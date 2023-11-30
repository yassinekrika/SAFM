from PIL import Image
import numpy as np

img = Image.open('/home/yassg4mer/Project/SAFM/bikes.bmp')

img_gray_scale = img.convert('L')

img_matrix = np.array(img_gray_scale)

rows, cols = img_matrix.shape

block_size = 4
abs_total = []

def absolute(block):
    abs = 0
    for n in range(0, len(block) - 1):
        abs += np.abs(block[n + 1] - block[n])
    return abs

def f1(x): 
    if x % 2 == 0:
        x += 1
    else: 
        x -= 1

    return x
    
def f0(x): 
    return x

for i in range(0, rows, block_size):
    for j in range(0, cols):
        block = img_matrix[i:i + block_size, j]
        
        abs = absolute(block)
        
        abs_f1 = f1(abs)
        
        abs_f0 = f0(abs)


        abs_total.append(abs)
        

