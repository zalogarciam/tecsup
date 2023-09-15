# Ejercicio 1
# Tiempo O(n)
# Espacio O(1)
# lista = [1,2,3,4,5]
# suma = 0

# for item in lista:
#     suma += item
# print(suma)

# Ejercicio 6
# Tiempo y Espacio O(n)
# lista = [1,2,3,4,4,5]

# nueva_lista = []

# for numero in lista:
#     if numero not in nueva_lista:
#         nueva_lista.append(numero)
# print(nueva_lista)

# Ejercicio 7

# 1 5 5
# 2 5 10
# 3 5 15
# 4 5 20
# 5 5 25

# Tiempo 3n = n
# Espacio 3n
# n = 5
# matriz = [[0] * 3 for _ in range(n)]
# # print(matriz)
# for item in matriz:
#     print(item)

# for fila in range(n):
#     for columna in range(3):
#         if columna == 0:
#             matriz[fila][columna] = fila + 1
#         if columna == 1:
#             matriz[fila][columna] = n
#         if columna == 2:
#             matriz[fila][columna] = (fila + 1) * n

# for item in matriz:
#     print(item)

# Ejercico 8
# [abc, abcd, abcde, ab, abcedef, aaaaaaaaaa]
# Ejercicio 9

# matriz1 = [[1,2,3,4],[4,5,6,7],[8,9,10,11]]
# matriz2 = [[1,2,3,4],[4,5,6,7],[8,9,10,11]]
# # matriz = [[2, 4, 6, 8] [8, 10, 12, 14] [16, 18,20, 22]]

# matriz = [[0] * 4 for _ in range(3)]
# print(matriz)
# for fila in range(3):
#     for columna in range(4):
#         matriz[fila][columna] = matriz1[fila][columna] + matriz2[fila][columna]

# print(matriz)

# Array

class Array:
    def __init__(self, capacidad) -> None:
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.contador = 0

    def print_array(self):
        for item in self.items:
            print('[', item, ']', end="") 
        print()

    def insert(self, valor):
        if self.longitud() == self.capacidad: # O(n)
            self.capacidad = self.capacidad * 2
            items_dinamico = [None] * self.capacidad
            for i in range (self.capacidad // 2):
                items_dinamico[i] = self.items[i]
            self.items = items_dinamico
        self.items[self.contador] = valor # O(1)
        self.contador += 1

    def delete(self, valor):
        for i in range(self.longitud()):
            if self.items[i] == valor:
                self.items[i] = None
                break

    def indice(self, valor):
        index = 0
        for i in range(self.longitud()):
             if self.items[i] == valor:
                break
             index +=1
        return index

    def longitud(self):
        return self.contador

    # def longitud_error(self):
    #     contador = 0
    #     for item in self.items:
    #         contador +=1
    #     return contador

arreglo = Array(5)
# arreglo.print_array()
arreglo.insert(7)
arreglo.insert(10)
arreglo.insert(3)
arreglo.insert(4)
arreglo.insert(1)
arreglo.insert(0)
# arreglo.print_array()
# arreglo.delete(10)
# arreglo.print_array()
# print(arreglo.longitud())
# print(arreglo.indice(3))

