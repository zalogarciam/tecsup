arreglo = [1,2,3,4]
n = 4
matriz = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]

# n = 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# print(matriz)
# matriz[3][3] = 9


#Willian
matriz[0][0] = 9
matriz[0][3] = 9
matriz[1][1] = 9
matriz[1][2] = 9
matriz[2][1] = 9
matriz[2][2] = 9
matriz[3][0] = 9
matriz[3][3] = 9

# Tiempo n^2
# Espacio 1
# for fila in range(n): # n
#     for columna in range(n): #  O(n^2)
#         print(fila, columna)

# Tiempo n^3
# Espacio 1
# for fila in range(n):
#     for columna in range(n):
#         for profundidad in range(n):
#             print(fila , columna , profundidad)

# Kevin
# matriz = [[1, 2, 3, 4],
#           [1, 2, 3, 4],
#           [1, 2, 3, 4],
#           [1, 2, 3, 4]]
# cambios = [(0, 0), (0, 3), (1, 1), (1, 2), (2, 1), (2, 2), (3, 0), (3, 3)]
# for i, j in cambios:
#     matriz[i][j] = 9
# for fila in matriz:
#     print(fila)

# Operaciones

arreglo = [2 , 4, 10, 5, 15, 3, 15]
# int[] arreglo = new int[10]  Tamano fijo

# print(arreglo)
# arreglo.append(99) # Tiempo O(1)
# print(arreglo)
# arreglo.insert(3, 100) # Tiempo O(n)
# print(arreglo)
# arreglo.remove(15) # Tiempo O(n)
# print(arreglo)
# print(arreglo.index(99)) # Tiempo O(n)

print(arreglo[4]) # O(1)

# element_buscar = 101 
# def buscar_elemento(element_buscar):
#     for item in arreglo:
#         if item == element_buscar:
#             print("Numero encontrado")
#             return
#     print("Numero no encontrado")
# buscar_elemento(element_buscar)