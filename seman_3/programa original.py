# Clase base que representa la información diaria del clima
class ClimaDiario:
    def __init__(self, dia, temperatura, humedad, precipitaciones):
        self.__dia = dia
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__precipitaciones = precipitaciones

    # Método para obtener el día
    def obtener_dia(self):
        return self.__dia

    # Método para obtener la temperatura
    def obtener_temperatura(self):
        return self.__temperatura

    # Método para obtener la humedad
    def obtener_humedad(self):
        return self.__humedad

    # Método para obtener las precipitaciones
    def obtener_precipitaciones(self):
        return self.__precipitaciones

    # Método para representar el objeto como una cadena
    def __str__(self):
        return f"Día: {self.__dia}, Temperatura: {self.__temperatura}, Humedad: {self.__humedad}, Precipitaciones: {self.__precipitaciones}"

# Clase derivada que extiende ClimaDiario, utilizada para cálculos adicionales si es necesario
class CalculoPromedioSemanal:
    def __init__(self):
        self.dias_clima = []

    # Método para agregar un objeto ClimaDiario
    def agregar_dia_clima(self, clima_diario):
        self.dias_clima.append(clima_diario)

    # Método para calcular el promedio de la semana (7 días)
    def calcular_promedio_semanal(self):
        total_temperatura = 0
        total_humedad = 0
        total_precipitaciones = 0

        for clima in self.dias_clima:
            total_temperatura += clima.obtener_temperatura()
            total_humedad += clima.obtener_humedad()
            total_precipitaciones += clima.obtener_precipitaciones()

        num_dias = len(self.dias_clima)

        if num_dias == 0:
            return "No hay datos disponibles para calcular el promedio"

        promedio_temperatura = total_temperatura / num_dias
        promedio_humedad = total_humedad / num_dias
        promedio_precipitaciones = total_precipitaciones / num_dias

        return {
            "promedio_temperatura": promedio_temperatura,
            "promedio_humedad": promedio_humedad,
            "promedio_precipitaciones": promedio_precipitaciones
        }

    # Método para mostrar los datos de la semana
    def mostrar_datos_semanales(self):
        for clima in self.dias_clima:
            print(clima)

# Ejemplo de uso
# Creamos objetos de ClimaDiario para cada día
clima_lunes = ClimaDiario("Lunes", 25.0, 60, 5)
clima_martes = ClimaDiario("Martes", 22.5, 55, 0)
clima_miercoles = ClimaDiario("Miércoles", 27.0, 65, 10)
clima_jueves = ClimaDiario("Jueves", 23.0, 50, 3)
clima_viernes = ClimaDiario("Viernes", 26.0, 70, 8)
clima_sabado = ClimaDiario("Sábado", 24.5, 60, 4)
clima_domingo = ClimaDiario("Domingo", 28.0, 75, 12)

# Creamos el objeto para cálculo de promedio semanal
calculo_semanal = CalculoPromedioSemanal()

# Agregamos cada día al cálculo semanal
calculo_semanal.agregar_dia_clima(clima_lunes)
calculo_semanal.agregar_dia_clima(clima_martes)
calculo_semanal.agregar_dia_clima(clima_miercoles)
calculo_semanal.agregar_dia_clima(clima_jueves)
calculo_semanal.agregar_dia_clima(clima_viernes)
calculo_semanal.agregar_dia_clima(clima_sabado)
calculo_semanal.agregar_dia_clima(clima_domingo)

# Mostramos los datos semanales
calculo_semanal.mostrar_datos_semanales()

# Calculamos y mostramos el promedio semanal
promedios = calculo_semanal.calcular_promedio_semanal()
print("\nPromedios semanales:")
print(f"Temperatura promedio: {promedios['promedio_temperatura']:.2f}")
print(f"Humedad promedio: {promedios['promedio_humedad']:.2f}")
print(f"Precipitaciones promedio: {promedios['promedio_precipitaciones']:.2f}")
