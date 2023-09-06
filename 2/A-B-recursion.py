# palabra = "RECURSION"

# for caracter in palabra:
#     print(caracter)

# def mostrar_palabra(palabra, contador):
#     if len(palabra) == contador: # Caso Base
#         return
#     print(palabra[contador]) # Contenido del algoritmo
#     mostrar_palabra(palabra, contador + 1) # Llamada recursiva

# mostrar_palabra(palabra, 0)
# Edson Arias
# def factorial (numero) : 
#     contador = 1
#     while(contador<=numero): 
#         fact = 1*contador, 
#         contador += 1, 
#         return fact
    
# print(factorial(4))

# Albert Mamani
# def factorial(n):
#     if n == 0: # Caso Base
#         return 1
#     else:
#         return n * factorial(n-1)   # LLamada recursiva 
    
# Subproblemas
# 4 * factorial (3) 
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1 * factorial(0) --> Caso Base
# 4 * 3 * 2 * 1 * 1 = 24 # Combinacion de resultados
    
# print(factorial(4))

#Javier Neira
def factorial(n):
    resultado = 1 # O(1) ESPACIO
    for i in range(1, n + 1): # O(n) TIEMPO
        resultado *= i
    return resultado
resultado = factorial(4)
# print(resultado)

#          0    1   2   3    4   5   6
# 0     1   1   2   3   5   8   13  21  34  55 ...
#ant   act
#      ant act
#          ant act
# Espacio O(1)
# Tiempo O(n)
n = 6
anterior = 0
actual = 1
for i in range(n + 1):
    siguiente = anterior + actual
    anterior = actual
    actual = siguiente
print(actual)

def fibonacci(n):
    # Caso Base
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n -1) + fibonacci(n-2) # Llamada recursiva
# Espacio O(n)
# Tiempo O(2^n)
# Subproblemas
#                                           fibonacci(n=4)
#                       fibonacci(3)              +           fibonacci(2)
#             fibonacci(2)      +   fibonacci(1)       +    fibonacci(1)    + fibonacci(0)
#   fibonacci(1)+fibonacci(0)  +     1                 +        1           +   0
#      1        +       0      +     1                  +       1           +    0
#           =  3
#          x
#      x        x
#   x   x     x     x
# x x  x x   x x   x x
# 16 llamadas = 2^n = 2^4 = 16


print(fibonacci(6))