class Animal:
    
    def __init__(self):
        self.age = 0
        self.prenom = "Luna"
        
    def veillir(self):
        self.age = 1
    
    def nommer(self):
        print("L'animal se nommme", self.prenom)

animal = Animal()

print("L'age de l'animal", animal.age,"ans")

animal.veillir()
print("L'age de l'animal", animal.age,"ans")

animal.nommer()