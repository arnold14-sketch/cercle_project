from abc import ABC, abstractmethod
from src.etape3.functions_all import function



class membre:
    def __init__(self):
        self._membre_informations = {
            "Nom": None,
            "Prenom": None,
            "Role": None,
            "Statut": None,
        }

    def __eq__(self, other):
        return self._membre_informations == other._membre_informations

    def __str__(self):

        return f"Nom:{self._membre_informations['Nom']} , Prenom:{self._membre_informations['Prenom']} , Statut:{self._membre_informations['Statut']} "

    def assigner_identite_membre(self, nom: str, prenom: str) -> None:

        self._membre_informations["Nom"] = nom
        self._membre_informations["Prenom"] = prenom

    def assigner_role_membre(self, role: str) -> None:

        self._membre_informations["Role"] = role

    def assigner_statut_membre(self, statut: str) -> None:

        self._membre_informations["Statut"] = statut

    def afficher_informations_membre(self) -> None:

        for key, value in self._membre_informations:
            print(f"{key} : {value}")


"""
    @property
    def nom (self):
        return self._membre_informations["Nom"]

    @nom.setter
    def nom(self,new_name):
        self._membre_informations["Nom"]=new_name

    @property
    def prenom (self):
        return self._membre_informations["Prenom"]
    
    @prenom.setter
    def prenom(self,new_prenom):
        self._membre_informations["Prenom"]=new_prenom

    @property
    def role (self):
        return self._membre_informations["Role"]
    
    @role.setter
    def role(self,new_role):
        self._membre_informations["Role"]=new_role

    @property
    def statut (self):
        return self._membre_informations["Statut"]
    
    @statut.setter
    def statut(self,new_statut):
        self._membre_informations["Statut"]=new_statut

"""


class builder_creation_membre(ABC):
    @abstractmethod
    def creation_identite(self):
        pass

    @abstractmethod
    def creation_role_membre(self):
        pass

    @abstractmethod
    def creation_statut_membre(self):
        pass

    @abstractmethod
    def show_membre():
        pass


class builder_creation_membre_ordinaire(builder_creation_membre):
    def __init__(self):  # permet de reset une variable
        self.reset()

    def reset(self):  # instancier un membre

        self._membre_ordinaire = membre()

    def creation_identite(self) -> None:

        nom_membre = function.normaliser_nom(
            function.demander_nom("Quel est le nom du membre : ")
        )
        prenom_membre = function.demander_nom("Quel est le prenom du membre : ")
        self._membre_ordinaire.assigner_identite_membre(nom_membre, prenom_membre)

    def creation_role_membre(self) -> None:

        role = "Ordinaire"
        self._membre_ordinaire.assigner_role_membre(role)

    def creation_statut_membre(self) -> None:

        statut = "Actif"
        self._membre_ordinaire.assigner_statut_membre(statut)

    def show_membre(self) -> membre:

        membre_ordinaire = self._membre_ordinaire

        return membre_ordinaire


class builder_creation_membre_leader(builder_creation_membre):
    def __init__(self):  # permet de reset une variable
        self.reset()

    def reset(self):  # instancier un membre

        self._membre_leader = membre()

    def creation_identite(self) -> None:

        nom = function.normaliser_nom(
            function.demander_nom("Quel est le nom du leader : ")
        )
        nom = function.normaliser_nom(nom)
        prenom = function.demander_nom("Quel est le prenom du leader : ")
        prenom = function.normaliser_nom(prenom)

        self._membre_leader.assigner_identite_membre(nom, prenom)

    def creation_role_membre(self) -> None:

        role = "Leader"
        self._membre_leader.assigner_role_membre(role)

    def creation_statut_membre(self) -> None:

        statut = "Actif"
        self._membre_leader.assigner_statut_membre(statut)

    def show_membre(self) -> membre:

        membre_leader = self._membre_leader

        return membre_leader


class director_creation_membre:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, new_builder: builder_creation_membre):

        self._builder = new_builder

    def construction_membre_ordinaire(self):

        self._builder.creation_identite()
        self._builder.creation_role_membre()
        self._builder.creation_statut_membre()

    def construction_membre_leader(self):
        self._builder.creation_identite()
        self._builder.creation_role_membre()
        self._builder.creation_statut_membre()
