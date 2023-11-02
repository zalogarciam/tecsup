# Example

# Array
# Una operación de rotación hacia la izquierda en una matriz desplaza cada 
# uno de los elementos de la matriz hacia la izquierda. Por ejemplo, si se 
# realizan 2 rotaciones hacia la izquierda en una matriz [1,2,3,4,5], entonces la matriz 
# se convertiría en [3,4,5,1,2]. Tenga en cuenta que el elemento del índice más bajo se 
# mueve al índice más alto en una rotación. Esto se llama matriz circular.

# Dada una matriz de números enteros y un número X, realice X rotaciones hacia 
# la izquierda en la matriz. Devuelve la matriz actualizada que se imprimirá 
# como una sola línea de números enteros separados por espacios.

# X = 4 [1,2,3,4,5]
# Result: [5,1,2,3,4]

# Edge cases -> Escenarios podria tener este ejercicio y manejarlos (5pts)
# Time and Space complexity (5pts)
# Code works (5pts)
# Syntax - Good practices (5pts)

# Time Complexity: O(n)
# Space complexity: O(n)
# Edge Cases: Array vacio, Array con un elemento, Array con mas de 1 elemento, 
# ...Negative numbers for X, etc.

def left_rotation(array, X):
    if X < 0: raise Exception("X cannot be less that 0")
    if len(array) == 0: raise Exception("Empty array") # Array vacio
    if len(array) == 1: return array # Array con un elemento
    rotations = X % len(array)
    new_array = array[rotations:] + array[:rotations] # Array con mas de 1 elemento
    return new_array

# print(left_rotation([], 4))
print(left_rotation([1], 4))
print(left_rotation([1,2,3,4,5], 4))
print(left_rotation([1,2,3,4,5], 2))
print(left_rotation([1,2,3,4,5], 16)) # 1 rotation
print(left_rotation([1,2,3,4,5], -2)) # 1 rotation

