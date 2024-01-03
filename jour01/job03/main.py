class Operation:
    
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition (self):
        return self.nombre1 + self.nombre2
        
operation = Operation(12,3)
print("Le nombre1 est", operation.nombre1)
print("Le nombre2 est", operation.nombre2)
print("l'addition de nombre1 et nombre2 est", operation.addition())