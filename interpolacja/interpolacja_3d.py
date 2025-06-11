
import numpy as np

from scipy.interpolate import RectBivariateSpline
import matplotlib.pyplot as plt

# tworzymy punkty na osiach x i y
x = np.arange(-6, 6, 1.5)
y = np.arange(-6, 6, 1.5)

# tworzymy siatkę punktów na płaszczyźnie xy
X, Y = np.meshgrid(x, y)
# ta siatka to wartosci wezlow na plaszczyznie

plt.plot(X, Y, 'o')

# wyliczamy Z dla każdego punktu siatki
Z = np.sin(np.sqrt(X**2+Y**2))
# teraz mamy zestaw wezlow, kazdy postaci (x,y,z)

fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,rstride=1, cstride=1,
                cmap='spring', edgecolor='none')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# ustawienie kata, pod ktorym ogladamy plaszczyzne
ax.view_init(60, 35)

plt.show()

# INTERPOLACJA


# UWAGA - KOMENDA interp2d WYMAGA WEKTOROW x, y ALE JUZ WARTOSCI Z WYLICZONYCH
# NA SIATCE KARTEZJANSKIEJ
# PONOWNIE TWORZY FUNKCJE f()
#f = interp2d(x, y, Z, kind='linear')
f = RectBivariateSpline(x, y, Z, kx=3, ky=3)

# OCZYWISIE, MOZEMY KORZYSTAC Z INNYCH METOD, JAK DLA INTERPOLACJI 1-d:
# 'nearest','quadratic','cubic'

# TU TWORZYMY SIATKE PUNKTOW DLA KTORYCH WYLICZYMY WARTOSCI FUNKCJI INTERPOLUJACEJ
# DLATEGO ZNOW WEKTORY xx i yy SA GESTSZE NIZ WEKTORY WEZLOW x i y
xx = np.arange(-6, 6, 0.1)
yy = np.arange(-6, 6, 0.1)

XX, YY = np.meshgrid(xx, yy)

ZZ = f(xx, yy)

fig2 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ,rstride=1, cstride=1,
                cmap='bone', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(60, 35)

plt.show()