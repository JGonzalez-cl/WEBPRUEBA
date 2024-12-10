data = b'\x42\x43\x44' # Datos en binario
with open('archivo.bin' , 'wb') as file:
    file.write(data) # Escribe la secuencia binaria en el fichero