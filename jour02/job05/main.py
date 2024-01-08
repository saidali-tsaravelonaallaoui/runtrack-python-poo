class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoire = 50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = True
        self.__reservoire = reservoire
        
    # Assesseurs (getters)
    def getMarque(self):
        return self.__marque
    
    def getModele(self):
        return self.__modele
    
    def getAnnee(self):
        return self.__annee
    
    def getKilometrage(self):
        return self.__kilometrage
    
    def getEn_marche(self):
        return self.__en_marche
    
    def getReservoire(self):
        return self.__reservoire
    
    # Mutateurs (setters)
    def setMarque(self, new_marque):
        self.__marque = new_marque
        
    def setModele(self, new_modele):
        self.__modele = new_modele
        
    def setAnnee(self, new_annee):
        self.__annee = new_annee
    
    def setKilometrage(self, new_kilometrage):
        self.__kilometrage = new_kilometrage
        
    def setEn_marche(self, new_etat):
        self.__en_marche = new_etat
        
    def setReservoire(self, new_reservoire):
        self.__reservoire = new_reservoire
        
    # Méthodes pour démarrer et arrêter la voiture
    def demarrer(self):
        if self._verifier_plein():
            self.__en_marche = True
            print("\nEn marche:", voiture.getEn_marche())
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer : réservoir insuffisant.")
        
    def arreter(self):
        self.__en_marche = False
        print("\nLa voiture s'arrête.")
        print("En marche:", voiture.getEn_marche())
        
    # Methode verif plein 
    def _verifier_plein(self):
        return self.__reservoire > 5
    
    # Methode affiche voiture
    def VoitureInfo(self):
        print("Marque :", voiture.getMarque())
        print("Modèle :", voiture.getModele())
        print("Année :", voiture.getAnnee())
        print("Kilométrage :",voiture.getKilometrage(),"km")
        
voiture = Voiture("Toyota", "Camry", 2018, 45000)
voiture.setReservoire(6)
voiture.VoitureInfo()
voiture.demarrer()
voiture.arreter()