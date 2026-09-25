from typing import Any

from src.etape3.functions_all.function import ajouter_membre,retirer_membre,afficher_tous_les_cercles,creer_cercle,cercles


class Employe_CB:

    def __init__(self,nom :str, prenom :str,date_entree :str,pratice :str ,statut):
        self._nom=nom
        self._prenom=prenom
        self._date_entree=date_entree
        self._pratice=pratice
        self._statut:Statut_interface=statut #ici je dis que le statut est de type classe statut developper .necessaire pour faire le lien vers la classe statut_interface
    
    @property
    def nom (self):
        return self._nom
    

    @property
    def statut(self):

        return self._statut
    
    @statut.setter
    def statut (self,new_statut): #new statut est de type statut donc attend une classe e
        self.new_statut=new_statut
    
    
    def get_info (self) ->str :
        
        print("\n===== Les informations individuelles de cet employé =====")
        print(f"1 - Nom : {self.nom} ")
        print(f"2 - Prenom : {self._prenom}")
        print(f"3 - Date_entree : {self._date_entree}")
        print(f"4 - Pratice : {self._pratice}")
        print(f"5 - Statut actuelle : {self._statut}")

    #def integrer_un_cercle (self) :# ordinaire qui fait la demande d'integration
        #self._statut.integrer_un_cercle() #je delegue la gestion de l'integration à la fonction
        #print ("La demande a été etudiée")

    #def sortir_cercle(self):#membre ou leader
        #self._statut.sortir_cercle(self) 

    #def designer_backup(self) -> Employe_CB: #prerogative leader

        #self._statut.designer_backup() 

    def supprimer_membre(self) -> None : #prerogative leader

        self._statut.supprimer_membre_delegation(self) 

    def ajout_membre(self) :#leader 

        self._statut.ajout_membre_delegation(self) 


class Statut_interface :
    """"
    def integrer_un_cercle (self) :# ordinaire qui fait la demande d'integration
        pass

    def sortir_cercle(self):#membre ou leader
        pass

    def designer_backup(self) -> Employe_CB: #prerogative leader

        pass
    """
    def supprimer_membre_delegation(self,employe_a_supprimer) -> None : #prerogative leader

        pass

    def ajout_membre_delegation(self,employe_a_ajouter) :#leader 

        pass

class Statut_Employe_Ordinaire (Statut_interface):
    """
    #def integrer_un_cercle (self,employe :Employe_CB) :# ordinaire qui fait la demande d'integration
        
        
        #print('***A developper A ETE ENREGISTRE****')

    
    #def sortir_cercle(self):#membre ou leader
        
        #raise ValueError("Vous n'etes pas autorisé à faire cette action ordinaire")

    #def designer_backup(self) -> Employe_CB: #prerogative leader

        #raise ValueError("Vous n'etes pas autorisé à faire cette action ordinaire")
    """
    def supprimer_membre_delegation(self,employe_a_supprimer) -> None : #prerogative leader

        raise ValueError("Vous n'etes pas autorisé à faire cette action!!")

    def ajout_membre_delegation(self,employe_a_ajouter) :#leader 

        raise ValueError("Vous n'etes pas autorisé à faire cette action !!")
    
class Statut_Employe_Membre (Statut_interface):
    """"
    def integrer_un_cercle (self) :
        
        #raise ValueError("Vous etes deja membre d'un cercle")
    
    #def sortir_cercle(self):#membre ou leader

        
        #print("la demande de sortie a été pris en compte")

    def designer_backup(self) -> Employe_CB: #prerogative leader

        raise ValueError("Vous n'etes pas autorisé à faire cette action")
    """
    def supprimer_membre_delegation(self,employe_a_supprimer) -> None : #prerogative leader

        raise ValueError("Vous n'etes pas autorisé à faire cette action")

    def ajout_membre_delegation(self,employe_a_ajouter) :#leader 

        raise ValueError("Vous n'etes pas autorisé à faire cette action")

class Statut_Employe_Leader (Statut_interface):
    """"
    def integrer_un_cercle (self) :# ordinaire qui fait la demande d'integration
        
        #raise ValueError("Operation impossible car vous etes deja leader d'un cercle")
    
    #def sortir_cercle(self):#membre ou leader
        
        
        print("la demande de sortie a été pris en compte")

    #def designer_backup(self) -> Employe_CB: #prerogative leader

        
        print("le backup est designé")
    """
    def supprimer_membre_delegation(self,employe_a_supprimer :Employe_CB) -> None : #prerogative leader

        retirer_membre(employe_a_supprimer,cercles)
        print("le membre est supprimé")

    def ajout_membre_delegation(self,employe_a_ajouter :Employe_CB) :#leader 
        
        ajouter_membre(employe_a_ajouter,cercles)
        print("le membre est ajouté")

if __name__ == "__main__" :
    n=None
    while n!='O':

        emp1=Employe_CB('ngue','arnold','1005','plateforme',Statut_Employe_Leader())
        creer_cercle(cercles)
        emp1.ajout_membre()
        afficher_tous_les_cercles(cercles)
        n=input("continuer?")
        #emp1.integrer_un_cercle()
        #emp1.ajout_membre()
        #emp1.get_info()
        """
        emp1.statut='membre'
        eta=emp1.statut
        n=emp1._nom
        print(eta)
        print(n)
        """



