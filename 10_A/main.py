import pandas as pd
import matplotlib.pyplot as plt
from Funciones import act1,act2,act3
def main():
    df = pd.read_csv('data.csv')
    num_paises = 10
    act1(df,num_paises)
    act2(df,num_paises)
    act3(df,num_paises)

main()