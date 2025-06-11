import math
import numpy as np

h = 1.
wynik = ["krok", "h", "iloraz", "poch"]
for k in range(60):
    iloraz = (math.exp(10+h) - math.exp(10))/h
    zapis = [k, h, iloraz, math.exp(10)]
    wynik = np.vstack([wynik,zapis])
    h = h/2

print(wynik)

def heron(a, x, epsilon):

    test = 1000
    while test > epsilon:
        x1 = (x + a/x)/2
        test = x1 - x
        x = x1

    return x

print(heron(16,1274.53,0.00005))


