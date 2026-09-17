class Numero:
    def __init__(self):
        self.NUM = 0
        self.CUADRADO = 0
        self.CUBO = 0

    def calcular(self):
        self.CUADRADO = self.NUM ** 2
        self.CUBO = self.NUM ** 3

    def mostrar(self):
        print("CUADRADO:", self.CUADRADO)
        print("CUBO:", self.CUBO)



numero = Numero()

numero.NUM = int(input("Ingrese un numero: "))

numero.calcular()

numero.mostrar()