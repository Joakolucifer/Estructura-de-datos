#declarar arreglo

m1=[[1,2,3],[4,5,6]]

print ("Matriz 1:",m1)

#para consultar elementos de la matriz
print("Segunda fila Matriz:",m1[1])
print("Tercer elemnto de la segunda fila:",m1[1][2])
print("Último elemento de la primera fila:",m1[0][-1])

#Consultando una columna
i= 1 #Columna que queremos obtener
columna= []
for fila in m1:
    columna.append(fila[i])
print("Segunda columna:",columna)    
filas= 2
Columnas = 2

for i in range(filas):
    for j in range(Columnas):
        m1[i][j]= int(input(f"Elemento({i+1},{j+1}):"))
for i in range(filas):
    for j in range(Columnas):
        print(m1[filas],[Columnas])        