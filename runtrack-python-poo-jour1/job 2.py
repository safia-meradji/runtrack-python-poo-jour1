class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def afficher_nombres(self):
        print("Le nombre 1 est", self.nombre1)
        print("Le nombre 2 est", self.nombre2)

# Instanciation de la classe
operation_instance = Operation(nombre1=12, nombre2=3)

# Appel de la méthode pour afficher les nombres en console
operation_instance.afficher_nombres()
