class Commande:
    def __init__(self, num_commande, list_commande, statut_commande):
        self.__num_commande = num_commande
        self.__list_commande = list_commande
        self.__statut_commande = statut_commande
        
        
    # Assesseurs (getters)

    def getNumCommande(self):
        return self.__num_commande
    
    def getListCommande(self):
        return self.__list_commande
    
    def getStatutCommande(self):
        return self.__statut_commande
    
    # Mutateurs (setters)
    
    def setNumCommande(self, new_num_commande):
        self.__num_commande = new_num_commande
    
    def setListCommande(self, new_list_commande):
        self.__list_commande = new_list_commande
        
    def setStatutCommande(self, new_statut_commande):
        self.__statut_commande = new_statut_commande
        
    