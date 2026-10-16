from typing import Any


MIN_MEMBRES = 3
MAX_MEMBRES = 8


def normaliser_nom(nom: str) -> str:
    """Nettoie un nom utilisateur."""
    return " ".join(nom.strip().split())


def demander_entier(
    message: str, minimum: int | None = None, maximum: int | None = None
) -> int:
    """Demande un entier et reessaie tant que la valeur est invalide."""
    while True:
        brut = input(message)
        try:
            valeur = int(brut)
        except ValueError:
            print("Erreur: merci de saisir un entier.")
            continue

        if minimum is not None and valeur < minimum:
            print(f"Erreur: la valeur doit etre >= {minimum}.")
            continue
        if maximum is not None and valeur > maximum:
            print(f"Erreur: la valeur doit etre <= {maximum}.")
            continue
        return valeur


def demander_nom(message: str) -> str:
    """Demande un nom non vide."""
    while True:
        nom = normaliser_nom(input(message))
        if not nom:
            print("Erreur: le nom ne peut pas etre vide.")
            continue
        return nom


def membre_appartient_a_un_cercle(
    cercles: dict[str, dict[str, Any]], nom_membre: str
) -> str | None:
    """Retourne le nom du cercle auquel le membre appartient, sinon None."""
    for nom_cercle, infos in cercles.items():
        if nom_membre in infos["membres"]:
            return nom_cercle
    return None


def choisir_cercle_existant(cercles: dict[str, dict[str, Any]]) -> str | None:
    """Demande un cercle existant et retourne son nom, ou None si aucun cercle."""
    if not cercles:
        print("Aucun cercle n'existe pour le moment.")
        return None

    nom = demander_nom("Nom du cercle: ")
    if nom not in cercles:
        print("Erreur: ce cercle n'existe pas.")
        return None
    return nom


def creer_cercle(cercles: dict[str, dict[str, Any]]) -> None:
    """Cree un cercle avec leader et membres initiaux."""
    nom_cercle = demander_nom("Nom du nouveau cercle: ")
    if nom_cercle in cercles:
        print("Erreur: un cercle porte deja ce nom.")
        return

    total_membres = demander_entier(
        f"Nombre total de membres ({MIN_MEMBRES}-{MAX_MEMBRES}) : ",
        MIN_MEMBRES,
        MAX_MEMBRES,
    )

    leader = demander_nom("Nom du leader: ")
    cercle_deja = membre_appartient_a_un_cercle(cercles, leader)
    if cercle_deja is not None:
        print(f"Erreur: '{leader}' est deja membre du cercle '{cercle_deja}'.")
        return

    membres: list[str] = [leader]
    deja_vus: set[str] = {leader.lower()}

    while len(membres) < total_membres:
        nom = demander_nom(f"Nom du membre {len(membres) + 1}: ")
        cle = nom.lower()
        if cle in deja_vus:
            print("Erreur: ce membre est deja dans ce cercle.")
            continue

        cercle_deja = membre_appartient_a_un_cercle(cercles, nom)
        if cercle_deja is not None:
            print(f"Erreur: '{nom}' est deja membre du cercle '{cercle_deja}'.")
            continue

        membres.append(nom)
        deja_vus.add(cle)

    # Validation explicite: le leader est bien membre du cercle.
    if leader not in membres:
        print("Erreur interne: le leader doit etre membre du cercle.")
        return

    cercles[nom_cercle] = {"leader": leader, "membres": membres}
    print(f"Cercle '{nom_cercle}' cree avec succes.")


def ajouter_membre(employe_a_ajouter, cercles: dict[str, dict[str, Any]]) -> None:
    """Ajoute un membre dans un cercle existant."""
    nom_cercle = choisir_cercle_existant(cercles)
    if nom_cercle is None:
        return

    infos = cercles[nom_cercle]
    membres: list[str] = infos["membres"]
    if len(membres) >= MAX_MEMBRES:
        print(f"Erreur: un cercle ne peut pas depasser {MAX_MEMBRES} membres.")
        return

    nom = employe_a_ajouter.nom
    # nom = demander_nom("Nom du membre a ajouter: ")

    if nom.lower() in {m.nom.lower() for m in membres}:
        print("Erreur: ce membre est deja dans ce cercle.")
        return

    cercle_deja = membre_appartient_a_un_cercle(cercles, nom)
    if cercle_deja is not None:
        print(f"Erreur: '{nom}' est deja membre du cercle '{cercle_deja}'.")
        return

    membres.append(employe_a_ajouter)
    print(f"'{nom}' a ete ajoute au cercle '{nom_cercle}'.")


def retirer_membre(employe_a_supprimer, cercles: dict[str, dict[str, Any]]) -> None:
    """Retire un membre d'un cercle existant."""
    nom_cercle = choisir_cercle_existant(cercles)
    if nom_cercle is None:
        return

    infos = cercles[nom_cercle]
    membres: list[str] = infos["membres"]
    leader: str = infos["leader"]

    if len(membres) <= MIN_MEMBRES:
        print(f"Erreur: un cercle doit garder au moins {MIN_MEMBRES} membres.")
        return

    # nom = demander_nom("Nom du membre a retirer: ")
    nom = employe_a_supprimer.nom

    if nom == leader.nom:
        print("Erreur: impossible de retirer le leader du cercle.")
        return

    index = next(
        (i for i, m in enumerate(membres) if m.nom.lower() == nom.lower()), None
    )
    if index is None:
        print("Erreur: ce membre n'existe pas dans ce cercle.")
        return

    retire = membres.pop(index)
    print(f"'{retire}' a ete retire du cercle '{nom_cercle}'.")


def rechercher_cercle(cercles: dict[str, dict[str, Any]]) -> None:
    """Recherche un cercle par nom."""
    if not cercles:
        print("Aucun cercle enregistre.")
        return

    nom = demander_nom("Nom du cercle a rechercher: ")
    if nom in cercles:
        infos = cercles[nom]
        print(
            f"Cercle trouve: {nom} | Leader: {infos['leader']} | Membres: {len(infos['membres'])}"
        )
    else:
        print("Ce cercle n'existe pas.")


def afficher_tous_les_cercles(cercles: dict[str, dict[str, Any]]) -> None:
    """Affiche tous les cercles avec leurs informations principales."""
    if not cercles:
        print("Aucun cercle enregistre.")
        return

    print("\n--- Liste des cercles ---")
    for nom_cercle, infos in cercles.items():
        membres = ", ".join(infos["membres"])
        print(f"- {nom_cercle}")
        print(f"  Leader : {infos['leader']}")
        print(f"  Membres ({len(infos['membres'])}) : {membres}")
    print("-------------------------\n")


def afficher_menu() -> None:
    print("\n===== Gestion des cercles =====")
    print("0 - Quitter")
    print("1 - Creer un cercle")
    print("2 - Ajouter un membre")
    print("3 - Retirer un membre")
    print("4 - Rechercher un cercle")
    print("5 - Afficher tous les cercles")
