# Los generadores son un sugar sintax de los iteradores
# yield es lo mismo que return pero no termina la funcion, sino la pausa

# Generator expression
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

my_second_list = [x*2 for x in my_list]  #List Comprehension
my_secong_gen = (x*2 for x in my_list)  # Generator expression

