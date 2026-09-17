class Familia:
    def __init__(self):
        self.EDJUAN = 0
        self.EDALBER = 0
        self.EDANA = 0
        self.EDMAMA = 0

    def edades(self):
        self.EDALBER = 2 * self.EDJUAN / 3
        self.EDANA = 4 * self.EDJUAN / 3
        self.EDMAMA = self.EDALBER + self.EDJUAN + self.EDANA

    def mostrar_edades(self):
        print("LAS EDADES SON:")
        print("ALBERTO:", int(self.EDALBER), "JUAN:", int(self.EDJUAN))
        print("ANA:", int(self.EDANA), "MAMA:", int(self.EDMAMA))



familia = Familia()

familia.EDJUAN = int(input("Ingrese la edad de Juan: "))

familia.edades()

familia.mostrar_edades()

