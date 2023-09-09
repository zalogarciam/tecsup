# Ejercicio 1

# def factorial(n):
#     if n == 1: return 1
#     return n * factorial(n - 1)
# n = 4
# print(factorial(n))

# Tiempo O(n)
# Espacio O(n)

# factorial(4)
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1

# n = 5
# 1 + 2 + 3 + 4 + 5 = 15

# def suma_natural(n):
#     if n == 1: return 1
#     return n + suma_natural(n - 1)

# n = 5
# print(suma_natural(n))

# suma_natural(5)
# 5 + suma_natural(4)
# 5 + 4 + suma_natural(3)
# 5 + 4 + 3 + suma_natural(2)
# 5 + 4 + 3 + 2 +   suma_natural(1)
# 5 + 4 + 3 + 2 + 1

# Ejercicio 3

# def fibonacci(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))
# Tiempo O(2^n)
# Espacio O(n)
# 0 1 1 2 3 5 8 13 21 34....

#                                fibonacci(4)
#                fibonacci(3)          +            fibonacci(2)
#        fibonacci(2) + fibonacci(1)   +    fibonacci(1) + fibonacci(0)
# fibonacci(1) + fibonacci(0) +   1    +          1      +      0
#       1      +       0      +   1    +          1      +      0
# = 3


# Ejercicio 4

# def potencia(x, n): 
#     if n == 1: return x
#     return x * potencia(x, n - 1)
# x = 2
# n = 5
# 32 = 2^5
# print(potencia(x, n))
# potencia(2, 5)
# 2 * potencia(2, 4)
# 2 * 2 * potencia(2, 3)
# 2 * 2 * 2 * potencia(2, 2)
# 2 * 2 * 2 * 2 * potencia(2, 1)
# 2 * 2 * 2 * 2 * 2 * potencia(2, 0)
# 2 * 2 * 2 * 2 * 2 * 1

# Ejercicio 5
# 12345 = 15
# 1 + 2+ 3 + 4 + 5 = 15

# def suma_digitos(numero, indice, suma):
#     if len(numero) == indice: return suma
#     suma += int(numero[indice])
#     return suma_digitos(numero, indice + 1, suma)
# print(suma_digitos("12345", 0, 0))

# suma_digitos(12345, 0, 1)
# suma_digitos(12345, 1, 3)
# suma_digitos(12345, 2, 6)
# suma_digitos(12345, 3, 10)
# suma_digitos(12345, 4, 15)
# suma_digitos(12345, 5, ... return suma)

# Ejercicio 6
# GONZALO , O
# 2

# Tiempo Espacio = O(n)

# def conteo_caracteres(palabra, caracter, indice, contador):
#     # caso base
#     if len(palabra) == indice: return contador
#     if palabra[indice] == caracter: contador += 1
#     return conteo_caracteres(palabra, caracter, indice + 1, contador)

# print(conteo_caracteres('GONZALO', 'O', 0, 0))

# conteo_caracteres('GONZALO', 'O', 0, 0)
# conteo_caracteres('GONZALO', 'O', 1, 1)
# conteo_caracteres('GONZALO', 'O', 2, 1)
# conteo_caracteres('GONZALO', 'O', 3, 1)
# conteo_caracteres('GONZALO', 'O', 4, 1)
# conteo_caracteres('GONZALO', 'O', 5, 1)
# conteo_caracteres('GONZALO', 'O', 6, 2)

# Ejercicio 7
# [1,2,3,4,5,6] = 21


def suma_lista(lista, indice, suma):
    if len(lista) == indice: return suma
    suma = suma + lista[indice]
    return suma_lista(lista, indice+1 , suma)

print(suma_lista([1,2,3,4,5,6], 0, 0))

# suma_lista([1,2,3,4,5,6], 0, 1)
# suma_lista([1,2,3,4,5,6], 1, 3)
# suma_lista([1,2,3,4,5,6], 2, 6)
# suma_lista([1,2,3,4,5,6], 3, 10)
# suma_lista([1,2,3,4,5,6], 4, 15)
# suma_lista([1,2,3,4,5,6], 5, 21)
# suma_lista([1,2,3,4,5,6], 6 ... CASO BASE return 21)



def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    if solve_nqueens_util(board, 0, n) is False:
        print("Solution does not exist")
        return
    print_solution(board)

def solve_nqueens_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueens_util(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))

solve_nqueens(4)




