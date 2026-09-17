class Ejercicio:
    
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 40

    def realizar_calculos(self):
        self.suma = self.suma + self.x
        
        self.x = self.x + self.y ** 2
        
        self.suma = self.suma + self.x / self.y

    def mostrar_resultado(self):
        print("EL VALOR DE LA SUMA ES:", self.suma)


ejercicio = Ejercicio()

ejercicio.realizar_calculos()

ejercicio.mostrar_resultado()
    