# Las operaciones de sets son las de conjuntos

# Union (resultado de combinar todos los elementos de un conjunto quitando los repetidos)
my_set1 = {3,4,5}
my_set2 = {5,6,7}
my_set3 = my_set1 | my_set2
print(f"El resultado de la union de {my_set1} y {my_set2} es {my_set3}")

# Interseccion (combina ambos sets pero obtiene solo los elementos que tienen en comun)
my_set3 = my_set1 & my_set2
print(f"El resultado de la interseccion de {my_set1} y {my_set2} es {my_set3}")

# Diferencia (muestra los datos que se encuentran en el set que no estan en el otro)
my_set3 = my_set1 - my_set2
print(f"El resultado de la diferencia entre {my_set1} y {my_set2} es {my_set3}")
my_set3 = my_set2 - my_set1
print(f"El resultado de la diferencia de {my_set2} y {my_set1} es {my_set3}")

# Diferencia simetrica (se obtienen todos los elementos menos los que se interceptan)
my_set3 = my_set1 ^ my_set2
print(f"El resultado de la diferencia simetrica de {my_set1} y {my_set2} es {my_set3}")
