# Programa creado para leer palindromos teniendo tipado estatico

def is_palindrome(string:str) -> bool:
    string=string.replace(" ","").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("ana")) # Si se pone un numero genera error de typo

if __name__=="__main__":
    run()

# mypy palindrome.py --check-untyped-defs -- luego de instalar mypy este comando muestra si uno puso un tipo de dato inconsistente