import random

class Personnage:
    # Constructeur
    def __init__(self, nom, vie=100):
        self.__nom = nom
        self.__vie = vie

    # Nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    # Vie
    def get_vie(self):
        return self.__vie

    def set_vie(self, vie):
        self.__vie = max(vie, 0)

    # Autres méthodes
    def attaquer(self, pv_personnage):
        affiche_degats = random.randint(1, 10)  
        pv_personnage.set_vie(pv_personnage.get_vie() - affiche_degats)
        return affiche_degats
    
class Jeu:
    # Constructeur
    def __init__(self):
        self.niveau = 1

    # Niveau
    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulte (1, 2, 3): "))
        while self.niveau < 1 or self.niveau > 3:
            print("Niveau incorrect.")
            self.niveau = int(input("Choisissez le niveau de difficulte (1, 2, 3): "))
        if self.niveau == 1:
            goku = Personnage("Goku", 200)
            beerus = Personnage("Beerus", 100)
            print("Niveau facile.")
        elif self.niveau == 2:
            goku = Personnage("Goku", 200)
            beerus = Personnage("Beerus", 200)
            print("Niveau moyen.")
        elif self.niveau == 3:
            goku = Personnage("Goku", 200)
            beerus = Personnage("Beerus", 250)
            print("Niveau difficile.")
        return goku, beerus

    # Lancer jeu
    def lancerJeu(self):
        goku, beerus = self.choisirNiveau()
        print(f"Vous affrontez Beerus au niveau {self.niveau}.\nLa vie de {goku.get_nom()} est a {goku.get_vie()} pv \nLa vie de {beerus.get_nom()} est a {beerus.get_vie()} pv\n")

        while goku.get_vie() > 0 and beerus.get_vie() > 0:
            degats_goku = goku.attaquer(beerus)
            if beerus.get_vie() <= 0:
                print(f"{beerus.get_nom()} a ete vaincu ! Vous avez gagne.")
                break

            degats_beerus = beerus.attaquer(goku)
            if goku.get_vie() <= 0:
                print(f"{goku.get_nom()} a ete vaincu ! Vous avez perdu.")
                break

            print(f"L'attaque de beerus a fait {degats_beerus} pv de degats a Goku: la vie de {goku.get_nom()} est a {goku.get_vie()} pv \n\nL'attaque de Goku a fait {degats_goku} pv de degats a Beerus: la vie de {beerus.get_nom()} est a {beerus.get_vie()} pv\n")


jeu = Jeu()
jeu.lancerJeu()