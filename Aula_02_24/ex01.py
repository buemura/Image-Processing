"""
- Crie a seguinte imagem (pode usaro paint)
- Leia um pixel vermelho, um verde, um azul, 
  um amarelo e um preto. E informe seus 
  valores em RGB
"""

# Importação das bibliotecas
import cv2

image = cv2.imread('images/cores.jpg')


def checkColor(x, y):
    (blue, green, red) = image[y, x]  # veja que a ordem BGR e não RGB
    print(f'The pixel ({x}, {y}) has the following color')
    print('Red:', red, 'Green:', green, 'Blue:', blue)


checkColor(400, 100)
checkColor(400, 200)
checkColor(400, 300)
checkColor(400, 400)
checkColor(400, 500)
