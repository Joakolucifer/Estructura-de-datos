import random

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m1=[[random.randint(0,5) for j in range(columnas) for i in range(filas)]]
m2=[[random.randint(0,5) for j in range(columnas) for i in range(filas)]]
for i in range (filas):
    for j in range (columnas):
         print(m1[i][j])
for i in range (filas):
    for j in range (columnas):
        m2=[[random.randint(0,5) for j in range(columnas) for i in range(filas)]]

ms= m1 + m2
  

for i in range (filas):
    for j in range (columnas):
        m3=[[random.randint(0,5) for j in range(columnas) for i in range(filas)]]

mf= ms- m3 
