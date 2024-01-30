class Ville:
    def __init__(self, nom_ville, nbre_habitant):
        self.__nom_ville = nom_ville
        self.__nbre_habitant = nbre_habitant
        
        
    def GetNomVille(self):
        return self.__nom_ville
    
    def GetNbreHabitant(self):
        return self.__nbre_habitant
    
    def ajouterPopulation(self):
        self.__nbre_habitant += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.ajouterPopulation()
    
paris = Ville("Paris", 1000000)
marseille = Ville("Marseile", 861635)

print("Population de la ville de",paris.GetNomVille(),":",paris.GetNbreHabitant(),"habitants")
print("Population de la ville de",marseille.GetNomVille(),":",marseille.GetNbreHabitant(),"habitants")

john = Personne("John", 45, paris)
Myrtille = Personne("Myrtille", 4, paris)
Chloe = Personne("Chloé", 18, marseille)

print("Mise a jour de la population de la ville de",paris.GetNomVille(), paris.GetNbreHabitant(),"habitants")
print("Mise a jour de la population de la ville de",marseille.GetNomVille(), marseille.GetNbreHabitant(),"habitants")