import math

def Prostokąty(a, b, n ):

    h = (b-a)/n
    P = 0
    x = a

    while x <= b:

        P += h*math.sin(x)
        x += h

    return P

print(Prostokąty(0, math.pi, 10000))

def Trapezy(a,b,n):

    h = (b - a) / n
    P = 0
    x = a
    x_next = x+h

    while x_next <= b:

        P += 0.5*h*(math.sin(x) + math.sin(x_next))

        x= x_next
        x_next += h

    return P

print(Trapezy(0, math.pi, 10000))

def Simpson(a, b, n):
    h = (b - a) / n
    P = 0
    x = a

    while x <= b:
        x_next = x +h
        #pod warunkiem że bierzemy środek przedziału
        P += h/6 * (math.sin(x) + 4*math.sin((x + x_next)/2) + math.sin(x_next))
        x +=h

    return P

print(Simpson(0,math.pi,10000))