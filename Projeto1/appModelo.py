"""
Encontrar 4 imagens de placa de carros

Montar um programa que comande uma cancela.

- 2 placas estão cadastradas. Reconhecer e escrever "Entrada Liberada".
- 2 placas não estão cadastradas. Reconhecer e escrever "Entrada não Liberada"

Compartilhar tela ou gravar um video de 3 minutos.
"""
import cv2

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

image1 = cv2.imread('images/placa1.jpg')
print("Altura (height): %d pixels" % (image1.shape[0]))
print("Largura (width): %d pixels" % (image1.shape[1]))
print("Canais (channels): %d" % (image1.shape[2]))

cv2.imshow('Original', image1)
print('Original')
a = (pytesseract.image_to_string(Image.open('images/placa1.jpg')))
print('Reconhecido: ', a)
print();

print('Final sem tratatmento')
custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
a = (pytesseract.image_to_string('images/placa1.jpg', config=custom_config))
print('Reconhecido: ', a)
print();

##### Tratamento da imagem ######
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
thresh = thresholding(image1)
cv2.imshow('Thresh', image1)

print('Final com tratatmento')
custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
a = (pytesseract.image_to_string(thresh, config=custom_config))
print('Reconhecido: ', a)

cv2.waitKey(0)