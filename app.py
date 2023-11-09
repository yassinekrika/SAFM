from PIL import Image, ImageChops
import sys
# from tkinter import ttk

try:
    img = Image.open('img3.bmp')
except IOError:
    print("Error when opening the image file")
    sys.exit(1)

print(img.format, img.size, img.mode)

# img.show()

# img.close()

colonne, ligne = img.size

imgF = Image.new(img.mode, img.size)

for i in range(ligne):
    for j in range(colonne):
        pixel = img.getpixel((j,i))
        p = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
        imgF.putpixel((j, i), p)

#imgF.show()
#imgF.close()

imgInvert = ImageChops.invert(img)
imgInvert.show()
imgInvert.close()

