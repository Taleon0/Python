# Lista de diccionarios

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
# List comprehension para traer la info de todos los trabajadores que tienen de lenguaje python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    print("Trabajadores que conocen el lenguaje python: ")
    for worker in all_python_devs:
        print(worker)
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    print("Trabajadores que se encuentran en Platzi: ")
    for worker in all_Platzi_workers:
        print(worker)

# High order functions
    adults = list(filter(lambda worker: worker["age"]>18,DATA)) # para que nos traiga los diccionarios que coinciden
    adults = list(map(lambda worker: worker["name"], adults)) # para que nos traiga solo los nombres del resultado anterior
    print("Trabajadores mayores a 18 años:")
    for worker in adults:
        print(worker)
    
# Sumar informacion al diccionario existente segun una condicion
    old_people = list(map(lambda worker: worker | {"old": worker["age"]>70} ,DATA))
    print("lista de trabajadores con informacion de si son mayores a 70 años")
    for worker in old_people:
        print(worker)

if __name__=="__main__":
    main()