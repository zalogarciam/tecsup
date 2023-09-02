# Complejidad de Tiempo: O(n) donde n es el numero de elementos del arreglo de entrada
# Complejidad de Espacio: O(1)

# def suma_enteros (arreglo):
#     suma = 0 # 0(1)
#     for num in arreglo :
#         suma += num
#     return suma

# print(suma_enteros([3,1,2,6,7])) # arreglo de n posiciones


# Complejidad de Tiempo: O(n) donde n es el numero de elementos del arreglo
# Complejidad de Espacio: O(n) donde n es el numero de elementos pares del arreglo

# Dado un arreglo de n elementos, devuelveme un arreglo de numeros de pares.
# def obtener_pares(arreglo):
#     pares = [] # O(n)
#     for num in arreglo:
#         if num % 2 == 0:
#             pares.append(num)
#     return pares

# print(obtener_pares([8,10,2,6,8])) # arreglo de n posiciones

# Crea una matriz de n * n, devuelveme la mitad de la matriz

# Complejidad de Tiempo: O(n) * O(n) = O(n^2)
# Complejidad de Espacio: O(1)

# def imprimir(n):
#     for i in range(n): # O(n)
#         for j in range(n): # O(n)
#             print(i, j)

# imprimir(4)

# Complejidad de Tiempo: O(n) * O(m-n) 
# Complejidad de Espacio: O(1)

# def imprimir(n, m):
#     for i in range(n): # O(n) 
#         for j in range(n, m): # O(m-n)
#             # suma = i + j
#             print(i ,j)

# imprimir(4,8)


# Complejidad de Tiempo: # n+(n -1)+(n-2)+(n-3)...+0 = n*(n -1)/2 = n^2 = O( n^2)
# Complejidad de Espacio: O(1)
def imprimir(n):
    for i in range(1, n + 1): # 
        for j in range(i + 1, n + 1):  
            print(i, j)
imprimir(4) # 4 * (4 - 1) / 2 = 12 / 2 = 6

# Complejidad de Tiempo: O(n^2) * 10000 = O(n^2)
# Complejidad de Espacio: O(1)

def imprimir(n):
    for i in range(n + 1): # O( n^2)
        for j in range(i + 1, n + 1):
            for k in range(10000): 
                 print(i, j, k)

# n = 1 000 000 000 = 1 000 000 000 000 000 000 0000


# Complejidad de Tiempo: O(n^2) + 9999 = O(n^2)
# Complejidad de Espacio: O(1)

def imprimir(n):
    for i in range(n + 1): # O( n^2)
        for j in range(i + 1, n + 1):
             print(i, j)
    for i in range(9999): 
        print(i)

# n = 1 000 000 000 = 1 000 000 000 000 000 000 + 9999 = 1 000 000 000 000 009 999

# Complejidad de tiempo: O(n^2 * m)
n = 10
m = 100
for i in range(n):
    for j in range (n):
        for k in range(m):
            print()

# Complejidad de tiempo: O(n^2 + m)
for i in range(n):
    for j in range (n):
        print()
for k in range(m):
    print()