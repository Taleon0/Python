# Funcion de orden superior
'''
def saludo(func):
    func()


def hola():
    print('Hola ! ! !')


def adios():
    print('Adios :(')


saludo(hola)
saludo(adios)

'''
# Hay 3 funciones de orden superior importante: FILTER - MAP - REDUCE


# Uso de filter : de una lista tomar todos los numeros que sean impares

my_list = [1,2,3,4,5,6,7,8,9,13,19,21]

odd = list(filter(lambda x: x%2 != 0, my_list))

print(f"Resultado de filter {odd}")


# Uso de map: de una lista, elevar todos los numeros al cuadrado

my_list_2 = [1,2,5,3,6,8,4]

sqares = list(map(lambda x: x**2, my_list_2))

print(f"Resultado de map {sqares}")


# Uso de reduce: en una lista donde todos los valores son iguales, los reduce (multiplicando entre si)

from functools import reduce

my_list_3 = [2,2,2,2,2]

all_multiplied = reduce(lambda a, b : a * b, my_list_3)

print(f"Resultado de reduce {all_multiplied}")
