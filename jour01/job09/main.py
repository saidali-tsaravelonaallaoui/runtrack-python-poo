class Produit:
    def __init__(self, nom, prix_HT, TVA):
        self.nom = nom
        self.prix_HT = prix_HT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prix_HT * (1 + self.TVA / 100)

    def afficher(self):
        print("Informations du produit:")
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prix_HT} €")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.calculerPrixTTC()} €")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix_HT):
        self.prix_HT = nouveau_prix_HT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prix_HT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Enceinte Bose", 800, 20)
produit2 = Produit("Téléphone", 500, 10)
produit3 = Produit("Imprimante", 200, 15)

produit1.afficher()
print("\n")
produit2.afficher()
print("\n")
produit3.afficher()

produit1.modifierNom("Nouvel ordinateur")
produit1.modifierPrixHT(900)

print("\nNouvelles informations du produit 1:")
produit1.afficher()
