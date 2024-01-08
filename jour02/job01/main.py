class Rectangle:
    
    def __init__(self,longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur 
        
    def getLongueur(self):
        return self._longueur
    
    def getLargeur(self):
        return self._largeur
    
    def setLongueur(self, new_longueur):
        self._longueur = new_longueur
    
    def setLargeur(self, new_largeur):
        self._largeur = new_largeur
        
rectangle = Rectangle(10,5)
print("Longueur initiale:",rectangle.getLongueur())
print("Largeur initiale:",rectangle.getLargeur())

rectangle.setLongueur(8)
rectangle.setLargeur(10)
print("\nLongueur modifiée:",rectangle.getLongueur())
print("Largeur modifiée:",rectangle.getLargeur())
