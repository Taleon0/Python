def make_division_by(n):
    def division(d):
        assert type(d) == int, "Solo se puede calcular con valores enteros"
        assert n != 0, "No es posible dividir por cero"
        return d/n
    return division

def main():
    division_by_3= make_division_by(3)
    print(division_by_3(18)) # Se espera que la salida sea 6
    division_by_5=make_division_by(5)
    print(division_by_5(100)) # se espera que la salida sea 20
    division_by_18 = make_division_by(18)
    print(division_by_18(54)) # Se espera que la salida sea 3

if __name__=="__main__":
    main()