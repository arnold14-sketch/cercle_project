from employe import creation_membre
from abc import abstractmethod,ABC
from typing import Any

class sauvegarde_membre(ABC) :

    @abstractmethod
    def save (membre: creation_membre.membre,liste_membres:list):
        pass

    @abstractmethod
    def liste_a_jour ():
        pass


class sauvegarde_membre_liste (sauvegarde_membre):

    def __init__(self,liste_membres:list):
        self._liste_membres=liste_membres

    def save (self,membre: creation_membre.membre,liste_membres:list):

        self._liste_membres.append(membre)

    def liste_a_jour(self):

        liste_membres=self._liste_membres

        return liste_membres






        




