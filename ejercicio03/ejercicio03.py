import re

def validar_entrada(entrada, tipo):
    if tipo == "numerica":
        patron = r'^\d+$'
        descripcion = "numérica"
    elif tipo == "texto":
        patron = r'^[a-zA-Z\s]+$'
        descripcion = "de texto"
    elif tipo == "email":
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        descripcion = "de email"
    elif tipo == "celular":
        patron = r'^\d{10}$'
        descripcion = "de celular (10 dígitos)"
    else:
        return False
    
    if re.match(patron, entrada):
        print(f"La entrada '{entrada}' es válida ({descripcion}).")
        return True
    else:
        print(f"La entrada '{entrada}' no es válida ({descripcion}).")
        return False





validar_entrada("12345", "numerica")
validar_entrada("Hello World", "texto")
validar_entrada("john@example.com", "email")
validar_entrada("1234567890", "celular")
validar_entrada("abc123", "otro_tipo")