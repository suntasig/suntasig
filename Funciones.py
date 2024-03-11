
# Datos de funcion
datos = {
    'Latacunga': [
        [20, 25, 22, 18],
        [23, 24, 21, 19],
        [22, 22, 20, 17]
    ],
    'Quito': [
        [18, 20, 19, 17],
        [21, 22, 20, 18],
        [20, 21, 19, 16]
    ],
    'Ambato': [
        [25, 28, 26, 23],
        [27, 27, 25, 22],
        [26, 25, 24, 21]
    ]
}
def calcular_temp_promedio(datos):
    temp_promedio_ciudad = {}

    for ciudad, semanas in datos.items():
        temp_total = 0
        num_semanas = len(semanas)
        for semana in semanas:
         temp_total += sum(semana)
         temp_promedio_ciudad[ciudad] = temp_total / (num_semanas * len(semanas[0]))
    return temp_promedio_ciudad
#calcular temperatura proemedio
temp_promedio = calcular_temp_promedio(datos)

for ciudad, temp in temp_promedio.items():

    print(f"Temperatura promedio en {ciudad}: {temp}")
