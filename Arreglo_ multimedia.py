def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def ordenar_fila_en_matriz(matriz, fila):
    fila_ordenada = list(matriz[fila])
    bubble_sort(fila_ordenada)
    matriz[fila] = fila_ordenada
# Matriz de ejemplo (3x3)
matriz = [
    [3, 1, 5],
    [4, 2, 7],
    [9, 6, 8]
]
print("Matriz original:")
for fila in matriz:
    print(fila)
fila_a_ordenar = 0
ordenar_fila_en_matriz(matriz, fila_a_ordenar)
print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
    print(fila)


