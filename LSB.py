from PIL import Image

def encode_lsb(original_image_path, secret_image_path, password):
    # Charger les images
    original_image = Image.open(original_image_path)
    secret_image = Image.open(secret_image_path)

    # S'assurer que les images ont la même taille
    secret_image = secret_image.resize(original_image.size)

    # Convertir les images en mode RVB (Red, Green, Blue)
    original_image = original_image.convert('RGB')
    secret_image = secret_image.convert('RGB')

    # Créer un objet d'image résultant
    encoded_image = Image.new('RGB', original_image.size)

    # Parcourir chaque pixel des deux images
    for x in range(original_image.width):
        for y in range(original_image.height):
            # Récupérer les composants RVB des deux images
            original_pixel = list(original_image.getpixel((x, y)))
            secret_pixel = list(secret_image.getpixel((x, y)))

            # Cacher l'image secrète dans les bits de poids faible (LSB)
            for i in range(3):  # Pour chaque composant RVB
                original_pixel[i] = (original_pixel[i] & 0xFE) | ((secret_pixel[i] >> 7) & 0x01)

            # Définir le pixel modifié dans l'image résultante
            encoded_image.putpixel((x, y), tuple(original_pixel))

    # Sauvegarder l'image encodée
    encoded_image.save('encoded_image.png')

def decode_lsb(encoded_image_path, password):
    # Charger l'image encodée
    encoded_image = Image.open(encoded_image_path)

    # Créer un objet d'image résultant
    decoded_image = Image.new('RGB', encoded_image.size)

    # Parcourir chaque pixel de l'image encodée
    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            # Récupérer le composant RVB du pixel encodé
            encoded_pixel = list(encoded_image.getpixel((x, y)))

            # Extraire l'image secrète des bits de poids faible (LSB)
            for i in range(3):  # Pour chaque composant RVB
                encoded_pixel[i] = (encoded_pixel[i] & 0x01) << 7

            # Définir le pixel modifié dans l'image résultante
            decoded_image.putpixel((x, y), tuple(encoded_pixel))

    # Sauvegarder l'image décodée
    decoded_image.save('decoded_image.png')

def encode_lsb2(original_image_path, secret_image_path, password):
    # Charger les images
    original_image = Image.open(original_image_path)
    secret_image = Image.open(secret_image_path)

    # S'assurer que les images ont la même taille
    secret_image = secret_image.resize(original_image.size)

    # Convertir les images en mode RVB (Red, Green, Blue)
    original_image = original_image.convert('RGB')
    secret_image = secret_image.convert('RGB')

    # Créer un objet d'image résultant
    encoded_image = Image.new('RGB', original_image.size)

    # Parcourir chaque pixel des deux images
    for x in range(original_image.width):
        for y in range(original_image.height):
            # Récupérer les composants RVB des deux images
            original_pixel = list(original_image.getpixel((x, y)))
            secret_pixel = list(secret_image.getpixel((x, y)))

            # Cacher l'image secrète dans les bits de poids faible (LSB2)
            for i in range(3):  # Pour chaque composant RVB
                original_pixel[i] = (original_pixel[i] & 0xFC) | ((secret_pixel[i] >> 6) & 0x03)

            # Définir le pixel modifié dans l'image résultante
            encoded_image.putpixel((x, y), tuple(original_pixel))

    # Sauvegarder l'image encodée
    encoded_image.save('encoded_image_lsb2.png')

def decode_lsb2(encoded_image_path, password):
    # Charger l'image encodée
    encoded_image = Image.open(encoded_image_path)

    # Créer un objet d'image résultant
    decoded_image = Image.new('RGB', encoded_image.size)

    # Parcourir chaque pixel de l'image encodée
    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            # Récupérer le composant RVB du pixel encodé
            encoded_pixel = list(encoded_image.getpixel((x, y)))

            # Extraire l'image secrète des bits de poids faible (LSB2)
            for i in range(3):  # Pour chaque composant RVB
                encoded_pixel[i] = (encoded_pixel[i] & 0x03) << 6

            # Définir le pixel modifié dans l'image résultante
            decoded_image.putpixel((x, y), tuple(encoded_pixel))

    # Sauvegarder l'image décodée
    decoded_image.save('decoded_image_lsb2.png')

def encode_lsb3(original_image_path, secret_image_path, password):
    # Charger les images
    original_image = Image.open(original_image_path)
    secret_image = Image.open(secret_image_path)

    # S'assurer que les images ont la même taille
    secret_image = secret_image.resize(original_image.size)

    # Convertir les images en mode RVB (Red, Green, Blue)
    original_image = original_image.convert('RGB')
    secret_image = secret_image.convert('RGB')

    # Créer un objet d'image résultant
    encoded_image = Image.new('RGB', original_image.size)

    # Parcourir chaque pixel des deux images
    for x in range(original_image.width):
        for y in range(original_image.height):
            # Récupérer les composants RVB des deux images
            original_pixel = list(original_image.getpixel((x, y)))
            secret_pixel = list(secret_image.getpixel((x, y)))

            # Cacher l'image secrète dans les bits de poids faible (LSB3)
            for i in range(3):  # Pour chaque composant RVB
                original_pixel[i] = (original_pixel[i] & 0xF8) | ((secret_pixel[i] >> 5) & 0x07)

            # Définir le pixel modifié dans l'image résultante
            encoded_image.putpixel((x, y), tuple(original_pixel))

    # Sauvegarder l'image encodée
    encoded_image.save('encoded_image_lsb3.png')

def decode_lsb3(encoded_image_path, password):
    # Charger l'image encodée
    encoded_image = Image.open(encoded_image_path)

    # Créer un objet d'image résultant
    decoded_image = Image.new('RGB', encoded_image.size)

    # Parcourir chaque pixel de l'image encodée
    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            # Récupérer le composant RVB du pixel encodé
            encoded_pixel = list(encoded_image.getpixel((x, y)))

            # Extraire l'image secrète des bits de poids faible (LSB3)
            for i in range(3):  # Pour chaque composant RVB
                encoded_pixel[i] = (encoded_pixel[i] & 0x07) << 5

            # Définir le pixel modifié dans l'image résultante
            decoded_image.putpixel((x, y), tuple(encoded_pixel))

    # Sauvegarder l'image décodée
    decoded_image.save('decoded_image_lsb3.png')

# Exemple d'utilisation
encode_lsb('/home/yassg4mer/Project/SAFM/images bmp/lena.bmp', '/home/yassg4mer/Project/SAFM/images bmp/user.bmp', 'password')
decode_lsb('encoded_image.png', 'password')

encode_lsb2('/home/yassg4mer/Project/SAFM/images bmp/lena.bmp', '/home/yassg4mer/Project/SAFM/images bmp/user.bmp', 'password')
decode_lsb2('encoded_image_lsb2.png', 'password')

encode_lsb3('/home/yassg4mer/Project/SAFM/images bmp/lena.bmp', '/home/yassg4mer/Project/SAFM/images bmp/user.bmp', 'password')
decode_lsb3('encoded_image_lsb3.png', 'password')

