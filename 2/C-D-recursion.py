# palabra = 'RECURSION'

# for caracter in palabra:
#     print(caracter)

# def mostrar(palabra, indice):
#     if indice == len(palabra): return # CASO BASE
#     print(palabra[indice])
#     mostrar(palabra, indice + 1) # LLAMADA RECURSIVA

# mostrar(palabra, 0)

# Factorial

# 4! = 4 * 3 * 2 * 1
n = 4

# Tiempo O(n)
# Espacio O(1)

# resultado = 1
# for i in range(1, n + 1):
#     resultado *= i
# print(resultado)


# Tiempo O(n) # numero total de llamadas recursivas.
# Espacio O(n) # el espacio que ocupa en la pila de llamadas 

# def factorial(n):
#     if n == 1: return 1 # caso base
#     return n * factorial(n - 1) # llamada recursiva

# n * factorial(n - 1) 

# Pila de llamadas (Call stack)
# Reduccion del problema
# factorial(4)
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1 # Combinacion de resultados.
# = 24

# print(factorial(n))
#                      n-2  n-1 n
#   0  1    1       2   3   5   8   13  21  34  55  89 ... 
# ant act   sig

# n = 5
# anterior = 0
# actual = 1

# Tiempo O(n+1) = O(n)
# Espacio O(?) = O(1)
# for i in range(n + 1):
#     siguiente = anterior + actual
#     anterior = actual
#     actual = siguiente

# print(anterior) 
# print(actual)


# Tiempo O(?) = O(2^(n-1)) = O(2^n) = 2^5 = 32 --> 16
# Espacio O(?) = O(n)

def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))

# fibonacci(n - 1) + fibonacci(n - 2)
# Pila de llamadas (Call stack)
# Reduccion del problema
#                                          fibonacci(5) =  2^0
#                   fibonacci(4)                +                   fibonacci(3) = 2^1
#       fibonacci(3)      +    fibonacci(2)     +      fibonacci(2)      +       fibonacci(1) = 2^2 = 4
# fibonacci(2)+fibonacci(1) + fibonaaci(1)+fibonacci(0) + fibonaaci(1)+fibonacci(0) + 1 = 2^3 = 8
# fibonacci(1)+fibonacci(0) + 1 + 1               + 0           + 1 +         0          + 1 = 2^4 = 16
# 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 = 5

# fibonnaci(6)