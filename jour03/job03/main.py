class Tache:
    def __init__(self,titre,description,statut="A faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def Fini(self):
        self.statut = "Terminée"

    
class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                return
        print(f"Tâche '{titre}' non trouvée.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.Fini()
                return
        print(f"Tâche '{titre}' non trouvée.")

    def afficherListe(self):
        print(self.taches)

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list

tache1 = Tache("Réviser pour l'examen", "Relire les chapitres 1 à 5 du livre de cours")
tache2 = Tache("Préparer le rapport", "Collecter les données et rédiger le rapport de projet")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)

print("Affichage de toutes les tâches:")
liste_taches.afficherListe()

liste_taches.marquerCommeFinie("Faire le ménage")

liste_taches.supprimerTache("Appeler le service client")

print("\nAffichage après modification:")
liste_taches.afficherListe()

tache_terminee = Tache("Préparer la présentation", "Créer les diapositives pour la réunion", "Terminée")
liste_taches.ajouterTache(tache_terminee)

taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire:")
for tache in taches_a_faire:
    print(f"- {tache.titre}")