
# Datos de temperaturas de 3 ciudades durante 4 semanas con 7 días por semana
datos_ciudades = {
    'Ambato': [
        [[25, 26, 27, 28, 29, 30, 31],
         [26, 27, 28, 29, 30, 31, 32],
         [27, 28, 29, 30, 31, 32, 33],
         [28, 29, 30, 31, 32, 33, 34]],
    ],
    'Latacunga': [
        [[20, 21, 22, 23, 24, 25, 26],
         [21, 22, 23, 24, 25, 26, 27],
         [22, 23, 24, 25, 26, 27, 28],
         [23, 24, 25, 26, 27, 28, 29]],
    ],
    'Quito': [
        [[30, 31, 32, 33, 34, 35, 36],
         [31, 32, 33, 34, 35, 36, 37],
         [32, 33, 34, 35, 36, 37, 38],
         [33, 34, 35, 36, 37, 38, 39]],
    ]
}
def calcular_temp_promedio(datos_ciudades):
    # Creamos  los promedios de temperatura de cada ciudad
    promedios_ciudades = {}

    # Recorremos los datos de cada ciudad
    for ciudad, semanas in datos_ciudades.items():
        suma_temperaturas = 0
        contador_dias = 0

        # Recorremos las semanas de cada ciudad
        for semana in semanas:
            # Recorremos los días de cada semana
            for dias in semana:
                # Sumamos las temperaturas de cada día
                suma_temperaturas += sum(dias)
                # Contamos los días para calcular el promedio
                contador_dias += len(dias)

        # Calculamos el promedio de temperatura para la ciudad actual
        promedio_ciudad = suma_temperaturas / contador_dias
        # Almacenamos el promedio en el diccionario de promedios
        promedios_ciudades[ciudad] = promedio_ciudad

    # Devolvemos promedios de temperaturas de cada ciudad
    return promedios_ciudades

# Llamamos a la función para calcular el promedio de temperaturas de cada ciudad
resultados = calcular_temp_promedio(datos_ciudades)

# Imprimimos los resultados
for ciudad, promedio in resultados.items():
    print(f"La temperatura promedio de {ciudad} es: {promedio} grados centigrados")