
# Ejercicio 3: La bandera de Dijkstra.

import random
from colorama import Fore

# Variables de color.
R = Fore.RED 
V = Fore.GREEN
A = Fore.BLUE
B = Fore.WHITE

# Lista para cada color.
rojo = []
verde = []
azul = []
blanco = []

# Función para ordenar la bandera.
def ordenar_bandera(bandera):
    for i in bandera:
        if i == R:
            rojo.append(i)
        if i == V:
            verde.appemd(i)
        if i == A:
            azul.append(i)
        if i == B:
            blanco.append(i)
    
    bandera_ordenada = rojo + verde + blanco + azul
    print(bandera_ordenada)

# Función por si quieres crear la bandera manualmente.
def crear_bandera_manualmente():
    lista_colores = input("Ingrese los colores separados por comas (R = rojo, V = verde, A = azul y B = casilla en blanco): ")
    bandera = lista_colores.split(",")
    ordenar_bandera(bandera)

# Función por si quieres crear la bandera aleatoriamente.
def crear_bandera_random():
    bandera = []
    for i in range(random.randint(14, 23)):
        random = random.randint(1, 4)
        if random == 1:
            bandera.append("R")
        if random == 2:
            bandera.append("V")
        if random == 3:
            bandera.append("A")
        if random == 4:
            bandera.append("B")
    
    ordenar_bandera(bandera)

# Función para reordenar la bandera.
def printear_bandera():
    que_quieres = input("¿Quieres crear tu la bandera (1) o deseas que se cree aleatoriamente (2)? ")
    if que_quieres == 1:
        crear_bandera_manualmente()
    elif que_quieres == 2:
        crear_bandera_random()


printear_bandera()



        



