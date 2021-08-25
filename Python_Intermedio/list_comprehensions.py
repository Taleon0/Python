# Crea una lista con ciertos criterios sin necesidad de usar funciones


# Obtener los numeros del 1 al 100 elevados al cuadrado
def main():
    squares = []
    print('\nSolucion metodo tradicional\n')
    for i in range(1,101):
        if i % 3 != 0:  #  Muestra solo los numeros que no son multiplo de 3
            squares.append(i**2)
    print(squares)
    print('\nSolucion por list_comprehensions (element for element in iterable if condition)\n')
    squares_list_comprehensions = [i ** 2 for i in range(1,101) if i % 3 != 0]
    print(squares_list_comprehensions)
    print('\nSolucion lista de todos los multiplos de 4 que tambien son multiplos de 6 y 9 hasta 5 digitos en numero\n')
    homework=[i for i in range(1,100000) if i % 4 == 0 if i % 6 == 0 if i % 9 == 0]
    print(homework)
if __name__ == '__main__':
    main()
