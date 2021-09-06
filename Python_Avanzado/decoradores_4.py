from datetime import datetime

#Decorador para determinar el tiempo que demora una funcion en ejecutarse
def execution_time(func):
    def wrapper(*args, **kwargs):  # *args: no importa la cantidad de argumentos posicionales que se le envien
        initial_time=datetime.now()
        func(*args, **kwargs)  # # **kwargs: no importa la cantidad de argumentos nombrados que se le envien
        final_time=datetime.now()
        time_elapse = final_time-initial_time
        print(f"Pasaron {time_elapse.total_seconds()} segundos")  # total_seconds es lo que nos permite ver el tiempo en segundos
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000):
        pass


@execution_time
def suma(a:int, b:int) -> int:
    return a+b

suma(5,5)
#random_func()


