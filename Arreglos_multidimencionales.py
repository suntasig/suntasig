# Arreglo multimedia
# Definir la matriz bidimensional
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None

# Definir el valor a buscar
valor_a_buscar = 7

# Buscar el valor en la matriz
posicion = buscar_valor(matrix, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz")

