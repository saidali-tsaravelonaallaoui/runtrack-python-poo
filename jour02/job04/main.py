class Student:
    def __init__(self, nom, prenom, num_etudiant, nbre_credit = 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__nbre_credit = nbre_credit
        self.__level = self.__studentEval()
        
    # Assesseurs (getters)
    def getNom(self):
        return self.__nom
    
    def getPrenom(self):
        return self.__prenom
    
    def getNum_etudiant(self):
        return self.__num_etudiant
    
    def getNbre_credit(self):
        return self.__nbre_credit
    
    def getLevel(self):
        return self.__level
    
    # Mutateurs (setters)
    def setAdd_credits(self, new_credit):
        if new_credit > 0:
            self.__nbre_credit += new_credit
            self.__level = self.__studentEval()
            print(f"{new_credit} crédits ajoutés avec succès.")
        else:
            print("\nErreur : Le nombre de crédits à ajouter doit être supérieur à zéro.")
            
    def __studentEval(self):
        if self.__nbre_credit >= 90:
            return "Excellent"
        elif self.__nbre_credit >= 80:
            return "Très bien"
        elif self.__nbre_credit >= 70:
            return "Bien"
        elif self.__nbre_credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def etudiant(self):
        print("Nom :",etudiant.getNom())
        print("Prénom :",etudiant.getPrenom())
        print("ID :",etudiant.getNum_etudiant())
        pass
    
    def AjoutCredit(self):
        etudiant.setAdd_credits(8)
        etudiant.setAdd_credits(10)
        etudiant.setAdd_credits(12)
        
    def studentInfo(self):
        print("\nLe nombre de credits de", etudiant.getNom(), etudiant.getPrenom(),"est de", etudiant.getNbre_credit(), "points")
        print("\nNom :",etudiant.getNom())
        print("Prénom :",etudiant.getPrenom())
        print("ID :",etudiant.getNum_etudiant())
        print(f"Niveau : {self.__level}")
            
etudiant = Student("John", "Doe", 145)


etudiant.etudiant()
etudiant.AjoutCredit()
etudiant.studentInfo()
