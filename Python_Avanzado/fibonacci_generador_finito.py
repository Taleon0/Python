from time import sleep

def fiboGen(max=None):
    numero_1 = 0
    numero_2 = 1

    while True:
        if max !=None and numero_1 > max:
            print("Se ha alcanzado el numero maximo")
            break
        yield numero_1
        auxiliar = numero_1 + numero_2
        numero_1, numero_2 = numero_2, auxiliar

if __name__=="__main__":
    n = int(input("Escribe el numero tope para la serie fibonacci: "))
    fibonacci = fiboGen(n)
    for element in fibonacci:
        print(element)
        sleep(1)