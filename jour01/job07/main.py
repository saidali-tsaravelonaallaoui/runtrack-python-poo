class Personnage:
    def __init__(self, x, y, plateau):
        self.x = x
        self.y = y
        self.plateau = plateau

    def gauche(self):
        if self.x > 0:
            self.x -= 1
        else:
            print("Déplacement impossible vers la gauche.")

    def droite(self):
        if self.x < len(self.plateau[0]) - 1:
            self.x += 1
        else:
            print("Déplacement impossible vers la droite.")

    def haut(self):
        if self.y > 0:
            self.y -= 1
        else:
            print("Déplacement impossible vers le haut.")

    def bas(self):
        if self.y < len(self.plateau) - 1:
            self.y += 1
        else:
            print("Déplacement impossible vers le bas.")

    def position(self):
        return (self.x, self.y)

plateau = [[0] * 6 for _ in range(6)]

mon_personnage = Personnage(4, 3, plateau)

print("Position initiale:", mon_personnage.position())

mon_personnage.gauche()
print("Déplacement vers la gauche:", mon_personnage.position())

mon_personnage.haut()
print("Déplacement vers le haut:", mon_personnage.position())

mon_personnage.droite()
print("Déplacement vers la droite:", mon_personnage.position())

mon_personnage.bas()
print("Déplacement vers le bas", mon_personnage.position())

print(plateau)