import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('data.csv')

# Todas las funciones muestran solo 10 ciudades, en este caso las 10 primeras

# Función para mostrar la población por ciudad
def act1(data):

    # Se mostrara un gráfico de pastel con las 10 ciudades que tienen mas poblacion.

    data['Population'] = data['Population'].str.replace(',', '').fillna(0).astype(int)
    top_10 = data.nlargest(10, 'Population')
    labels = top_10['City']
    sizes = top_10['Population']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Población por ciudad')
    plt.show()

# Función para mostrar la densidad por km2
def act2(data):
    #Se muestra un gráfico de pastel con la densidad por km2 de las 10 ciudades con mayor densidad por KM2.

    data['Density KM2'] = data['Density KM2'].str.replace(',', '').fillna(0).astype(int)
    top_10 = data.nlargest(10, 'Density KM2')
    labels = top_10['City']
    sizes = top_10['Density KM2']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Densidad por km2')
    plt.show()

# Función para mostrar la densidad por m2
def act3(data):

    #Se muestra un gráfico de pastel con la densidad por m2 de las 10 ciudades con mayor densidad por m2

    data['Density  M2'] = data['Density  M2'].str.replace(',', '').fillna(0).astype(int)
    top_10 = data.nlargest(10, 'Density  M2')
    labels = top_10['City']
    sizes = top_10['Density  M2']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Densidad por m2')
    plt.show()
