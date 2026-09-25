from src.etape3.functions_all import function, function_utils
from src.etape3.employe.creation_membre import membre


class cercle:
    def __init__(self):

        self._cercle_informations = {
            "nom_cercle": None,
            "Leader": None,
            "Liste_des_membres": [],
        }

    def __eq__(self, other):
        if isinstance(other, cercle):
            return (
                self._cercle_informations["nom_cercle"]
                == other._cercle_informations["nom_cercle"]
            )

        return False

    @property
    def nom(self) -> str:
        return self._cercle_informations["nom_cercle"]

    @nom.setter
    def nom(self, new_name: str):
        self._cercle_informations["nom_cercle"] = new_name

    @property
    def leader(self) -> membre:
        return self._cercle_informations["Leader"]

    @leader.setter
    def leader(self, new_leader: membre):
        self._cercle_informations["Leader"] = new_leader

    @property
    def Liste_des_membres(self) -> list:
        return self._cercle_informations["Liste_des_membres"]

    def ajouter_membre(self, new_membre: membre):

        self._cercle_informations["Liste_des_membres"].append(new_membre)

    def retirer_membre(self, membre_a_supprimer: membre):

        self._cercle_informations["Liste_des_membres"].remove(membre_a_supprimer)


class builder_creation_cercle:
    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._cercle = cercle()

    def creation_nom(self, nom_cercle: str):

        self._cercle.nom = nom_cercle

    def creation_leader(self, new_leader: membre):

        self._cercle.leader = new_leader
        self._cercle.ajouter_membre(new_leader)

    def creation_membre(self, new_membre: membre):

        self._cercle.ajouter_membre(new_membre)

    def show_cercle(self) -> cercle:

        cercle_creer = self._cercle

        return cercle_creer


class director_cercle:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, new_builder: builder_creation_cercle):
        self._builder = new_builder

    def creation_cercle(self):
        MIN_MEMBRES = 3
        MAX_MEMBRES = 8
        i = 1
        nom_cercle = function.normaliser_nom(
            function.demander_nom("Quel est le nom du cercle :  ")
        )
        # if function_utils.cercle_existe()
        self._builder.creation_nom(nom_cercle)
        new_leader = function_utils.generer_leader_cercle()
        self._builder.creation_leader(new_leader)
        total_membres = function.demander_entier(
            f"Nombre total de membres ({MIN_MEMBRES}-{MAX_MEMBRES}) : ",
            MIN_MEMBRES,
            MAX_MEMBRES,
        )
        while i < total_membres:
            new_membre = function_utils.generer_membre_ordinaire()
            self._builder.creation_membre(new_membre)
            i += 1
