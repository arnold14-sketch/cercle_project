from typing import Any
def main() -> None:

    cercles: dict[str, dict[str,Any]] = {}

    while True:
        afficher_menu()
        choix = demander_entier("Votre choix (0-5): ", 0, 5)

        if choix == 0:
            print("Au revoir.")
            break
        if choix == 1:
            creer_cercle(cercles)
        elif choix == 2:
            ajouter_membre(cercles)
        elif choix == 3:
            retirer_membre(cercles)
        elif choix == 4:
            rechercher_cercle(cercles)
        elif choix == 5:
            afficher_tous_les_cercles(cercles)

def demander_entier(message: str, minimum: int | None = None, maximum: int | None = None) -> int:
    ...#signifie ne fait rien (il va falloir faire du dev) contrairement à pass qui signifie 