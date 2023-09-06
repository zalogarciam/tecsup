# Ejercicio 1
# Complejidad de tiempo: O(1)
# Complejidad de espacio: O(1)

# nombre = input("Nombre: ")
# print("Hola ", nombre)

# Ejercicio 2
# Complejidad de tiempo: O(n)
# Complejidad de espacio: O(1)
# n = 5 , 1 + 2 + 3 + 4 + 5 = 15

# n = int(input("Numero: "))

# suma = 0
# for i in range(1, n + 1):
#     suma += i # suma = suma + i
# print(suma)

# Ejercicio 3
# Complejidad de tiempo: O(1)
# Complejidad de espacio: 0(1)

# a = int(input("Numero 1: "))
# b = int(input("Numero 2: "))

# print('Suma:', a+b) #0(1)
# print('Resta:', a-b) #0(1)
# print('Multiplicacion:', a*b) #0(1)
# print('Division:', a/b) #0(1)

# Ejercicio 4
# Complejidad de tiempo: O(n) donde n es el numero mayor
# que me pide el enunciado al realizar la tabla de multiplicaciom
# Complejidad de espacio: 0(1)
# n = 5
# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# ...
# 10 * 5 = 50

# n = int(input("Numero: "))
# for i in range(1, 10 + 1):
#     print(i , "*", n, "=", i * n)


# Ejercicio 5
# [1,4,6,7,8,9,10,11,12]
# Objetivo: 9
# True

# Complejidad de tiempo O(n)
# Complejidad de espacio O(1)

# lista = [1,4,6,7,0,9,10,11,8]

# objetivo = 8

# for item in lista:
#     if item == objetivo:
#         print("Si se encontro")
#         break


# Ejercicio 6

# Complejidad de tiempo O(n)
# Complejidad de espacio  O(n)

# [1,4,6,8,5,3,9] entrada
# pares [4,6,8]
# impares [1,5,3,9]

# lista = [1,4,6,8,5,3,9]
# lista = [2,4,6,8,10,12,14]

# longitud de la lista = longitud de la lista de pares + longitud de la lista
# impares
# pares = []
# # impares = []
# # pares + impares = lista
# # O(n) donde n es la longitud del arreglo de entrada
# for numero in lista:
#     if numero % 2 == 0:
#         pares.append(numero)
#     # else:
#     #     impares.append(numero)
# print(pares)
# print(impares)

# Ejercicio 7
# Tiempo
# Espacio

# lista = [2,4,6,8,10,12,14,1]

# print(max(lista))
# max = -999999999
# for i in lista:
#     if i > max:
#         max = i
# print(max)

# Ejercicio 8
# O(1)
# n = 10
# potencia = 2
# print(n ** potencia)


# Ejercicio 9

# GONZALO
# A = 1
# E = 0
# I = 0
# O = 2
# U = 0
# Espacio : # O(1)
# Tiempo O(n) donde n es la longitud de la cadena
# cadena = 'gonzalo'
# a = 0 # O(1)
# e = 0 # O(1)
# i = 0 # O(1)
# o = 0 # O(1)
# u = 0 # O(1)
# for caracter in cadena:
#     if caracter == 'a': a+=1
#     if caracter == 'e': e+=1
#     if caracter == 'i': i+=1
#     if caracter == 'o': o+=1
#     if caracter == 'u': u+=1

# print('a',a)
# print('e',e)
# print('i', i)
# print('o', o)
# print('u', u)

# cadena = "gonzalo"

# vocales = "aeiou" # ['a','e','i','o','u'] O(v)
# diccionario = {} # O(v)
# # Tiempo: O(v) + O(n)
# # Espacio: O(v) + O(v) 
# for vocal in vocales: # O(v) donde v es la cantidad de vocales
#     diccionario[vocal] = 0
# print(diccionario)

# for caracter in cadena: # O(n) donde n es la longitud de la cadena
#     if caracter in vocales:
#         diccionario[caracter] += 1
# print(diccionario)

# n = 10
# m = 20
# # Tiempo n^2
# for i in range(n):
#     for j in range(n):
#         print(i, j)   

# Tiempo n * m
# for i in range(n):
#     for j in range(m):
#         print(i, j)

# Tiempo n^3 + n = n^3
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print(i, j, k)
# for i in range(n):
#     print(i)

# n = 1 000 000 000
# n^3 = 1 000 000 000 000 000 000 000 000 000 + 1 000 000 0000

n = 4
# # 1
# for i in range(1, n + 1):
#     print('*' * i)

# 2
for i in range(1, n + 1): 
    for j in range(i): 
        print('*', end="")
    print()

# n + (n-1) + (n-2) + (n-3) + (n-4) + ... + 1
# = n (n + 1) / 2
# = 10 (11) / 2 = 55

# = n (n + 1) / 2
# = n^2 + n / 2
# = n^2

# n = 4
# n + (n-1) + (n-2) + 1
# 4 + 3 + 2 + 1 = 10
# = n (n + 1) / 2
# = 4*5/2 = 10

# = n (n + 1) / 2 O(n) tiempo
# = n^2 + n / 2
# = n^2
