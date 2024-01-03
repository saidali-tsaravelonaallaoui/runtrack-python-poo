class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        infos = f"Nom du produit : {self.nom}\n"
        infos += f"Prix HT : {self.prixHT}\n"
        infos += f"TVA : {self.TVA}%\n"
        infos += f"Prix TTC : {self.calculerPrixTTC()}"
        return infos
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    def recupererNom(self):
        return self.nom
    
    def recupererPrixHT(self):
        return self.prixHT
    
    def recupererTVA(self):
        return self.TVA

produit1 = Produit("Banane", 10, 5)
produit2 = Produit("Télé", 12000, 20)
print("Informations initiales :")
print("Produit 1 :")
print(produit1.afficher())
print("\nProduit 2 :")
print(produit2.afficher())
produit1.modifierNom("Cahier")
produit1.modifierPrixHT(10)
produit2.modifierNom("PC portable")
produit2.modifierPrixHT(1500)
print("\nNouveaux prix des produits :")
print("Produit 1 :")
print(f"Nouveau prix HT du produit 1 : {produit1.getPrixHT()}")
print("Prix TTC du produit 1 :", produit1.calculerPrixTTC())
print("\nProduit 2 :")
print(f"Nouveau prix HT du produit 2 : {produit2.getPrixHT()}")
print("Prix TTC du produit 2 :", produit2.calculerPrixTTC())