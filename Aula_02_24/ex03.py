"""
- Gere uma imagem com quadrados verdes
- Pode utilizar a imagem entrada.jpg
- Não se esqueça de mostrar a imagem
"""

# Importação das bibliotecas
import cv2

image = cv2.imread('images/entrada.jpg')

for x in range(0, image.shape[1], 20):  # Percorre as linhas
    for y in range(0, image.shape[0], 20):  # Percorre as colunas
        for ax in range(0, 5, 1):
            for ay in range(0, 5, 1):
                image[y + ay, x + ax] = (0, 255, 0)

# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", image)
cv2.waitKey(0)  # espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("images/saida_ex03.jpg", image)
