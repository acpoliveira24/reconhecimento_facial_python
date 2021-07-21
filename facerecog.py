import cv2


# Carrega o modelo necessário para o reconhecimento facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Carrega a imagem selecionada (coloque o nome e o tipo da imagem que vai usar)
img = cv2.imread('pessoas.jpg')

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta os rostos na imagem
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Desenha um retângulo nos rostos detectados
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Mostra o resultado em uma nova janela
cv2.imshow('img', img)
cv2.waitKey()

# Salva a imagem com o retângulo nos rostos (se preferir, troque o nome do arquivo e da extensão para .png)
cv2.imwrite('img.png', img)
