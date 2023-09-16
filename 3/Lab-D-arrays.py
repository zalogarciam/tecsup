# Ejercicio 1

# Tiempo O(n)
lista = [1,2,3,4,5]

suma = 0
for elemento in lista:
    suma += elemento

# print(suma)

# Ejercicio 3

#

# Ejercicio 6

# lista = [1,2,3,4,5,5,5,6,7,7]
# lista [1,2,3,4,5,6,7] 


# Tiempo O(n)
lista_2 = [] # Espacio O(n)
for item in lista:
    if item not in lista_2:
        lista_2.append(item)

# print(lista_2)

# Ejercicio 7

# 1 5 5
# 2 5 10
# 3 5 15
# 4 5 20
# 5 5 25

# Tiempo O(3n) = O(n)
# Espacio O(3n)
# n = 100
# matriz = [[0] * 3 for _ in range(n)]
# print(matriz)
# for fila in range(n):
#     for columna in range(3):
#         if columna == 0:
#             matriz[fila][columna] = fila + 1
#         if columna == 1:
#             matriz[fila][columna] = n
#         if columna == 2:
#             matriz[fila][columna] = (fila + 1) * n
   
# for fila in matriz:
#     print(fila)


# Ejercicio 8

# [abcd, av, bac, acasd, asqwesd]
# return asqwesd

# lista = ["abcd", "av", "bac", "acasd", "asqwesd"]
# # O(n) donde n es el numero de palabras del arreglo/lista
# mayor = None
# longitud = -999999999
# for item in lista:
#     if len(item) > longitud:
#         longitud = len(item)
#         mayor = item
# print(mayor) 

# Ejercicio 9

# 1 2 3 4   1 1 1 1     2 3 4 5
# 1 2 3 4   2 1 1 1 =   3 3 4 5
# 1 2 3 4   1 1 1 2     2 3 4 6
# 1 2 3 4   1 1 1 1     2 3 4 5

matriz_1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
matriz_2 = [[1,1,1,1], [2,1,1,1], [1,1,1,2], [1,1,1,1]]
matriz_resultado = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

n = 4
# Tiempo y Espacio: n^2
for i in range(n):
    for j in range(n):
        matriz_resultado[i][j] = matriz_1[i][j] + matriz_2[i][j]

# print(matriz_resultado)


class Arreglo:
    def __init__(self, capacidad) -> None:
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.contador = 0

    # Tiempo O(n)
    def print_arreglo(self):
        for item in self.items:
            print('[',item, ']', end=" ")
        print()
    
    # En el peor de los casos es O(n), pero por insercion 
    # sin duplicar el arreglo es O(1)
    def insertar(self, valor): # O(1)
        if self.tamano() == self.capacidad: # Arreglo lleno O(n)
            nuevo_arreglo = [None] * (self.capacidad * 2)
            for i in range(self.tamano()):
                nuevo_arreglo[i] = self.items[i]
            self.capacidad = self.capacidad * 2
            self.items = nuevo_arreglo
        self.items[self.contador] = valor # O(1)
        self.contador +=1

    # def insertar_error(self, valor):
    #     indice = 0
    #     for i in range(len(self.items)):
    #         if i == len(self.items):
    #             break
    #     self.items[indice] = valor

    # Tiempo es O(n)
    def eliminar(self, valor):
        # for i in range(self.tamano()):
        #     if self.items[i] == valor:
        #         self.items[i] = None
        for i in range(self.tamano()):
            if self.items[i] == valor:
                for j in range(i, self.tamano()):
                    self.items[j] = self.items[j + 1]
                return
    # Tiempo O(1)
    def tamano(self):
        return self.contador
    
    # Tiempo O(n)
    def indice(self, valor):
        indice = 0
        for i in range(self.tamano()):
            if self.items[i] == valor:
                break
            indice +=1
        print(indice)

    # O(1)
    def elemento(self, indice):
        print(self.items[indice])

arreglo = Arreglo(5)
arreglo.insertar(2)
arreglo.insertar(4)
arreglo.insertar(10)
arreglo.insertar(5)
arreglo.insertar(15)
arreglo.insertar(3)
# arreglo.print_arreglo()
arreglo.eliminar(5)
# arreglo.print_arreglo()
# arreglo.indice(5)
# arreglo.elemento(3)

# arreglo.print_arreglo()
