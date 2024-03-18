def calcular_descuento(monto_total, porcentaje_descuento=10):

   # Calcula el descuento aplicando el porcentaje al monto total de la compra.

    descuento = monto_total*porcentaje_descuento / 100
    return descuento
# Llamar a la función calculo descuento
monto_compra_1 = 500
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1-descuento_1

monto_compra_2 = 1500
porcentaje_descuento_2 = 10
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

# Resultados
print("Llamada 1:")
print("Monto de compra:", monto_compra_1)
print("Porcentaje de descuento por defecto:", 12, "%")
print("Monto del descuento:", descuento_1)
print("Monto final a pagar después del descuento:", monto_final_1)

print("\nLlamada 2:")
print("Monto de compra:", monto_compra_2)
print("Porcentaje de descuento:", porcentaje_descuento_2, "%")
print("Monto del descuento:", descuento_2)
print("Monto final a pagar después del descuento:", monto_final_2)




