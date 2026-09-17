class Empleado:
    def __init__(self):
        self.HORAS = 0
        self.VALORHORA = 0
        self.SALBRUTO = 0
        self.RETENCION = 0
        self.SALNETO = 0

    def calcular_salario(self):
        self.SALBRUTO = self.HORAS * self.VALORHORA
        self.RETENCION = self.SALBRUTO * 12.5 / 100
        self.SALNETO = self.SALBRUTO - self.RETENCION

    def mostrar_resultados(self):
        print("SALARIO BRUTO:", self.SALBRUTO)
        print("RETENCION:", self.RETENCION)
        print("SALARIO NETO:", self.SALNETO)

empleado = Empleado()

empleado.HORAS = int(input("Ingrese las horas trabajadas: "))
empleado.VALORHORA = int(input("Ingrese el valor de la hora: "))

empleado.calcular_salario()

empleado.mostrar_resultados()