from PIL import Image
image = Image.open('/home/yassg4mer/Project/SAFM/ch/image_cachee.png')
def extraire_message(image):
    largeur, hauteur = image.size
    donnees = image.load()
    message = ""
    
    index_message = 0

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = donnees[x, y]
            message += str(r & 1)
            index_message += 1

            if index_message % 9 == 0 and message[-16:] == "1111111111111110":
                return ''.join(chr(int(message[i:i + 8], 2)) for i in range(0, len(message) - 16, 8))

    return None

# Extraire le message de l'image
message_extrait = extraire_message(Image.open("/home/yassg4mer/Project/SAFM/ch/image_cachee.png"))
print("Message extrait :", message_extrait)