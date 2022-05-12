#Los iteradores manejan la formulas matematicas para crear sucesiones incluso infinitas 
import time

class FiboIter():
    def __init__(self, max=None):
        self.max=max

    def __iter__(self):
        self.number_1 = 0
        self.number_2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.number_1
        elif self.counter == 1:
            self.counter += 1
            return self.number_2
        else:
            self.auxiliar = self.number_1 + self.number_2
            # self.number_1 = self.number_2
            # self.number_2 = self.auxiliar
            self.number_1, self.number_2 = self.number_2, self.auxiliar  # swaping o intercambio
            self.counter += 1
            if not self.max:
                return self.auxiliar
            if self.max:
                if self.auxiliar >= self.max:
                    print("Numero maximo alcanzado")
                    raise StopIteration
                else:
                    return self.auxiliar


if __name__=="__main__":
    fibonacci = FiboIter(100)  # instanciar la clase
    for element in fibonacci:
        print(element)
        time.sleep(1) # Se pausa un segundo despues de imprimir 

