# crear una función para convertir grados centígrados a grados Fahrenheit, a grados kelvin
# Fahrenheit = (9/5)*(grad_centi)+32
# Kelvin = 273.15+grad_cent
def convertir_temperatura(grad_centi):
    # Convertir a Fahrenheit
    fahrenheit = (9 / 5) * grad_centi + 32

    # Convertir a Kelvin
    kelvin = grad_centi + 273.15

    return fahrenheit, kelvin


# Ejemplo de uso:
grados_centigrados = 30
fahrenheit, kelvin = convertir_temperatura(grados_centigrados)

print(f"{grados_centigrados} grados Centigrados son {fahrenheit:.2f} grados Fahrenheit.")
print(f"{grados_centigrados} grados Centigrados son {kelvin:.2f} Kelvin.")

