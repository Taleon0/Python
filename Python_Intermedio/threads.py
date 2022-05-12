import threading
import time

def hola_mundo(nombre):
    print('Hola mundo '+nombre)
    time.sleep(3)

if __name__ == "__main__":
    hilo = threading.Thread(target=hola_mundo, args=("Tati",))
    hilo.start()
    print("Esto es en el main")
