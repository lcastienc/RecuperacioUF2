import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv("data.csv")


# Función para mostrar la velocidad del microprocesador por ID
def mostrar_velocidad_microprocesador(ids):
    velocidad_micro = data.loc[data['id'].isin(ids), ['id', 'clock_speed']]

    # Crear gráfica de velocidad del microprocesador
    plt.bar(velocidad_micro['id'], velocidad_micro['clock_speed'])
    plt.xlabel('ID del móvil')
    plt.ylabel('Velocidad del microprocesador')
    plt.title('Velocidad del microprocesador por ID')
    plt.show()


# Función para mostrar los megapíxeles por ID
def mostrar_megapixeles(ids):
    megapixeles = data.loc[data['id'].isin(ids), ['id', 'px_height', 'px_width']]
    megapixeles['megapixeles'] = megapixeles['px_height'] * megapixeles['px_width'] / 1000000

    # Crear gráfica de megapíxeles
    plt.bar(megapixeles['id'], megapixeles['megapixeles'])
    plt.xlabel('ID del móvil')
    plt.ylabel('Megapíxeles')
    plt.title('Megapíxeles por ID')
    plt.show()


# Función para mostrar la capacidad de la batería por battery power
def mostrar_capacidad_bateria(ids):
    capacidad_bateria = data.loc[data['id'].isin(ids)]
    capacidad_bateria_count = capacidad_bateria['battery_power'].value_counts().reset_index()
    capacidad_bateria_count.columns = ['Battery Power', 'Cantidad']

    # Crear gráfica de capacidad de la batería
    plt.bar(capacidad_bateria_count['Battery Power'], capacidad_bateria_count['Cantidad'])
    plt.xlabel('Battery Power')
    plt.ylabel('Cantidad')
    plt.title('Capacidad de la batería por Battery Power')
    plt.show()