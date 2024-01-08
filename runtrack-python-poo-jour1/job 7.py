class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Instanciation de la classe Personnage
personnage = Personnage()

# Affichage de la position initiale du personnage
print("Position initiale :", personnage.position())

# Déplacement du personnage vers la droite
personnage.droite()

# Affichage de la nouvelle position du personnage
print("Nouvelle position :", personnage.position())

# Déplacement du personnage vers le haut
personnage.haut()

# Affichage de la nouvelle position du personnage
print("Nouvelle position :", personnage.position())
