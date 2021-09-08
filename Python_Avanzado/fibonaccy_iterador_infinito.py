#Los iteradores manejan la formulas matematicas para crear sucesiones incluso infinitas 
import time

class FiboIter():
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
            return self.auxiliar

if __name__=="__main__":
    fibonacci = FiboIter()  # instanciar la clase
    for element in fibonacci:
        print(element)
        time.sleep(1) # Se pausa un segundo despues de imprimir 