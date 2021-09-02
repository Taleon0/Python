def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Escribe un numero entero: "))

print(fibonacci(n))

"""     EXPLICACION:
    Para n=5
    f(5-1)+f(5-2) Es decir f(4) + f(3) --> necesitamos saber cuanto valen
    Pero cuanto vale f(4) pues pasa a ser n=4
    f(4-1)+f(4-2) Es decir f(3) + f(2) --> necesitamos saber cuanto valen
    Pero cuanto vale f(3) pues pasa a ser n=3
    f(3-1)+f(3-2) Es decir f(2) + f(1) --> necesitamos saber cuanto valen
    Pero cuanto vale f(2) pues pasa a ser n=2
    f(2-1)+f(2-2) Es decir f(1) + f(0) --> necesitamos saber cuanto valen

    La condicional dice que si n==0 o n==1 entonces f(1) y f(0) valen 1, es decir

    f(2) = f(1) + f(0) = 1 + 1 = 2
    f(3) = f(2) + f(1) = 2 + 1 = 3
    f(4) = f(3) + f(2) = 3 + 2 = 5
    f(5) = f(4) + f(3) = 5 + 3 = 8

"""