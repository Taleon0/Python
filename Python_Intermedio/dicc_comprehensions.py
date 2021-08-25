from math import sqrt
# Crea un diccionario con ciertos criterios sin necesidad de usar funciones

# Obtener los numeros del 1 al 100 elevados al cubo
def main():
    my_dicc={}
    print('\nSolucion metodo tradicional\n')
    for i in range(1,101):
        if i % 3 != 0: #  Muestra solo los numeros que no son multiplo de 3
            my_dicc[i]=i**3
    print(my_dicc)
    print('\nSolucion por dicc_comprehensions (key:value for key in iterable if condition)\n')
    my_dicc_comprehensions={i : i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dicc_comprehensions)
    print('\nSolucion diccionario cuyas llaves sean los primeros 1000 numeros naturales con sus '+
            'raices cuadradas como valores\n')
    my_dicc_homework={i:round(sqrt(i),2) for i in range(1,1001)}
    print(my_dicc_homework)

if __name__ == '__main__':
    main()