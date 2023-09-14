matriz2 = [0,0,0,0]
# print(matriz2)
matriz = [0] * 4
# print(matriz)

matriz2d = [[0] * 4] *4
# print(matriz2d)

n = 4

# for i in range(n):
#     for j in range(n):
#         print('[',i,j, ']', end="")
#     print()

# matriz = [[0] * 4 for _ in range(n)]
# for fila in matriz:
#     print(fila)
# matriz[2][2] = 1
# print()
# for fila in matriz:
#     print(fila)
# print(matriz)

# Tiempo #O(n^3)
# Espacio #O(1) Tiempo constante

# for i in range(n): #O(n)
#     for j in range(n): #O(n)
#         for k in range(n): #O(n)
#             print(i,j,k)

# Tiempo #O(n)* O(n) = O(n^2)
# Espacio #O(1) Tiempo constante

# for i in range(n): #O(n)
#     for j in range(n): #O(n)
#         print(i,j,k)

# print([0] * n) # = [0, 0, 0, 0]
# matriz = [[0, 0, 0, 0] for _ in range(n)]
# = [0, 0, 0, 0]
# = [0, 0, 0, 0]
# = [0, 0, 0, 0]
# = [0, 0, 0, 0]

# matriz[0][0] = 1
# matriz[0][3] = 1
# matriz[1][1] = 1
# matriz[1][2] = 1
# matriz[2][1] = 1
# matriz[2][2] = 1
# matriz[3][0] = 1
# matriz[3][3] = 1
# for fila in matriz:
#     print(fila)

arreglo = [2 , 4, 10, 5, 15, 3]
# [2 , 4, 10, 5, 15, 3, _]
# [2 , 4, 10, 5, 15, 3, _]
# [2 , 4, 10, 5, 15, 3, 3]
# [2 , 4, 10, 5, 15, 15, 3]
# [2 , 4, 10, 5, 99, 15, 3]

# Insertame el 100 en la posicion 3
# [2 , 4, 10, 5, 99, 15, 3]
# [2 , 4, 10, 5, 99, 15, 3, _]
# [2 , 4, 10, 5, 99, 15, 3, 3]
# [2 , 4, 10, 5, 99, 15, 15, 3]
# [2 , 4, 10, 5, 99, 99, 15, 3]
# [2 , 4, 10, 5, 5, 99, 15, 3]
# [2 , 4, 10, 100, 5, 99, 15, 3]

# Tiempo O(n)
# Peor de los casos: # Insertame el X en la posicion 0
# [2 , 4, 10, 100, 5, 99, 15, 3]
# [X, 2 , 4, 10, 100, 5, 99, 15, 3]

# print(arreglo)
arreglo.append(7) # Tiempo O(1) ... arreglo[contador+1] = 7 # inserta al final
# # for .... 7 Erroneo!
# # CONTADOR +=1 + 1 + 1 + 1 = len(array)
# print(len(arreglo)) # for i in range(arreglo) contador +=1 O(n)

# print(arreglo)
arreglo.insert(4, 99) # Tiempo O(1)  # inserta en la pos 4
# print(arreglo)
# arreglo.remove(4) # Tiempo O(n) - porque tengo que buscar el elemento... peor de los casos n veces 
# print(arreglo)
# print(arreglo[5]) # Tiempo O(1) 


arreglo = [2 , 4, 10, 100, 5, 99, 15, 3]
n = 0
def busqueda_lineal(n):
    for numero in arreglo:
        if numero == n:
            print("Numero Encontrado")
            return
    print("Numero no encontrado")

busqueda_lineal(n)