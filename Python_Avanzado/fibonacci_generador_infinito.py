from time import sleep, time
def fiboGen():
    numero_1 = 0
    numero_2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield numero_1
        elif counter == 1:
            counter += 1
            yield numero_2
        else:
            auxiliar = numero_1 + numero_2
            numero_1, numero_2 = numero_2, auxiliar
            counter += 1
            yield auxiliar

if __name__=="__main__":
    fibonacci = fiboGen()
    for element in fibonacci:
        print(element)
        sleep(1)
