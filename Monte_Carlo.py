import random
import math 

def monte_carlo_integral(f, a, b, n):
    """
    Liczy przybliżenie całki oznaczonej funkcji f(x) w przedziale [a, b]
    metodą Monte Carlo, także gdy f(x) może przyjmować wartości ujemne.
    
    Parametry:
        f  - funkcja f(x)
        a  - początek przedziału
        b  - koniec przedziału
        n  - liczba losowanych punktów
    
    Zwraca:
        Przybliżenie całki oznaczonej ∫_a^b f(x) dx
    """
    # Przybliżenie min i max wartości f(x) na [a, b]
    sample_points = [a + (b - a) * i / 100 for i in range(101)]
    f_min = min(f(x) for x in sample_points)
    f_max = max(f(x) for x in sample_points)

    count_pos = 0
    count_neg = 0

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(f_min, f_max)
        fx = f(x)

        if y >= 0 and y <= fx:
            count_pos += 1
        elif y < 0 and y >= fx:
            count_neg += 1

    rect_area = (b - a) * (f_max - f_min)
    return (count_pos - count_neg) / n * rect_area

result = monte_carlo_integral(lambda x: math.sin(x), 0, math.pi, 100000)
print(f"Przybliżona całka: {result:.5f}")

def Monte_Carlo_pi(n):
    k = 0 
    for _ in range(n):
        x, y = random.random(), random.random()  
        if x*x + y*y <= 1:
            k += 1
    return 4 * k / n  


print(Monte_Carlo_pi(10000000))