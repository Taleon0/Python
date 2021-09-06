from typing import Dict, List, Tuple

# para declarar un tipo estatico es con a:tipodato

a: int = 5
print(a)
b: str = 'Hola'
print(b)
c: bool = True
print(c)

def suma(x: int, y: int) -> int:  #La flecha es para indicar que la funcion devielve un entero
    return x + y

print(suma(1,2))

# Para diccionarios y listas se impotan Dict y List del modulo typing

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str,int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45
},

countries: List[Dict[str,str]] = [{
    'name':'argentina',
    'people': '450000'
},
{
    'name':'mexico',
    'people':'9000000'
},
{
    'name':'colombia',
    'people':'9999999999'
}
]

numbers: Tuple[int, float, int] = (1, 0.5, 2)
