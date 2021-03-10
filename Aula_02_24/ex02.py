"""
- Faça uma escala de azul
- Pode utilizar a imagem entrada.jpg
- Não se esqueça de mostrar a imagem
"""

# Importação das bibliotecas
import cv2

image = cv2.imread('images/entrada.jpg')

for b in range(0, 255, 1):  # percorre as linhas
    for g in range(0, 255, 10):  # percorre as colunas
        for r in range(0, 255, 10):  # percorre as colunas
            image[b + 65, int(25 * g / 10 + r / 10)] = b, g, r

# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", image)
cv2.waitKey(0)  # espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("images/saida_ex02.jpg", image)
