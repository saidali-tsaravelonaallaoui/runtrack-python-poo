class Livre:
    def __init__(self, titre, auteur, nbre_page):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbre_page = nbre_page
        self.__disponible = False
  
    # Assesseurs (getters)
    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur
    
    def getNbre_page(self):
        return self.__nbre_page
    
    def Disponible(self):
        return self.__disponible
    
    # Mutateurs (setters)
    def setTitre(self, new_titre):
        self.__titre = new_titre
        
    def setAuteur(self, new_auteur):
        self.__auteur = new_auteur
    
    def setNbre_page(self, new_nbre_page):
        if isinstance(new_nbre_page, int) and new_nbre_page > 0:
            self.__nbre_page = new_nbre_page
        else:
            print("\nErreur : Le nombre de pages doit être un nombre entier positif.")
            
    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            print("\nEmprunt du livre en cours...")
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("\nLe livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            print("\nRetour du livre en cours...")
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("\nLe livre est maintenant disponible.")
        
livre = Livre("Apprendre à programmer avec Python 3","Gérard Swinnen", 60)

print("Titre :", livre.getTitre())
print("Auteur :",livre.getAuteur())
print("Nombres de pages :",livre.getNbre_page(),"pages")

# Vérification de la disponibilité
print("\nLe livre est disponible :", livre.verification())

livre.emprunter()

# Tentative de ré-emprunt du livre
livre.emprunter()

# Rendre le livre
livre.rendre()

# Tentative de rendre à nouveau le livre
livre.rendre()