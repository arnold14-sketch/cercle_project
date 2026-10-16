from functions import adaptators
from persistance import sauvegarde
from functions import utils


def main() -> None:

    while True:
        save_cercle = sauvegarde.sauvegarde_cercle()
        utils.afficher_menu()
        choix = utils.demander_entier("Votre choix (0-5): ", 0, 5)

        if choix == 0:
            print("Au revoir.")
            break
        if choix == 1:
            cercle = adaptators.generer_cercle()
            print("\n----Recapitulatif cercle---\n")
            adaptators.afficher_cercle_detaillés(cercle)
            save_cercle.save(cercle)

        elif choix == 2:
            adaptators.ajouter_membre(save_cercle.cercles)

        elif choix == 3:
            adaptators.retirer_membre(save_cercle.cercles)

        elif choix == 4:
            adaptators.rechercher_cercle(save_cercle.cercles)

        elif choix == 5:
            adaptators.afficher_tous_les_cercles_detaillés(save_cercle.cercles)


if __name__ == "__main__":
    main()
