class Personnage:
    def __init__(self, matrice, x, y):
        self.matrice = matrice
        self.x = x
        self.y = y
        self.matrice[x][y] = 1
    
    def gauche(self):
        if self.x > 0:
            self.matrice[self.x][self.y] = 0 
            self.x -= 1
            self.matrice[self.x][self.y] = 1
    
    def droite(self):
        if self.x < len(self.matrice) - 1:
            self.matrice[self.x][self.y] = 0
            self.x += 1
            self.matrice[self.x][self.y] = 1
    
    def haut(self):
        if self.y > 0:
            self.matrice[self.x][self.y] = 0
            self.y -= 1
            self.matrice[self.x][self.y] = 1
    
    def bas(self):
        if self.y < len(self.matrice[0]) - 1:
            self.matrice[self.x][self.y] = 0
            self.y += 1
            self.matrice[self.x][self.y] = 1
    
    def position(self):
        return (self.x, self.y)
matrice = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

mon_personnage = Personnage(matrice,2, 2)

print(matrice)
print("Position actuelle du personnage :", mon_personnage.position())