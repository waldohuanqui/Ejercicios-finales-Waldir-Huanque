import requests
import sqlite3

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        tipo_cambio = response.json()
        
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS tipo_cambio
                          (moneda TEXT, compra NUMERIC, venta NUMERIC)''')
        
        cursor.execute("INSERT INTO tipo_cambio VALUES (?, ?, ?)",
                       (tipo_cambio['moneda'], tipo_cambio['compra'], tipo_cambio['venta']))
        
        conn.commit()
        conn.close()
        print("Datos insertados correctamente en la base de datos.")
    else:
        print("Error al obtener el tipo de cambio.")

obtener_tipo_cambio()