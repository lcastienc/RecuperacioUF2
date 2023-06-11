from Funciones import mostrar_velocidad_microprocesador, mostrar_megapixeles, mostrar_capacidad_bateria

# Función principal
def main():
    # IDs de muestra
    ids_muestra = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

    # Llamar a las funciones para generar las gráficas
    mostrar_velocidad_microprocesador(ids_muestra)
    mostrar_megapixeles(ids_muestra)
    mostrar_capacidad_bateria(ids_muestra)

# Llamar a la función principal
main()
