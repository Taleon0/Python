# Creando el iterador

my_list=[1, 2, 3, 4, 5, 6]
my_iter = iter(my_list)

# Iterando un iterador

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

# o con el ciclo for que es un sugar sintax del while con el try catch

for element in my_list:
    print(element)
