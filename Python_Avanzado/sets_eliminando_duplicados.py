# Por medio de una funcion y sin sets ---------------------------------------------

def remove_duplicates(someList):
    without_duplicates=[]
    for element in someList:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list=[1,1,2,1,2,3,6,5,2,2,3,3,5]
    print(f"El resultado de eliminar duplicados de la lista {random_list} es: {remove_duplicates(random_list)}")

# Por medio de sets -----------------------------------------------------------------

def main():
    random_list=[1,1,2,1,2,3,6,5,2,2,3,3,5]
    print(f"El resultado de eliminar duplicados de la lista {random_list} es: {set(random_list)}")


if __name__=="__main__":
    run()
    main()
