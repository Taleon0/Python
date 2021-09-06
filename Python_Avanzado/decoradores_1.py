def decorador(func):
    def envoltura():
        print("Esto se añade a mi funcion original")
        func()
    return envoltura

def saludo():
    print("Hola")

saludo()  #Solo imprime Hola

saludo = decorador(saludo)
saludo()  # Imprime la modificacion realizada por la funcion decorador + Hola