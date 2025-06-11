
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import pchip_interpolate
import matplotlib.pyplot as plt

# TWORZE 7 WEZLOW INTERPOLACYJNYCH ROWNOODLEGLYCH
x = np.linspace(0, 2, 7)
# DZIEKI MNOZENIU PRZEZ PI - WEZLY W ZAKRESIE (0,2*PI)
x = x*np.pi
# INTERPOLUJEMY FUNKCJE SIN(X)
y = np.sin(x)

# DLA TYCH WARTOSCI X WYLICZAMY WARTOSCI FUNKCJI INTERPOLACYJNYCH
# TEN SAM OCZYWISCIE ZAKRES ALE WIEKSZA GESTOSC PO TO BY UZYSKAC 
# LADNE WYKRESY FUNKCJI INTERPOLACYJNYCH
x2 = np.linspace(0, 2, 1000)
x2 = x2*np.pi

# FUNKCJE SCHODKOWE = METODA NAJBLIZSZEGO PUNKTU
# DLA KAZDEJ WARTOSCI X ZNAJDOWANA JEST NAJBLIZSZA WARTOSC WEZLA 
# I PRZYPISANA WARTOSC Y Z TEGO WEZLA - STAD SCHODKI

f_1 = interp1d(x, y, kind='nearest')

plt.plot(x, y, 'o')
plt.plot(x2,f_1(x2),'-')
plt.legend(['wezly', 'najblizszy'], loc='best')
plt.show()

# UWAGA - W PODOBNY SPOSOB BEDZIEMY WYLICZALI CALKI METODA PROSTOKATOW
# PAMIETAJAC, ŻE CALKA TO POLE POWIERZCHNI POD WYKRESEM FUNKCJI
# PYTHON POZWALA ROWNIEZ ODSZUKIWAC NAJBLIZSZY WCZESNIEJSZY LUB NASTEPNY WEZEL

f_2 = interp1d(x, y, kind='previous')
f_3 = interp1d(x, y, kind='next')

plt.plot(x, y, 'o')

plt.plot(x2,f_1(x2),'-',x2,f_2(x2),'--',x2,f_3(x2),':')
plt.legend(['wezly', 'najblizszy', 'poprzedni', 'nastepny'], loc='best')
plt.show()

# FUNKCJE SKLEJANE - SPLINE

# PIERWSZY PRZYKLAD INTERPOLACJI SKLEJANEJ - PROSTA LAMANA
# MIEDZY KAZDA PARA WEZLOW WYZNACZONY JEST INNY WIELOMIAN 1-G0 STOPNIA
# CZYLI PROSTA (TU ODCINEK LACZACY WEZLY)

f_1 = interp1d(x, y, kind='slinear')
# UWAGA - KOMENDA interp1d TWORZY NA PODSTAWIE WEZLOW x, y FUNKCJE, TU f_1()

plt.plot(x, y, 'o', x2, np.sin(x2))
plt.plot(x2,f_1(x2),'-')
plt.legend(['wezly', 'sin(x)', 'liniowy'], loc='best')
plt.show()

# DODAJEMY KOLEJNE METODY SKLEJANE:
# WIELOMIANY KWADRATOWE (2-GO STOPNIA)
f_2 = interp1d(x, y, kind='quadratic')
# WIELOMIANY SZESCIENNE (3-GO STOPNIA) = SPLAJNY NATURALNE (PATRZ WYKLAD)
f_3 = interp1d(x, y, kind='cubic')

# DODAJEMY INTERPOLACJE SKLEJANA HERMITE'A - WIELOMIANY 3-GO STOPNIA
# BEZ ZALOZENIA ROWNOSCI (CZYLI CIAGLOSCI) 2 POCHODNEJ W WEZLACH
# Piecewise Cubic Hermite Interpolating Polynomial 
f_4 = pchip_interpolate(x,y,x2)
# UWAGA - TA KOMENDA NIE TWORZY FUNKCJI, TYLKO WYLICZA WARTOSCI FUNKCJI 
# INTERPOLACYJNEJ W WEZLACH

plt.plot(x, y, 'o', x2,np.sin(x2))

plt.plot(x2,f_1(x2),'-',x2,f_2(x2),'--',x2,f_3(x2),':',x2,f_4,'-')
plt.legend(['wezly', 'sin(x)', 'liniowy', 'kwadratowy', 'cubic', 'pchip'], loc='best')
plt.show()

# WYKRES TYLKO WIELOMIANOW 3-GO STOPNIA 

plt.plot(x, y, 'o', x2,np.sin(x2))

plt.plot(x2,f_3(x2),':',x2,f_4,'-')
plt.legend(['wezly', 'sin(x)', 'naturalny', 'Hermite'], loc='best')
plt.show()

# BŁĄD BEZWZGLĘDNY METOD SPLINE

err_1 = abs(f_1(x2) - np.sin(x2))
err_2 = abs(f_2(x2) - np.sin(x2))
err_3 = abs(f_3(x2) - np.sin(x2))
err_4 = abs(pchip_interpolate(x,y,x2) - np.sin(x2))

plt.plot(x2,err_1,'-',x2,err_2,'--',x2,err_3,':',x2,err_4,'-')
plt.legend(['liniowy', 'kwadratowy', 'cubic', 'pchip'], loc='best')
plt.show()

# TYLKO WIELOMIANY 3-CIEGO STOPNIA - zachowanie koło maksimum

x2 = np.linspace(0, 1, 500)
x2 = x2*np.pi

f_4 = pchip_interpolate(x,y,x2)

plt.plot(x[1:4], y[1:4], 'o', x2,np.sin(x2),':')

plt.plot(x2,f_3(x2),'-.',x2,f_4,'-')
#plt.legend(['wezly', 'sin(x)', 'cubic', 'pchip'], loc='best')
plt.legend(['wezly', 'sin(x)', 'naturalny', 'Hermite'], loc='best')
plt.show()



# TYLKO WIELOMIANY 3-CIEGO STOPNIA - zachowanie dla funkcji płaskiej
# METODA PCHIP "ZACHOWUJE KSZTAŁT" WEZLOW - NIE DODAJE MAKSIMÓW I MINIMÓW
# MIEDZY NIMI

x = np.linspace(-3, 3, 7)
y = [-1, -1, -1, 0, 1, 1, 1]

x2 = np.linspace(-3, 3, 1000)
                 
f_3 = interp1d(x, y, kind='cubic')
f_4 = pchip_interpolate(x,y,x2)

plt.plot(x,y,'o',x2,f_3(x2),'-',x2,f_4,'-.')
#plt.legend(['wezly','cubic','pchip'], loc='best')
plt.legend(['wezly','naturalny','Hermite'], loc='best')
plt.show()

