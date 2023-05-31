from datetime import datetime

def registrar_evento(nombre_archivo, nombre_evento):
    fecha_actual = datetime.now()
    formato_fecha = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
    nombre_archivo = nombre_archivo.replace(" ", "-")
    nombre_evento = nombre_evento.replace(" ", "-")
    
    log_entry = f"{formato_fecha}-{nombre_archivo}-{nombre_evento}"
    
    with open("info.log", "a") as archivo_log:
        archivo_log.write(log_entry + "\n")
    
    print("Evento registrado correctamente en info.log.")

registrar_evento("mi_archivo.txt", "evento_importante")
