class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return self.nom + self.prenom
    
personne1 = Personne("Mohamed", " Ali")
personne2 = Personne("Allaoui", " Said")
print("Je suis", personne1.SePresenter())
print("Je suis", personne2.SePresenter())