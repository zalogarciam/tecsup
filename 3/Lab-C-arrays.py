# # Ejercicio

# # Tiempo O(n)
# # Espacio O(1)
# lista = [4,6,7,2,3,5]

# suma = 0
# for numero in lista:
#     suma += numero
# # print(suma)

# # Ejercicio 3
# pares = 0
# impares = 0
# for numero in lista:
#     if numero % 2 == 0:
#         pares +=1
#     else:
#         impares +=1
# print(pares, impares)


# Ejercicio 6

arreglo = [1,2,2,3,4,4,4,5,6]
arreglo = [1,2,3,4,5,6,7,8,9,0]
# # 1,2,3,4,5,6
# # Tiempo y Espacio : O(n)
# # [1,2,3,4,5,6,7,8,9,10]
nuevo_arreglo = []
for numero in arreglo:
    if numero not in nuevo_arreglo:
        nuevo_arreglo.append(numero)

print(nuevo_arreglo)


# Ejercicio 7
# 1 5 5
# 2 5 10
# 3 5 15
# 4 5 20
# 5 5n25

# Tiempo : O(n)
# Espacio O(3n)
# n = 100

# matriz = [[0] * 3 for _ in range(n)]

# for fila in range(n):
#     for columna in range(3):
#         if columna == 0:
#             matriz[fila][columna] = fila + 1
#         if columna == 1:
#             matriz[fila][columna] = n
#         if columna == 2:
#             matriz[fila][columna] = (fila+1) * n

# for fila in matriz:
    # print(fila)

# Ejercicio 8 
# [abc, ba, abcdef, as, two]
# Return abcdef

# lista = ["abc", "ba", "abcdef", "as", "two"]

# Tiempo y Espacio O(n)
# mayor = ""
# for palabra in lista:
#     if len(palabra) > len(mayor):
#         mayor = palabra
# print(mayor)


# 1 2 3 4   4 4 4 4   5 6 7 8
# 1 2 3 4   1 1 1 1 = 2 3 4 5
# 1 2 3 4   2 2 2 2   3 4 5 6
# 1 2 3 4   3 3 3 3   4 5 6 7

# n = 4
# matriz = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# matriz_2 = [[4,4,4,4], [1,1,1,1], [2,2,2,2], [3,3,3,3]]
# matriz_resultado =  [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# for i in range(n):
#     for j in range(n):
#         matriz_resultado[i][j] = matriz[i][j] + matriz_2[i][j]

# for fila in matriz_resultado:
#     print(fila)

class Arreglo:
    def __init__(self, capacidad) -> None:
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.contador = 0

    def insertar(self, valor):
        if self.capacidad == self.contador: # O(n)
            nuevo_arreglo = [None] * (self.capacidad * 2)
            for i in range(self.capacidad):
                nuevo_arreglo[i] = self.items[i]
            self.capacidad = self.capacidad * 2
            self.items = nuevo_arreglo
        self.items[self.contador] = valor # O(1)
        self.contador += 1

    def eliminar(self, valor):
        # for i in range(self.tamano()):
        #     if self.items[i] == valor:
        #         self.items[i] = None
        for i in range(self.tamano()):
            if self.items[i] == valor:
                for j in range(i, self.tamano()):
                    self.items[j] = self.items[j + 1]
        self.contador -= 1

    def tamano(self):
        return self.contador

    # def insertar_error(self, valor): # O(n)
    #     indice = 0
    #     for i in range(len(self.items)):
    #         indice +=1
    #     self.items[indice] =  valor

    def print_array(self):
        for item in self.items:
            print('[',item, ']', end=" ")
        print()
    def indice(self, value):
        indice = 0
        for i in range(self.tamano()):
            if self.items[i] == value:
                break
            indice+=1
        return indice

    def elemento(self, indice):
        return self.items[indice]

    def buscar(self, value):
        for i in range(self.tamano()):
            if self.items[i] == value:
                return True
        return False


arreglo = Arreglo(7)
arreglo.insertar(2)
arreglo.insertar(3)
arreglo.insertar(7)
arreglo.insertar(9)
arreglo.insertar(10)
arreglo.insertar(99)
arreglo.print_array()
arreglo.eliminar(7)
arreglo.print_array()
# print(arreglo.elemento(4))
# print(arreglo.indice(10))
# print(arreglo.tamano())
# arreglo.print_array()


