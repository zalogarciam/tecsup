# Ejercicio 1
# Complejidad de tiempo O(1)
# Complejidad de espacio O(1)

# nombre = input("Nombre:")
# print('Tu nombre es: ', nombre)

# Ejercicio 2
# Complejidad de tiempo O(n)
# Complejidad de espacio O(1)

# n = int(input("Numero: "))

# suma = 0
# for i in range(n + 1):
#     suma += i # suma = suma + i

# print(suma)

# def suma(n):
#     suma = 0
#     for i in range(n + 1):
#         suma += i # suma = suma + i

# Ejercicio 3
# Complejidad de tiempo O(1)
# Complejidad de espacio O(1)

# a = int(input("Numero 1: "))
# b = int(input("Numero 2: "))

# print('Suma', a + b) # O(1)
# print('Resta', a - b) # O(1)
# print('Multiplicacion', a * b) # O(1)
# print('Division', a / b) # O(1)

# Ejercicio 4
# Complejidad de tiempo O(n) donde n es el numero de iteraciones 
# para la tabla de multiplicar. En este ejemplo es 10. O(10)
# Complejidad de espacio O(1)

# numero = int(input("Numero: "))
# for i in range(1, 10):
#     print(str(numero), "*", str(i), "=",numero * i)

# Ejercicio 5
# Complejidad de tiempo O(n)
# Complejidad de espacio O(1)

# lista = [2,4,1,6,7]
# objetivo = 10

# # for i in range(len(lista)): O(n)
# #     if lista[i] == objetivo:
# #         print("Numero encontrado")

# if objetivo in lista: # O(n)
#     print("Numero encontrado")
# else:
#     print("Numero no encontrado")


# Ejercicio 6
# Complejidad de tiempo O(n)
# Complejidad de espacio O(n)

# lista = [2,4,6,8,10,12,14]
# # pares + impares = n 
# pares = [] # O(n)
# # impares = [] # O(n)
# for i in range(len(lista)):
#     if lista[i] % 2 == 0:
#         pares.append(lista[i])
#     # else:
#     #     impares.append(lista[i])
# print(pares)
# print(impares)

# Ejercicio 7
# Complejidad de tiempo O(n)
# Complejidad de tiempo O(1)

# lista = [3,4,6,8,10,12,14, 1] 
# # print(max(lista))

# max = -999999999
# for i in range(len(lista)):
#     if (lista[i] > max):
#         max = lista[i]
# print(max)


# Ejercicio 8
# Complejidad de tiempo O(1)
# Complejidad de tiempo O(1)
# n = 10
# potencia = 2
# print("Resultado:", 10 ** 2)


# Complejidad de espacio O(1)
# Complejidad de tiempo O(n^2)
# n = 10

# for i in range(n):
#     for j in range(n):
#         print(i, j)

# Complejidad de espacio O(1)
# Complejidad de tiempo O(n * m)
# n = 10
# m = 15
# for i in range(n):
#     for j in range(m):
#         print(i, j)


# Complejidad de espacio O(1)
# Complejidad de tiempo O(n^3 + n) = n^ 3
# n = 10
# m = 15
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print(i, j, k)
# for i in range(n):
#     print(i)

# n = 1 000 000 000
# 1 000 000 000 000 000 000 000 000 000 + 1 000 000 000

# Ejercicio 9 
# Entrada: GONZALO
# A = 1, E = 0, I = 0, O = 2, U = 0

cadena = "gonzalo"
# a = 0
# e = 0
# i = 0
# o = 0
# u = 0
# for caracter in cadena:
#     if caracter == "a": a += 1
#     if caracter == "e": e += 1
#     if caracter == "i": i += 1
#     if caracter == "o": o += 1
#     if caracter == "u": u += 1    
# print('a:',a)
# print('e:',e)
# print('i:',i)
# print('o:',o)
# print('u:',u)

# Tiempo: O(n)+O(v)
# Espacio O(v) + O(v) = O(2v) = O(v)
# cadena = "gonzalo"
# vocales = "aeiou" # ['a', 'e', 'i', 'o', 'u]
# diccionario = {}

# for vocal in vocales: # O(v) donde v es la cantida de vocales
#     diccionario[vocal] = 0
# print(diccionario)
# for caracter in cadena: # O(n) donde es la longitud de la cadena
#     if caracter in vocales:
#         diccionario[caracter] += 1

# print(diccionario)


# Ejercicio 10 
# Complejidad de tiempo n * (n - 1) / 2 = n^2 - n / 2 = n^2 
n = 4 
for i in range(1, n + 1): # O(n) 
    for j in range(i): # 
        print('*', end="")
    print()

# = n + (n - 1) + (n - 2) + 1 = n * (n + 1) / 2
# = 4 + 4-1 + 4-2 + 1
# = 4 + 3 + 2 + 1 = 10

# n * (n + 1) / 2
# 4 * (4 + 1) / 2 
# 4 * 5  / 2 = 10

# n * (n + 1) / 2
# n^2 + n / 2
# n^2


# = n * (n - 1) / 2 = 10 * (10 - 1) / 2 = 90/2 = 45
# = 10 + (10 - 1) + (10 - 2) + (10 - 3 + ... + 1 