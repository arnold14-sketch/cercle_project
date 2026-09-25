from typing import Any


# creation de la classe cercle et de ses attributs
class cercle:
    # save_cercles=[]
    def __init__(self, name: str, description: str, list_membres: list):

        if name.strip() == "" and description.strip() == "" and list_membres == []:
            raise ValueError("Motif: Nom,description et liste de membre obligatoires")
        elif name.strip() == "":
            raise ValueError("Motif: Nom obligatoire")
        elif description.strip() == "":
            raise ValueError("Motif: Description obligatoire")
        elif len(list_membres) < 3 or len(list_membres) > 8:
            raise ValueError("Motif: Le cercle doit avoir entre 3 et 8 membres")

        else:
            self._name = name
            self.description = description
            self.list_membres = list_membres
            # .save_cercles.append(self)
            # cercles.save_name_circles.append(name)#save circle's name

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, new_cerle_name):
        self._name = new_cerle_name

    def c_ajout_membre(self, new_member_name):

        self.list_membres.append(new_member_name)
        print(f"{new_member_name} rajouté avec succès")

    def suppression_membre(self, member_name):
        if member_name in self.list_membres:
            self.list_membres.remove(member_name)
            print("Membre supprimé avec succès")
        else:
            raise ValueError("Motif:Motif:Ce membre n'appartient pas au cercle")


def afficher_menu() -> None:
    print("********* Bienvenue dans votre programme de gestion de cercle *******\n")
    print("Que desirez-vous faire \n")
    print("0-Quitter le programme\n")
    print("1-Creer un cercle\n")
    print("2-Ajouter un membre dans un cercle\n")
    print("3-Suprimer un membre d'un cercle\n")
    print("4-Rechercher un cercle par nom\n")
    print("5-Afficher tous les cercles\n")


def demander_entier(
    message: str, minimum: int | None = None, maximum: int | None = None
) -> int | None:
    try:
        choix = int(input(message))
        if not (choix <= minimum or choix >= maximum):
            return choix
        else:
            print("Merci de renseigner une valeur dans l'intervalle defini")
            return None
    # print ("Motif: Merci de renseigner un entier")
    # return None
    except:
        raise ValueError("Renseigner un entier")


"""    
"""


def creation_cercle(nom_cercle: str, cercles: dict[str, dict[str, Any]]) -> dict:
    list_membre = list()
    if nom_cercle not in cercles:
        description = input("Description du cercle")
        nbre_membre = demander_entier("Combien de membre à assigner?", 5, 8)
        if nbre_membre != None:
            for i in range(nbre_membre):
                add_member = input(f"Entrer le nom du membre {i + 1}")
                list_membre.append(add_member)

            try:
                new_cercle = cercle(nom_cercle, description, list_membre)
                cercles[new_cercle.name] = new_cercle
                print("Le cercle " + nom_cercle + " a bien été crée" + "Au suivant")
            except TypeError:
                raise ("Motif: Une error c'est produite lors de la creation du cercle")

        else:
            raise ValueError("Motif: Merci de renseigner un nbre de membre conforme")

    else:
        raise ValueError("Motif: Un cercle existe deja sous ce nom")


def ajout_membre(cercles: dict[str, dict[str, Any]]):

    f_nom_cercle = input("Dans quel cercle rajoutons le membre")
    if f_nom_cercle in cercles:
        if len(cercles[f_nom_cercle].list_membres) < 8:
            f_new_nom_membre = input("Quel est le nom du membre")

            for c in cercles.values():  # recherche si le membre existe dans un cercle
                for nom_membre in c.list_membres:
                    if f_new_nom_membre != nom_membre:
                        pass
                        is_exist = False

                    else:
                        is_exist = True
                        break

            # try:
            if is_exist == False:
                cercles[f_nom_cercle].c_ajout_membre(f_new_nom_membre)
                print("Membre rajouté")

            elif is_exist == True:
                raise ValueError("Ce membre appartient à un cercle")  # {est_membre_de}

            # except TypeError:
            # raise ("une erreur est survenue lors de la creation du cercle")

        else:
            raise ValueError("nombre de membres max atteint")
    else:
        print("Cercle n'existe")


def suppression_membre(cercles: dict[str, dict[str]]) -> None:

    s_membre = input("Merci de renseigner le nom")
    confirmation = False
    for c in cercles.values():
        for nom_membre in c.list_membres:
            if nom_membre == s_membre:
                try:
                    c.suppression_membre(s_membre)
                    confirmation = True
                    print("Membre supprimé")

                except TypeError:
                    raise ("une erreur est survenue lors de la suppression")
                break
        if confirmation == False:
            raise ValueError("Le membre renseigné n'existe pas")


def recherche_cercle(cercles: dict[str, dict[str, Any]]) -> None:
    cercle_recherche = input("quel est cerle? ")
    if cercle_recherche in cercles:
        print("Le cercle existe")
        # return cercle
    else:
        print("Le cercle n'existe pas")
        # return None


def affichage_cercle(cercles: dict[str, dict[str]]) -> None:

    # for cercle in cercle_list:
    print("Voici la liste des cercles enregistrés: " + cercles)


if __name__ == "__main__":
    cercles: dict[str, dict[str]] = {}

    while True:
        afficher_menu()
        choix = demander_entier("Votre choix (0-5): ", 0, 5)
        if choix == 0:
            print("Merci d'etre passé")
            break

        elif choix == 1:
            nom_cercle = input("Nom du cercle")
            creation_cercle(nom_cercle, cercles)

        elif choix == 2:
            nom_membre = input("Saisir nom du nouveau membre")
            ajout_membre(nom_membre, cercles)

        elif choix == 3:
            nom_membre = input("saisir le nom du membre")
            suppression_membre(nom_membre, cercles)
        elif choix == 4:
            cercle_recherche = input("saisir le nom du cercle:")
            recherche_cercle(cercle_recherche, cercles)
        elif choix == 5:
            affichage_cercle(cercles)
