# Sugar sintax o azucar sintactica, se utiliza para hacer un poco mas ameno el codigo

def decorador(func):
    def envoltura():   # por lo general el nombre es envoltura o wrapper
        print("Esto se añade a mi funcion original")
        func()
    return envoltura

@decorador   # esto significa que de una vez se returna la funcion decorador pasandole la funcion de abajo
def saludo():
    print("Hola")

saludo()