with open('archivo.bin', 'rb') as file:
    file.seek(2) # Mueve el puntero
    data = file.read(2) # Lee x bytes
    print(data)