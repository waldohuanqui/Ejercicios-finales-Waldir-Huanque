import pandas as pd
import sqlite3

datos_csv = pd.read_csv('archivo.csv')

conn = sqlite3.connect('basedatos.db')

datos_csv.to_sql('tabla_datos', conn, if_exists='replace', index=False)

conn.close()

import sqlite3

def leer_datos():
    conn = sqlite3.connect('basedatos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tabla_datos')

    datos = cursor.fetchall()

    for fila in datos:
        
        valor1 = fila[0]
        valor2 = fila[1]
        print(f"Valor1: {valor1}, Valor2: {valor2}")

    cursor.close()
    conn.close()
leer_datos()
