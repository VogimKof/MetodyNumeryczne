import numpy as np
import matplotlib.pyplot as plt

def interpolacja(x, X, Y):
    wynik = 0
    for i in range(len(X)):
        val = Y[i]
        for j in range(len(X)):
            if i != j:
                val *= (x - X[j])/(X[i]-X[j])
        wynik += val
    return wynik

X = np.linspace(-1, 1, 11)
Y = abs(X)

x = np.linspace(-1, 1, 1000)
plt.plot(X,Y,'o-')
plt.plot( x,interpolacja(x,X,Y))
plt.legend(["wezly"])
plt.show()
