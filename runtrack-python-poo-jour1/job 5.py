class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Instanciation de la classe Point
point_instance = Point(x=3, y=5)

# Appel des méthodes pour afficher les coordonnées du point
point_instance.afficherLesPoints()

# Appel des méthodes pour afficher x et y
point_instance.afficherX()
point_instance.afficherY()

# Changement des valeurs de x et y
point_instance.changerX(8)
point_instance.changerY(12)

# Appel de nouveau des méthodes pour afficher les coordonnées du point
point_instance.afficherLesPoints()
