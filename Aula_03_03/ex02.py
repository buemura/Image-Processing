import cv2

image = cv2.imread('images/entrada.jpg')

vertical_size = image.shape[0]
horizontal_size = image.shape[1]

def change_colors():
    for x in range(0, horizontal_size, 1):
        for y in range(0, vertical_size, 1):
            (b, g, r) = image[y, x]
            if b>=240 and g>=240 and r>=240:
                image[y, x] = (0, 0, 0)
            elif b<=20 and g<=20 and r<=20:
                image[y, x] = (255, 255, 255)


def save_image():
    cv2.imshow("Imagem alterada",image)
    cv2.imwrite("images/saida_ex02.jpg",image)
    cv2.waitKey(0)


change_colors()
save_image()
