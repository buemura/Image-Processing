import cv2

image = cv2.imread('images/entrada.jpg')

vertical_size = image.shape[0]
horizontal_size = image.shape[1]


def create_lines():
    # Horizontal Lines
    image[20:40, 20:horizontal_size - 20] = (255, 0, 0)
    image[vertical_size - 40:vertical_size - 20, 20:image.shape[1] - 20] = (255, 0, 0)
    # Vertical Lines
    image[20:vertical_size - 20, 20:40] = (255, 0, 0)
    image[20:vertical_size - 20, horizontal_size - 40:horizontal_size - 20] = (255, 0, 0)


def write_name():
    cv2.putText(image, "Bruno Uemura", (320, 560), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)


def change_colors():
    for x in range(0, horizontal_size, 1):
        for y in range(0, vertical_size, 1):
            (b, g, r) = image[y, x]
            if b >= 240 and g >= 240 and r >= 240:
                image[y, x] = (0, 200, 0)
            elif b == 0 and g == 0 and r == 0:
                image[y, x] = (0, 50, 0)


def save_image():
    cv2.imshow("Imagem alterada", image)
    cv2.imwrite("images/saida_ex01.jpg", image)
    cv2.waitKey(0)


create_lines()
write_name()
change_colors()
save_image()
