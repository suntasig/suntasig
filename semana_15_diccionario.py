# crear un diccionario con información ficticia

información_personal = {
    "nombre": "Luis Suntasig",
    "edad":35,
    "ciudad":"Latacunga"
}

# Acceder al valor asociado con la clave ciudad y nodificarlo
información_personal["ciudad"] = "Quito"

# Agregar una nueva clave para presentar la profeción
información_personal["profeción"] = "Arquitecto"

# verificar numero telefonico si existe y agregar si no existe
if "telefono" not in información_personal:
    información_personal["telefono"] = "0987853470"

# Eliminar la clave de edad
información_personal.pop("edad")

# imprimir el diccionario final
print("diccionario final")
print(información_personal)
