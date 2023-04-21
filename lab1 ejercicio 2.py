import random

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
e = int(input("Ingrese un escalar: "))
m1=[[random.randint(0,5) for j in range(columnas) for i in range(filas)]]

mm =  m1*e

