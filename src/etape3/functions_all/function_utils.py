from cercle import creation_cercle

from src.etape3.employe import creation_membre
from src.etape3.functions_all import function


def generer_membre_ordinaire() -> creation_membre.membre:

    builder_creation_membre = creation_membre.builder_creation_membre_ordinaire()
    director = creation_membre.director_creation_membre()
    director.builder = builder_creation_membre
    director.construction_membre_leader()

    membre_ordinaire_generer = builder_creation_membre.show_membre()

    return membre_ordinaire_generer


def generer_leader_cercle() -> creation_membre.membre:

    builder_creation_leader = creation_membre.builder_creation_membre_leader()
    director = creation_membre.director_creation_membre()
    director.builder = builder_creation_leader
    director.construction_membre_leader()
    leader_generer = builder_creation_leader.show_membre()

    return leader_generer


def generer_cercle() -> creation_cercle.cercle:

    builder_creation_cercle = creation_cercle.builder_creation_cercle()
    director = creation_cercle.director_cercle()
    director.builder = builder_creation_cercle
    director.creation_cercle()
    cercle_generer = builder_creation_cercle.show_cercle()

    return cercle_generer


def afficher_cercle_detaillés(cercle: creation_cercle.cercle) -> None:

    print("\n--- Details du cercle ---\n")
    for key, value in cercle._cercle_informations.items():
        if isinstance(value, list):
            print(f"{key} : \n")
            i = 1
            for element in value:
                # if isinstance(element ,creation_membre.membre)

                print(f"\t {i}-{element}")
                i += 1
        else:
            print(f"{key} : {value} \n")


def afficher_tous_les_cercles_detaillés(cercles: list[creation_cercle.cercle]) -> None:

    print("\n--- AFFICHAGE DES CERCLES  ---\n-")
    i = 1
    for cercle in cercles:
        print(f"\n---- CERCLE {i} ------ \n")
        afficher_cercle_detaillés(cercle)
        i += i


def afficher_nom_tous_les_cercles(cercles: list[creation_cercle.cercle]):

    i = 1
    for cercle in cercles:
        print(f"\t{i}-{cercle._cercle_informations['nom_cercle']}\n")
        i += 1


def ajouter_membre(cercles: list[creation_cercle.cercle]):

    if not len(cercles) < 1:
        print("\n--- LISTE DES CERCLES---\n-")
        afficher_nom_tous_les_cercles(cercles)
        valeur = function.demander_entier(
            "Entrer le numero du cercle correspondant : ", 1, len(cercles)
        )
        membre_ordinaire = generer_membre_ordinaire()
        cercle = cercles[valeur - 1]
        cercle.ajouter_membre(membre_ordinaire)

    else:
        print("AUCUN CERCLE EXISTANT -MERCI DE CREER UN CERCLE")


def retirer_membre(cercles: list[creation_cercle.cercle]):

    if not len(cercles) < 1:
        print("\n--- LISTE DES CERCLES---\n-")
        afficher_nom_tous_les_cercles(cercles)
        valeur = function.demander_entier(
            "Entrer le numero du cercle correspondant : ", 1, len(cercles)
        )
        cercle = cercles[valeur - 1]
        liste_membres = cercle._cercle_informations["Liste_des_membres"]
        i = 1
        print("----LISTE DES MEMBRES DE CE CERCLE---")
        for element in liste_membres:
            print(f"{i}-{element}\n")
            i += 1

        if not len(liste_membres) < 4:
            valeur2 = function.demander_entier(
                "Entrer le numero du membre correspondant : ", 1, len(liste_membres)
            )
            cercle._cercle_informations["Liste_des_membres"].pop(valeur2)
            print("Retrait du membre achevé")

        else:
            print("SUPPRESSION IMPOSSIBLE : Un cercle doit avoir minimum 3 membres")
    else:
        print("AUCUN CERCLE EXISTANT -MERCI DE CREER UN CERCLE")


def rechercher_cercle(cercles: list[creation_cercle.cercle]):

    if not len(cercles) < 1:
        nom_cercle = function.demander_nom("Quel est le nom du cercle : ")
        nom_cercle = function.normaliser_nom(nom_cercle)

        index = 0
        for cercle in cercles:
            if cercle._cercle_informations["nom_cercle"] == nom_cercle:
                afficher_cercle_detaillés(cercles[index])
                return
            index += index
        print("Ce cercle n'existe pas")

    else:
        print("AUCUN CERCLE EXISTANT")


def cercle_existe(cercles: list[creation_cercle.cercle], nom_cercle: str) -> bool:
    """Retourne si oui ou non le cercle existe déjà"""
    for element in cercles:
        if element._cercle_informations["nom_cercle"] == nom_cercle:
            return True
    return False
