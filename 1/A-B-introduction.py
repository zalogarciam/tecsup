# def suma_enteros(arreglo):
#     suma = 0 
#     for num in arreglo:
#         suma += num
#     return suma

# print(suma_enteros([1,2,3,4,5])) # 5 = n

# # Complejidad de tiempo O(n) donde n es el numero de items que existen en el arreglo.
# # Complejidad de espacio O(1) 

# def suma_enteros(arreglo):
#     suma = 0 # O(1)
#     for num in arreglo:
#         suma += num
#     return suma

# print(suma_enteros([1,2,3,4,5,6,7,8,9,0])) # 10 = n
# # Complejidad de tiempo O(n)
# # Complejidad de espacio O(1) 

# def obtener_pares(n):
#     pares = []
#     for num in n:
#         if num % 2 == 0:
#             pares.append(num) # 2, 4, 6
#     return pares # [2,4,6,8, 10, 12]

# print(obtener_pares([1,2,3,4,5,6])) # 6 items
# print(obtener_pares([2,4,6,8, 10, 12])) # 6 items Peor de los casos

# # Complejidad de tiempo O(n)
# # Complejidad de espacio O(n) 

# def imprimir(n, m):
#     for i in range(n): # 0 al 4 ----> n = 5
#         for j in range(m): # 0 al 4 -----> n = 10
#             print(i, j) # 25 registros.
# imprimir(5, 10)
# # Complejidad de tiempo O(n^2)
# # Complejidad de espacio O(1) 

# Complejidad de tiempo O(n * m)

# def imprimir(n, m): # n =5 , m = 10
#     for i in range(n): # 5
#         for j in range(n, m): # 5 al 10
#             suma = i + j
#             print(suma)

# imprimir(3, 5)
# # Complejidad de tiempo O(n * (m - n ))
# # Complejidad de espacio O(1) 


# def imprimir(n):
#     for i in range(n):
#         for j in range(i + 1, n):
#             print(i, j)
# O(1 + 2 + 3 + ... + n) =  [(n * (n - 1)) / 2] = 5 * 6 / 2 = 15 = (n^2 - n) / 2 = n^2
# (n^2 - n) / 2 = n^2
# n = 1 000 000 ^ 2 - 1 000 000  / 2 = 1 000 000 000 000 000  - 1 000 000  / 2
# n^2 + n = n ^2

# # 1 + 2 +3 +4 +5 = 15   
# imprimir(5)   


# def imprimir(n):
#     for i in range(n):
#         for j in range(i + 1, n): # n ^ 2
#             for k in range(10000):  # n = 10000
#                  print(i, j, k)

# Complejidad de tiempo O(n^2*10000) = O(n^2) =
# n = 1 000 000 000 000 000 * 10000

# def imprimir(n):
#     for i in range(n):
#         for j in range(i + 1, n): # n ^ 2
#              print(i, j)
#     for i in range(9999): # 9999
#         print(i)

# Complejidad de tiempo O(n ^ 2 + 9999) = n ^ 2
# n = 1 000 000 000 000 000 + 9999

# n ^ 2 + n
# n = 1 000 000 000 000  + 1 000 000

# Analisis Asintotico
# O(1) O(1) O(1) O(1) O(n) O(1) O(1) O(1) O(1) ... = 0(1)