# Los sets son una estructura en la cual no se permiten elementos repetidos 
# y sus elementos son inmutables, esta estructura no tiene orden, por lo cual
# no es posible llamar elementos por subindices

my_set = {3, 4, 5}
print(f"my_set = {my_set}")
my_set2 = {"Hola",23.3, False, True}
print(f"my_set 2 = {my_set2}")
my_set3 = {3, 3, 5}  # Al incluir elementos repetidos se eliminan los duplicados al guardarse
print(f"my_set 3 = {my_set3}")

"""
my_set4 = {[3, 4, 5],6}  # Genera error debido a que contiene una lista, que es un elemento mutable
print(f"my_set = {my_set4}")
"""

# Creacion de set vacios

empty_dic={} # por defecto se crea como un diccionario
empty_set=set() # se crea como un set

# Cateo a conjuntos (set)

my_list = [1, 1, 2, 2, 3, 3, 4]
my_tuple = ("Hola","Hola","Hola",1)
my_cast_list_to_set = set(my_list)  # Elimina duplicados
my_cast_tuple_to_set = set(my_tuple) # Elimina duplicados
print(f"El resultado del casteo de lista es: {my_cast_list_to_set}")
print(f"El resultado del casteo de tupla es: {my_cast_tuple_to_set}")

#Agregar datos al set

print(f"my_set = {my_set}")
    # Añadir un elemento
my_set.add(2)
print(f"my_set luego de agregar 2 = {my_set}")
    # Añadir varios elementos
my_set.update([1,2,7])
print(f"my_set luego de agregar 1, 2, 7 = {my_set}")
    # Añadir multiples elementos
my_set.update([12,15,1,2],{6,8,9,11})
print(f"my_set luego de agregar 12, 15, 1, 2, 6, 8, 9, 11 = {my_set}")

# Eliminar el elemento del set

my_set.discard(1)
print(f"my_set luego de eliminar el 1: {my_set}")
my_set.remove(2)
print(f"my_set luego de eliminar el 2: {my_set}")
    # Elementos inexistentes
my_set.discard(1) # No genera error al no encontrar un elemento que borrar
print(f"my_set luego de eliminar el 1: {my_set}")
"""
my_set.remove(2) # Genera error al no encontrar un elemento que borrar
print(f"my_set luego de eliminar el 2: {my_set}")
"""
    #Borrar elemento aleatorio
my_set.pop()
print(f"my_set luego de eliminar un elemento aleatorio: {my_set}")
    # Borrar todos los elementos del set
my_set.clear()
print(f"my_set luego de eliminar todos los elementos: {my_set}")
