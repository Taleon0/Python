def read():
    numbers = []
# Para leer un archivo se usa with open -- r para lectura -- w para escritura -- a para agregar al final sin reemplazar
    with open("./archivos/numbers.txt","r",encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Maria","Andres","Gonzalo","Marcela","Ana Maria","Ñoño","Pacho"]
# Si se va a escribir un archivo, como en este caso y no existe, python lo crea
    with open("./archivos/names.txt","w",encoding="utf-8") as wr:
        for name in names:
            wr.write(name)
            wr.write("\n")


def main():
    read()
    write()


if __name__=="__main__":
    main()