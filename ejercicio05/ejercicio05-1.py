import sqlite3

import ejercicio05

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
