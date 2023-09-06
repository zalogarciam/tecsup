# Lab 1 - Introduccion
# Ejercicio 1

# Complejidad de tiempo y espacio: O(1)
# nombre = input('Nombre: ') 
# print('Tu nombre es:', nombre)

# Ejercicio 2

# Complejidad de tiempo: O(n + 1) = O(n)
# Complejidad de espacio: O(1)
# n = int(input('Ingrese un numero: ')) # 5 --> 0+1+2+3+4 +5
# suma = 0 # O(1)
# for i in range(n + 1):
#     suma = suma + i
# print(suma)

# Ejercicio 3

# Complejidad de tiempo: O(1)
# Complejidad de espacio: O(1)
# a = int(input('Ingrese el primer numero: ')) # O(1)
# b = int(input('Ingrese el segundo numero: '))  # O(1)
# if a == 0 or b == 0: # O(1)
#     raise Exception('Ingrese valores positivos')
# print('Suma:', a + b) # O(1)
# print('Resta:', a - b) # O(1)
# print('Division:', a // b) # O(1)
# print('Multiplicacion:', a * b) # O(1)

# Ejercicio 4

# Complejidad de tiempo: O(10) = O(1)
# Complejidad de espacio: O(1)
# n = int(input('Ingrese el primer numero: ')) # O(1)
# 5
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# 4 x 5 = 20
# 5 x 5 = 25
# 6 x 5 = 30
# 7 x 5 = 35
# 8 x 5 = 40
# 9 x 5 = 45
# 10 x 5 = 50

# for i in range(1, 1000000): # O(10)
#     print(i, "x", n ,"=", i * n)

# Para el caso del 1000000 O(1000000)
# O(n) donde n es el numero maximo en la tabla multiplicar
# del ejercicio. En este caso = 1000000


# Complejidad de tiempo: O(n)
# Complejidad de espacio: O(n)

# def tabla_multiplicar(n):
#     cadena = [] # arreglo adicional
#     for i in range(1, n): # O(10)
#         resultado = str(i) + "x" + str(n) + "=" + str(i * n)
#         cadena.append(resultado)
#     return cadena

# cadena = tabla_multiplicar(n) # 10
# print(cadena)

# Ejercicio 5 
# Complejidad de tiempo : O(n)
# Complejidad de espacio : O(n)

# Lin
# objetivo = int(input("Ingrese un numero objetivo: "))
# lista = [1, 2, 3, 4, 5]

# if objetivo in lista:
#      print("Si se encuentra el objetivo ", objetivo)

# Angel Eduardo

# lista = [3,6,8,2,45,9,1,11]
# objetivo = int(input("Ingrese el numero objetivo: "))
# if objetivo in lista:
#     print("El numero si esta en la lista")
# else:
#     print("El numero no se encuentra en la lista")

# Ramiro
# Lista es parte del problema pero no de la solucion
# Por ende, no se considera en la complejidad de espacio
# lista = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] # n =10 
# Resultado= [10 .. 10]
# numero = int(input('Ingrese numero a buscar en la lista: '))

# Por otro lado, resultado [] es parte de la solucion
# Por ende se considera en la complejidad de tiempo

# resultado = [] # Complejidad de espacio O(n)
# for i in range(10): # Complejidad de tiempo O(n)
#     if numero == lista [i]:
#         resultado.append(numero)

# print(resultado)
# Complejidad de Tiempo seria O(n) donde n 
# es la cantidad de items en la lista que va a recorrer
# el algoritmo.
# Complejidad de Espacio seria O(1) porque solamente
# estoy utilizando una variable para guardar el numero
# a buscar


# Ejercicio Original

#Complejidad de Tiempo: 0(n)
#Complejidad de Espacio: 0(1)
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numero = int(input('Ingrese numero a buscar en la lista: '))
# for i in range(10):
#     if numero == lista [i]:
#         print("Numero Encontrado")
#         break
#     else:
#         continue


# Ejercicio 6
#Complejidad de Tiempo: 0(1)
#Complejidad de Espacio: 0(1)

