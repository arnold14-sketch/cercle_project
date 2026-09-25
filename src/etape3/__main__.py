from src.etape3.save_functions import sauvegarde
from src.etape3.functions_all import function_utils, function


def main() -> None:

    while True:
        save_cercle = sauvegarde.sauvegarde_cercle()
        function.afficher_menu()
        choix = function.demander_entier("Votre choix (0-5): ", 0, 5)

        if choix == 0:
            print("Au revoir.")
            break
        if choix == 1:
            cercle = function_utils.generer_cercle()
            print("\n----Recapitulatif cercle---\n")
            function_utils.afficher_cercle_detaillés(cercle)
            save_cercle.save(cercle)

        elif choix == 2:
            function_utils.ajouter_membre(save_cercle.cercles)

        elif choix == 3:
            function_utils.retirer_membre(save_cercle.cercles)

        elif choix == 4:
            function_utils.rechercher_cercle(save_cercle.cercles)

        elif choix == 5:
            function_utils.afficher_tous_les_cercles_detaillés(save_cercle.cercles)


if __name__ == "__main__":
    main()
