import pandas as pd
import matplotlib.pyplot as plt

def act1(dataframe, num_paises):
    paises = dataframe['location'].unique()[:num_paises]
    df_paises = dataframe[dataframe['location'].isin(paises)].copy()
    df_paises['date'] = pd.to_datetime(df_paises['date'])
    df_paises['month_year'] = df_paises['date'].dt.to_period('M')
    casos_por_mes = df_paises.groupby(['location', 'month_year'])['total_cases'].sum()

    plt.figure(figsize=(10, 5))
    for pais in casos_por_mes.index.get_level_values(0).unique():
        casos_pais = casos_por_mes[pais]
        casos_pais = casos_pais.astype(str)
        plt.plot(casos_pais.index.astype(str), casos_pais.values, label=pais)
    plt.xlabel('Mes')
    plt.ylabel('Total de casos')
    plt.xticks(rotation=45)
    plt.legend()
    plt.title('Casos totales por mes')
    plt.show()


def act2(dataframe, num_paises):
    paises = dataframe['location'].unique()[:num_paises]
    df_paises = dataframe[dataframe['location'].isin(paises)].copy()
    df_paises['date'] = pd.to_datetime(df_paises['date'])
    df_paises['month_year'] = df_paises['date'].dt.to_period('M')
    muertes_por_mes = df_paises.groupby(['location', 'month_year'])['total_deaths'].sum()

    plt.figure(figsize=(10, 5))
    for pais in muertes_por_mes.index.get_level_values(0).unique():
        muertes_pais = muertes_por_mes[pais]
        muertes_pais = muertes_pais.astype(str)
        plt.plot(muertes_pais.index.astype(str), muertes_pais.values, label=pais)
    plt.xlabel('Mes')
    plt.ylabel('Total de muertes')
    plt.xticks(rotation=45)  #
    plt.legend()
    plt.title('Muertes totales por país')

    plt.yticks([0, 500, 1000, 1500, 2000], ['0-500', '500-1000', '1000-1500', '1500-2000', '>2000'])

    plt.show()


def act3(dataframe, num_paises):
    paises = dataframe['location'].unique()[:num_paises]
    df_paises = dataframe[dataframe['location'].isin(paises)].copy()
    df_paises['date'] = pd.to_datetime(df_paises['date'])
    df_paises['month_year'] = df_paises['date'].dt.to_period('M')
    muertes_por_mes = df_paises.groupby(['month_year', 'location'])['total_deaths'].sum()

    plt.figure(figsize=(10, 5))
    for pais in muertes_por_mes.index.get_level_values(1).unique():
        muertes_pais = muertes_por_mes[:, pais]
        muertes_pais = muertes_pais.astype(str)
        plt.plot(muertes_pais.index.astype(str), muertes_pais.values, label=pais)
    plt.xlabel('Mes')
    plt.ylabel('Total de muertes')
    plt.xticks(rotation=45)
    plt.legend()
    plt.title('Muertes por mes por país')

    plt.yticks([0, 500, 1000, 1500, 2000], ['0-500', '500-1000', '1000-1500', '1500-2000', '>2000'])

    plt.show()
