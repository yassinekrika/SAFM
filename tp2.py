import numpy as np 
from PIL import Image, ImageOps
import math

image = Image.open('img3.bmp')

image_array = np.array(image)

def extract_bit_plane(image, bit_position): 
    mask = 1 << bit_position
    bit_plane = (image & mask) >> bit_position
    return bit_plane

bit_plane_1 = extract_bit_plane(image_array, 0)

bit_plane_2 = extract_bit_plane(image_array, 1)

bit_plane_3 = extract_bit_plane(image_array, 2)

bit_plane_4 = extract_bit_plane(image_array, 3)

bit_plane_5 = extract_bit_plane(image_array, 4)

bit_plane_6 = extract_bit_plane(image_array, 5)

bit_plane_7 = extract_bit_plane(image_array, 6)

bit_plane_8 = extract_bit_plane(image_array, 7)

bit_plane_1_image = ImageOps.grayscale(Image.fromarray((bit_plane_1 * 255).astype(np.uint8)))

bit_plane_2_image = ImageOps.grayscale(Image.fromarray((bit_plane_2 * 255).astype(np.uint8)))

bit_plane_3_image = ImageOps.grayscale(Image.fromarray((bit_plane_3 * 255).astype(np.uint8)))

bit_plane_4_image = ImageOps.grayscale(Image.fromarray((bit_plane_4 * 255).astype(np.uint8)))

bit_plane_5_image = ImageOps.grayscale(Image.fromarray((bit_plane_5 * 255).astype(np.uint8)))

bit_plane_6_image = ImageOps.grayscale(Image.fromarray((bit_plane_6 * 255).astype(np.uint8)))

bit_plane_7_image = ImageOps.grayscale(Image.fromarray((bit_plane_7 * 255).astype(np.uint8)))

bit_plane_8_image = ImageOps.grayscale(Image.fromarray((bit_plane_8 * 255).astype(np.uint8)))


bit_plane_1_image.save('bit_plane_1.jpg')

bit_plane_2_image.save('bit_plane_2.jpg')

bit_plane_3_image.save('bit_plane_3.jpg')

bit_plane_4_image.save('bit_plane_4.jpg')

bit_plane_5_image.save('bit_plane_5.jpg')

bit_plane_6_image.save('bit_plane_6.jpg')

bit_plane_7_image.save('bit_plane_7.jpg')

bit_plane_8_image.save('bit_plane_8.jpg')

