# 🧑 Reconhecimento Facial

Código em Python para reconhecimento de rostos em fotos com a biblioteca `opencv-python`. Após rodar o código, o resultado será a imagem em uma nova janela com um retângulo desenhado em volta dos rostos e um novo arquivo de imagem gerado.

## Instruções

Instale a biblioteca através de `pip install opencv-python`.

Clone o repositório e abra o arquivo `facerecog.py`. O repositório já contém uma imagem de exemplo para ser usadas como teste. Se for usar outra imagem, coloque o nome e a extensão correspondentes no lugar de `pessoas.jpg`.

:rotating_light: Atenção: se sua imagem não estiver na mesma pasta do repositório, é necessário colocar o caminho completo do arquivo.

Na linha `cv2.imwrite('img.png', img)` é possível também trocar o nome do arquivo que será gerado assim como a extensão também pode ser *.png*.

Em seguida, apenas execute o código. A imagem com os rostos detectados com um retângulo será aberta e também um novo arquivo de imagem com o nome e formato escolhidos será gerado.