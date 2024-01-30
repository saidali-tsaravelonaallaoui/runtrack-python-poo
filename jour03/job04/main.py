class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques pour le joueur {self.nom}:")
        print(f"Position: {self.position}")
        print(f"Nombre de buts marqués: {self.buts_marques}")
        print(f"Nombre de passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes reçus: {self.cartons_jaunes}")
        print(f"Cartons rouges reçus: {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques pour l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()


joueur1 = Joueur("Neymar", 10, "Attaquant")
joueur2 = Joueur("Lewandowski", 9, "Attaquant")
joueur3 = Joueur("Kante", 7, "Milieu")
joueur4 = Joueur("Ramos", 4, "Défenseur")

equipe1 = Equipe("Paris Saint-Germain")
equipe2 = Equipe("Bayern Munich")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)

print("Statistiques des joueurs avant le match:")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()
joueur4.recevoirUnCartonRouge()

print("\nStatistiques des joueurs après le match:")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()