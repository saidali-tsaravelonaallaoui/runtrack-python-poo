class Livre:
    def __init__(self, titre, auteur, nbre_page):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbre_page = nbre_page
  
    # Assesseurs (getters)
    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur
    
    def getNbre_page(self):
        return self.__nbre_page
    
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
        
livre = Livre("Apprendre à programmer avec Python 3","Gérard Swinnen", 60)

print("Titre :", livre.getTitre())
print("Auteur :",livre.getAuteur())
print("Nombres de pages :",livre.getNbre_page(),"pages")

livre.setNbre_page(50)
print("\nTitre du Livre :", livre.getTitre(), "de l'Auteur",livre.getAuteur(),"avec",livre.getNbre_page(),"pages d'exercices corrigés !")