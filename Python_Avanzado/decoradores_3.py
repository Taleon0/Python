# Decorador que se crea para imprimir los strings en mayusculas

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"

print(mensaje("Cesar"))
