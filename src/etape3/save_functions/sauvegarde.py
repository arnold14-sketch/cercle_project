from src.etape3.cercle import creation_cercle
from abc import abstractmethod, ABC
from src.etape3.employe import creation_membre


class sauvegarde(ABC):
    @abstractmethod
    def save(objet, liste_objet: list):
        pass

    @abstractmethod
    def afficher_liste_a_jour():
        pass


class sauvegarde_cercle(sauvegarde):
    cercles: creation_cercle.cercle = []

    def __init__(self):
        self._liste_cercles = sauvegarde_cercle.cercles

    def save(self, c: creation_cercle.cercle):
        if not self.check_cercle_existe(c):
            self._liste_cercles.append(c)
            print("Sauvegarde du cercle effectuée")

        else:
            print("Doublon : Sauvegarde impossible car un cercle existe sous ce nom")

    def check_cercle_existe(self, c: creation_cercle.cercle):

        for element in self._liste_cercles:
            if element == c:
                print("CE CERCLE EXISTE DEJA")
                return True

        return False

    def afficher_liste_a_jour(self):

        for value in self._liste_cercles:
            print(f"{value}")


class sauvegarde_membre(sauvegarde):
    membres: creation_membre.membre = []

    def __init__(self, liste_membres: list):
        self._liste_membres = liste_membres

    def save(self, m: creation_membre.membre):

        self._liste_membres.append(m)
        print("Sauvegarde du membre effectuée")

    def afficher_liste_a_jour(self) -> None:

        for value in self._liste_membres:
            print(f"{value}")
