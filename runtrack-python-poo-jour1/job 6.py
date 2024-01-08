class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"L'âge de l'animal est {self.age} ans")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

    def afficherNom(self):
        print(f"L'animal se nomme {self.prenom}")

# Instanciation de la classe Animal
animal_instance = Animal()

# Affichage de l'âge initial de l'animal
animal_instance.afficherAge()

# Faire vieillir l'animal
animal_instance.vieillir()

# Affichage de l'âge après avoir vieilli
animal_instance.afficherAge()

# Nommer l'animal
animal_instance.nommer("Luna")

# Affichage du nom de l'animal
animal_instance.afficherNom()
