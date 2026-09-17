class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

    def calcular_longitud(self):
        return 2 * 3.1416 * self.radio

    def mostrar_resultados(self):
        print("El área del círculo es:", self.calcular_area())
        print("La longitud de la circunferencia es:", self.calcular_longitud())


radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)

circulo.mostrar_resultados()