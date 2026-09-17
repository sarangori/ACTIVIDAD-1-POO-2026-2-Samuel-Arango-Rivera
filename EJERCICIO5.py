class Ejercicio5:

    def __init__(self, valor_x=20, valor_y=40):
        self.suma = 0
        self.x = valor_x
        self.y = valor_y

    
    def calcular_suma(self):
        
        
        self.suma = self.suma + self.x
        
        
        self.x = self.x + self.y ** 2
        
        
        self.suma = self.suma + self.x / self.y
        
        
        print(f"EL VALOR DE LA SUMA ES: {self.suma}")
        


if __name__ == "__main__":
    
    ejercicio = Ejercicio5()
    ejercicio.calcular_suma()
    
    