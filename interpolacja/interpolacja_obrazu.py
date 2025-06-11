
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

from PIL import Image

# KONWERSJA ZDJECIA DO TABELI

# wczytujemy obraz z pliku
im = Image.open('Banach.jpg') 
# konwersja do szarej skali kolorów (greyscale)
im = np.array(im.convert('L'))

# pierwotne zdjecie
plt.imshow(im, cmap=plt.get_cmap('Greys_r'))

# odczytujemy liczbę wierszy i kolumn piksli obrazu
nx, ny = im.shape[1], im.shape[0]
# tworzymy siatke kartezjanska wielkosci obrazu - kazdy punkt
# odpowiada pikslowi obrazu
X, Y = np.meshgrid(np.arange(0, nx, 1), np.arange(0, ny, 1))

# PROBKUJEMY OBRAZ
# liczba probek piksli z obrazu
nprobek = 1000

# losujemy "nprobek" piksli z obrazu
ix = np.random.randint(im.shape[1], size=nprobek)
iy = np.random.randint(im.shape[0], size=nprobek)
# pobieram wartosci wylosowanych piksli
probki = im[iy,ix]

# ODTWARZAMY OBRAZ KORZYSTAJAC Z INTERPOLACJI

# tworze obraz interpolowany na podstawie wylosowanych piksli
# metody do zastosowania: #linear, #nearest, #cubic
int_im = griddata((iy, ix), probki, (Y, X), method='cubic')

plt.imshow(int_im, cmap=plt.get_cmap('Greys_r'))


