import pandas as pd
from Funciones import act1,act2,act3

# Leemos el archivo CSV
df = pd.read_csv('data.csv')

def main():
    # Llamar a las funciones para que se visualizen los graficos de cada uno
    act1(df)
    act2(df)
    act3(df)

#Llamamos a la funcion
main()