"""
Exemplo 2. Reconhecimento de formas
"""

# Importação das bibliotecas
import cv2
# Leitura da image com a função imread()
image = cv2.imread('images/vermelho.jpg')
print('Largura em pixels: ', image.shape [1]) #largura da image
print('Altura em pixels: ', image.shape [0]) #altura da image
print ('Qtde de canais: ', image.shape [2])

xi=image.shape[1]
xf=0
yi= image.shape[0]
yf=0

for y in range(0, yi, 1): #percorre as linhas
    for x in range(0,xi, 1): #percorre as colunas
        (b, g, r) = image[y, x]
        if((b==0)&(g==0)&(r>220)):
            if(x<xi): 
                xi=x
            if(x>xf): 
                xf=x
            if(y<yi): 
                yi=y
            if(y>yf): 
                yf=y

print('xi= ',xi , 'xf= ',xf)
print('yi = ',yi , 'yf =',yf)
cv2.waitKey(0) #espera pressionar qualquer tecla