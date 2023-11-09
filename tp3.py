import numpy as np
from PIL import Image

image = Image.open('img3.bmp')

message = 'This is a secret message'
message_binaire = ''.join(format(ord(char), '08b') for char in message)

def cacher_message(image, message):
    largeur, hauteur = image.size
    donnees = image.load()
    message += "1111111111111110"

    index_message = 0

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b, = donnees[x, y]

            r = r & 254 | int(message[index_message])
            g = g & 254 | int(message[index_message])
            b = b & 254 | int(message[index_message])
            index_message += 1

            if index_message == len(message):
                image.save('image_cache.jpg')
                return image
    
    return None

def extraire_message(image):
    largeur, hauteur = image.size
    donnees = image.load()

    message = ""
    index_message = 0

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = donnees[x, y]
            message += str(r & 1)
            message += str(g & 1)
            message += str(b & 1)
            index_message += 1

            if index_message >= 16 and message[-16:] == "1111111111111110":
                return ''.join(chr(int(message[i:i + 8], 2)) for i in range(0, len(message) - 16, 8))

    return None

cacher_message(image, message_binaire)

message_extraire = extraire_message(Image.open('image_cache.jpg'))
print('secret message', message_extraire)
