# Factorial
# Tiempo O(n)
# Espacio O(n
# 4! = 4 * 3 * 2 * 1

# def factorial(n):
#     if n == 1:  return 1 # Caso Base
#     return n * factorial(n-1)

# # 4 * factorial (n-1)
# # 4 * factorial (3)
# # 4 * 3 * factorial (2)
# # 4 * 3 * 2 * factorial (1) # caso base
# # 4 * 3 * 2 * 1 = 24

# n = 4
# print(factorial(n))

# Tiempo O(n)
# Espacio O(n
# def suma(n):
#     if n == 1: return 1
#     return n + suma(n-1)

# n = 5
# print(suma(n))


# Tiempo O(2^n)
# Espacio O(n)

# def fibonacci(n):
#     if n == 1: return 1
#     if n == 0: return 0
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))
# n = 5

#                           fibonacci(5)
#          fibonacci(4)         +              fibonacci(3)
# fibonacci(3)   + fibonacci(2)   +       fibonacci(2) + fibonacci(1)
# f(2) + f(1)    + f(1) + f(0)     +  f(1) + f(0) +    1
# f(1) + f(0) + 1 + 1 +     0      +   1   +   0      + 1
# 1   + 0   + 1 + 1  +     0      + 1    + 1
# = 5

# def potencia(x, n):
#     if n == 0: return 1
#     return x * potencia(x, n - 1)
# Tiempo O(n)
# Espacio O(n)
# print(potencia(2,5))
# x^n = 2^5
# x = 2
# n = 5

# potencia(2, 5)
# 2 * potencia(2, 4)
# 2 * 2 * potencia(2, 3)
# 2 * 2 * 2 * potencia(2, 2)
# 2 * 2 * 2 * 2 * potencia(2, 1)
# 2 * 2 * 2 * 2 * 2 * potencia(2, 0)
# 2 * 2 * 2 * 2 * 2 * 1

# 12345 = 15
# Tiempo O(n)
# Espacio O(n)
# def suma_digitos(numero, indice):
#     if indice == len(numero): return 0
#     return int(numero[indice]) + suma_digitos(numero, indice+1)

# print(suma_digitos("12345", 0))

# GONZALO, O
# 2

# Tiempo O(n)
# Espacio O(n)
# def conteo_caracteres(palabra, caracter, indice, contador):
#     if indice == len(palabra): return contador
#     if palabra[indice] == caracter: contador +=1
#     return conteo_caracteres(palabra, caracter, indice + 1, contador)

# print(conteo_caracteres('GONZALO', 'O', 0, 0))



# [2,5,6,1,5] = 19 
# Tiempo O(n)
# Espacio O(n)
def sumar(lista, indice, suma):
    if indice == len(lista): return suma
    suma = suma + lista[indice]
    return sumar(lista, indice + 1, suma)

print(sumar([1,2,3,4,5], 0, 0))


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


