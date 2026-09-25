from typing import Any


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
    choix = int(input(message))
    try:
        if not (choix <= minimum or choix >= maximum):
            return choix
        else:
            print("Merci de renseigner une valeur dans l'intervalle defini")
            return None

    except ValueError:
        print("Merci de renseigner un entier")
        return None


def creation_cercle(cercles: dict[str, dict[str, Any]]):
    nbre_cercle = input("Combien de cercles souhaitez vous creer?")
    try:
        if nbre_cercle > 0:
            if type(nbre_cercle) is not float:
                for i in range(nbre_cercle):
                    nom_cercle = input(
                        "Renseignez le nom du cercle " + str(i + 1) + " :"
                    )

                    if nom_cercle not in cercles:
                        cercles[nom_cercle] = []
                        print(
                            "Le cercle "
                            + nom_cercle
                            + " a bien été crée"
                            + "Au suivant"
                        )
                    else:
                        print("Un cercle existe deja sous ce nom")
            else:
                print("Ne renseignez pas une valeur decimale ")
        else:
            print(" Merci de renseigner un entier positif ")
    except ValueError:
        print(" Merci de renseigner un entier positif et non un caractère ")


def ajout_membre(
    cercles: dict[str, dict[str, Any]],
    minimum_membre: int | None = None,
    maximum_membre: int | None = None,
):

    nbre_membre = input("Combien de membres souhaitez-vous rajouter?")

    try:
        if nbre_membre > minimum_membre or nbre_membre < maximum_membre:
            if type(nbre_membre) is int:
                for j in range(nbre_membre):
                    cercle = input(
                        "Dans quel cercle souhaitez-vous rajouter le membre?"
                    )
                    if cercle in cercles:
                        membre = input("Nom du membre à ajouter")

                        liste_total_membres = [
                            element for liste in cercles.values() for element in liste
                        ]

                        if membre not in liste_total_membres:
                            cercles[cercle].append(membre)
                            print("Membre rajouté")
                        else:
                            print("ce membre appartient à un cercle")

                    else:
                        print("ce cercle n'existe pas ")

            else:
                print("Ne pas reseigner une valeur decimale")
        else:
            print("ERROR!Le nombre de membres doit entre 5 et 8")

    except ValueError:
        print("Merci de renseigner un entier")


def suppression_membre(cercles: dict[str, dict[str]]) -> None:
    nbre_suppression = input("Renseignez le nombre de membres à supprimer")
    try:
        if nbre_suppression > 0:
            if type(nbre_suppression) is int:
                for j in range(nbre_suppression):
                    membre = input("Renseignez le nom du membre à supprimer :")

                    liste_totale_membres = [
                        element for liste in dict.values() for element in liste
                    ]
                    if membre in liste_totale_membres:
                        for liste in cercles.values():
                            if membre in list:
                                list.remove(membre)
                                print("suppression effectuée")
                                break
                    else:
                        print("membre inexistant")

        else:
            print("Renseigner un entier positif")
    except ValueError:
        print("Ne renseigner pas une chaine de caractère")


def recherche_cercle(cercles: dict[str, dict[str, Any]]) -> None:

    cercle = input("Entrer le nom du cercle que vous chercher")
    if cercle in cercles:
        print("Ce cercle existe bien en base")
    else:
        print("Ce cercle n'existe pas")


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
            creation_cercle(cercles)

        elif choix == 2:
            ajout_membre(cercles)

        elif choix == 3:
            suppression_membre(cercles)
        elif choix == 4:
            recherche_cercle(cercles)
        elif choix == 5:
            affichage_cercle(cercles)
