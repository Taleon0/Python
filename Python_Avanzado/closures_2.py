# programa que repite cierta cantidad de veces un string

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"  #afirma que es string es un string o genera el mensaje puesto
        return string*n
    return repeater

def run():
    repeat5 = make_repeater_of(5)
    repeat8 = make_repeater_of(8)
    print(repeat5("Hola "))
    print(repeat8("Platzi, "))

if __name__== "__main__":
    run()