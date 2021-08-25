# Se crea una funcion anonima con solo una linea de codigo que es asignada directamente a una variable


def main():
    palindrome = lambda name : name == name[::-1]
    print(palindrome('ana'))


if __name__=='__main__':
    main()