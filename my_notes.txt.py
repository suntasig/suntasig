# Crear el archivo my_notes.txt y escribir algunas notas
with open("my_notes.txt", "w") as file:
    file.write("1. Recordar comprar leche en el supermercado.\n")
    file.write("2. Llamar a Juan para confirmar la cita.\n")
    file.write("3. Terminar el informe antes del viernes.\n")

# Abrir el archivo y leer las notas línea por línea
with open("my_notes.txt", "r") as file:
    # Leer las líneas una por una
    for line in file.readlines():
        # Mostrar la línea en la consola
        print(line.strip())  # strip() para eliminar caracteres de nueva línea

# Cerrar el archivo después de realizar las operaciones necesarias
file.close()