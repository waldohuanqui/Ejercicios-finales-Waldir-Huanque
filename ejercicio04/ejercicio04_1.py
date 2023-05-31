import pandas as pd
import numpy as np

datos_csv = pd.read_csv('archivo.csv')
datos_excel = pd.read_excel('archivo.xlsx')
datos_json = pd.read_json('archivo.json')

datos_filtrados = datos_csv[datos_csv['columna'] > 100]

datos_filtrados = datos_excel[(datos_csv['columna1'] > 100) & (datos_csv['columna2'] == 'valor')]


datos_combinados = pd.concat([datos_csv, datos_excel, datos_json])


datos_csv['nueva_columna'] = datos_csv['columna1'] + datos_csv['columna2']

datos_csv['nueva_columna'] = np.where(datos_csv['columna'] > 100, 'Mayor', 'Menor')

