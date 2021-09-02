objetivo = int(input("Escoge un numero: "))  # Numero a calcular la raiz cuadrada
epsilon = 0.01  # Margen de error
bajo = 0.0  # valor minimo del rango
alto = max(1.0, objetivo) # valor maximo del rango a validar
respuesta = (alto+bajo) / 2 # valor medio del conjunto, de aqui se apoyara el programa para saber si toma el rango superior o inferior

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f"El alto es = {alto}, el bajo es = {bajo} y la respuesta es {respuesta}")
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo)/2

print(f"La raiz cuadrada de {objetivo} es {respuesta}")