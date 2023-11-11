costos_fijos = 300000  # euros al año
capacidad_maxima_negocios = 1500000  # euros
costos_variables_proporcion = 2 / 3  # dos tercios

# Calcular costos variables
costos_variables = capacidad_maxima_negocios * costos_variables_proporcion

# Calcular precio de venta por unidad (que en este caso es igual a la cifra de negocios máxima)
precio_venta_por_unidad = capacidad_maxima_negocios

print(precio_venta_por_unidad)
# Calcular punto muerto
punto_muerto = costos_fijos / (precio_venta_por_unidad - costos_variables)

# Mostrar resultado
print(f"El Punto Muerto es de {round(punto_muerto, 2)} euros.")