# n = int(input('Ingrese un numero: ')) #0(1)
# if n % 2 == 0: #0(1)
#     print('Este numero es par') #0(1)
# else:
#     print('Este numero es impar')

# Ejercicio 7
# Complejidad de Tiempo: 0(?)
# Complejidad de Espacio: 0(?)

# Ramiro
#Complejidad de Tiempo: 0(1) --> O(n)
#Complejidad de Espacio: 0(1)
# lista = [4232, 4753, 12435, 1252654, 131424, 214, 1512, 12124, 6856, 324]
# print(max(lista)) # O(1) complejidad de espacio

# Mauro
# lista = [1,2,3,4,5,6,22,8,9,10]
# maximo = 0
# for i in lista:
#     if i > maximo:
#         maximo = i
# print(maximo)
# Complejidad de tiempo O(n)
# Complejidad de espacio O(1)

# Lin

#ejercicio 7
# Complejidad de tiempo : O(1) --> O(n)
# Complejidad de espacio : O(1)
# lista = [20,100,60,120,180,200,3,5]
# maxValor = max(lista)
# print("El valor maximo en la lista es:", maxValor)

# Angel
# Ejercicio 7
# Complejidad de tiempo: O(n)
# Complejidad de espacio: O(1)
# lista = [1, 5, 2, 8 ,10 ,44, 100, -55]
# mayor = 0
# for i in lista:
#     if mayor < i:
#         mayor = i
# print(mayor)

# Wilbert

# def encontrar_maximo(lista):
#     return max(lista)
# números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# máximo = encontrar_maximo(números)
# print("El número máximo es:", maximo)

# Deivid

# lista = [1,5,32,45,6,52] # Parte del problema

# maximo = 0 # Parte de la solucion --> O(1) Complejidad Espacio
# for numero in lista:
#     if numero > maximo:
#         maximo = numero
# print("El número máximo es: ", maximo)
# # Complejidad de tiempo: O(n)
# # Complejidad de espacio: O(1)

# Ejercicio 8
# # Complejidad de tiempo: O(1)
# # Complejidad de espacio: O(1)
# numero = int(input('Ingrese un numero: '))   #O(1)
# potencia = int(input('Ingrese la potencia: '))  #O(1)
# print(numero ** potencia)  #O(1)

# Ejercicio 9 
# # Complejidad de tiempo: O(n)
# donde n es la longitud de la cadena
# # Complejidad de espacio: O(1)
cadena = input('Ingrese la cadena: ')
# a = 0 # O(1)
# e = 0 # O(1)
# i = 0 # O(1)
# o = 0 # O(1)
# u = 0 # O(1)
# for vocal in cadena:
#     if vocal == 'a': a += 1
#     if vocal == 'e': e += 1
#     if vocal == 'i': i += 1
#     if vocal == 'o': o += 1
#     if vocal == 'u': u += 1
# print('a: ', a) # O(1)
# print('e: ', e) 
# print('i: ', i)
# print('o: ', o)
# print('u: ', u)

diccionario = {} # clave y valor O(v)
# clave seria la vocal y el valor seria el contador
vocales = "aeiou" # ['a', 'e', 'i', 'o', 'u'] O(v)

for vocal in vocales: #O(v) donde v es el numero de vocales
    diccionario[vocal] = 0
print(diccionario)

for vocal in cadena: #O(n) donde n es la longitud de la cadena
    if vocal in vocales: diccionario[vocal] += 1
print(diccionario)

# Complejidad de tiempo: O(n) + O(v)
# Complejidad de espacio: O(v) + O(v) = O(2v) = O(v) 

# Ejercicio 10

# Ramiro

#Complejidad de Tiempo: 0(n)
#Complejidad de Espacio: 0(1)
for i in range (5):
    for j in range (i):
        print('* ', end='')
    print()

# Javier

def patron(filas):
    for i in range(1, filas + 1):
      print("*" * i)
filas = int(input("Ingresa la cantidad de filas para el patron: "))
patron(filas)

# Deivid
n = int(input("Ingrese un numero: "))
for i in range(1, n + 1):
    print("*" * i)
#Complejidad de tiempo y espacio: O(n^2)