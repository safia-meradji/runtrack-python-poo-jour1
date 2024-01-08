class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix HT du produit : {self.prixHT} €")
        print(f"TVA du produit : {self.TVA}%")
        print(f"Prix TTC du produit : {self.calculerPrixTTC()} €")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit(nom="Ordinateur", prixHT=800, TVA=20)
produit2 = Produit(nom="Smartphone", prixHT=400, TVA=15)

# Affichage des informations initiales des produits
print("Informations initiales pour le Produit 1:")
produit1.afficher()

print("\nInformations initiales pour le Produit 2:")
produit2.afficher()

# Modification du nom et du prix pour chaque produit
produit1.modifierNom("Laptop")
produit1.modifierPrixHT(900)

produit2.modifierNom("Téléphone")
produit2.modifierPrixHT(450)

# Affichage des nouvelles informations des produits
print("\nInformations modifiées pour le Produit 1:")
produit1.afficher()

print("\nInformations modifiées pour le Produit 2:")
produit2.afficher()
