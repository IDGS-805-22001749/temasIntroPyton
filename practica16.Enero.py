#Practica 16 de Enero, calcular la distancia 


import math

def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia


x1 = float(input("Ingresa la coordenada x del punto 1: "))
y1 = float(input("Ingresa la coordenada y del punto 1: "))
x2 = float(input("Ingresa la coordenada x del punto 2: "))
y2 = float(input("Ingresa la coordenada y del punto 2: "))

distancia = calcular_distancia(x1, y1, x2, y2)
print(f"La distancia entre los puntos es: {distancia}")
