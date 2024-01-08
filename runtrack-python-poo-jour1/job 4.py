class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes
personne1 = Personne(nom="Doe", prenom="John")
personne2 = Personne(nom="Dupont", prenom="Jean")

# Appel de la méthode SePresenter pour chaque personne
presentation1 = personne1.SePresenter()
presentation2 = personne2.SePresenter()

# Impression des présentations en console
print(presentation1)
print(presentation2)
