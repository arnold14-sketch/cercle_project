def creation_cercle(nbre_cercle,cercle_list):
    try:
        nbre_cercle=int(nbre_cercle)
        if nbre_cercle<=0:
            print(" La valeur doit etre positive ")
            controle=1#si la valuer n'est pas positive
        else:
            for i in range(nbre_cercle):
                while True:
                    add=input("Renseignez le nom du cercle "+str(i+1)+" :")
                    if add in cercle_list:
                        print('Un cercle porte déjà ce nom,merci de renseigner un autre nom')
                    else:
                        cercle_list.append(add)
                        cercles_dict[add]=[]
                        print('Le cercle '+add+' a bien été crée')
                        break
            controle=0#si pas d'erreur
    except ValueError:
        print(" Merci de renseigner un entier et non un caractère ") 
        controle=1   
    return cercle_list,controle

def ajout_membre(nbre_membre,cercle,cercles_dict):
    check=[]
    try:
        nbre_membre=int(nbre_membre)
    
        if nbre_membre<5 or nbre_membre>8:
            print("ERROR!Le nombre de membres doit entre 5 et 8")
            controle=1
        
        else:

            for j in range(nbre_membre):
                while True:
                    add=input("Renseignez le nom du membre "+str(j+1)+" :")
                    for cle,lst in cercles_dict.items():#creer une liste de tous les membres
                        k=0
                        for l in lst:
                            check.append(lst[k])
                            k=+1
                    #check
                    if add in check:#verifie si le membre existe dans la liste globale crée
                        print("Cette personne est déjà membre d'un cercle ")
                    else:
                        cercles_dict[cercle].append(add)#ajoute le membre dans le dict si inexistant
                        print(add+' a bien été ajouté dans la liste des membres du cercle '+cle)
                        break
            
            controle=0

    except ValueError:
        print("Merci de renseigner un entier")
        controle=1
    return cercles_dict,controle

def suppression_membre(nbre_membre:int ,cercle,cercles_dict):
    try:
        nbre_membre=int(nbre_membre)
        for j in range(nbre_membre):
            delete=input("Renseignez le nom du membre à supprimer :")
            if delete in cercles_dict[cercle]:
                cercles_dict[cercle].remove(delete)
                print(delete+' a été supprimé du cercle '+cercle)
                controle=0        
            else :
                controle=1    
                print("ce membre n'existe pas dans ce cercle")
    except ValueError:
        print("Merci de renseigner un entier")
        controle=1

    return cercles_dict,controle
def recherche_cercle(cercle,cercle_list):
    if cercle in cercle_list:
        print("Ce cercle existe bien en base")
    else:
        print("Ce cercle n'existe pas")
def affichage_cercle(cercle_list):
    #for cercle in cercle_list:
    print ('Voici la liste des cercles enregistrés: '+str(cercle_list))

    
if __name__ == "__main__":
    cercle_list=[]
    cercles_dict={}
    #Gestion du nombre de cercle
    while True:
        print('********* Bienvenue dans votre programme de gestion de cercle *******\n')
        print('Que desirez-vous faire \n')
        print('0-Quitter le programme\n')
        print('1-Creer un cercle\n')
        print('2-Ajouter un membre dans un cercle\n')
        print("3-Suprimer un membre d'un cercle\n")
        print("4-Rechercher un cercle par nom\n")
        print("5-Afficher tous les cercles\n")
        while True:#boucle sur le programme tant que l'option quitté n'est pas activé
            enter=input('Merci de renseigner votre choix: ')
            try :
                enter=int(enter)
                if enter<0 or enter>5:#verifie que le choix de l'input du menu
                    print('merci de renseigner un chiffre present dans le menu soit de 0 à 5')
            except ValueError:
                print('Merci de renseigner un entier')
            break
        if enter==0:
            print("Merci d'etre passé")
            break

        if enter==1 :

            
            while True:
                while True:#boucle si la fonction ne crée pas les cercles
                    c=input("combien de cercles souhaitez-vous crée ?")
                    cercle_list,controle_main1=creation_cercle(c,cercle_list)
                    if controle_main1==0:
                        break
                break

        if enter==2:
            if cercle_list==[]:
                print("Aucun cercle n'est crée pour le moment.Faites le d'abord")
            else:
                
                while True:#boucle tant que le nom de cercle rensigné n'est pas correcte
                    cercle=input("Dans quel cercle souhaitez-vous rajouter des membres?")
                    for valeur in cercles_dict:
                        if cercle==valeur:
                            confirmation=0
                            break
                        else:
                            confirmation=1
                    if confirmation==1:
                        print("Le cercle renseigné n'existe pas") 
                    if confirmation==0:
                        while True:#boucle tant que les membres ne sont pas crées
                            m=input("combien de membres souhaitez-vous pour le cercle "+cercle+" ?")
                            cercles_dict,controle_main2=ajout_membre(m,cercle,cercles_dict)
                            if controle_main2==0:
                                break
                        break

                            
        if enter==3:
            if cercle_list==[]:
                print("Aucun cercle n'est crée pour le moment.Faites le d'abord")
            else:
                while True:#boucle tant que le nom de cercle est inexistant
                    cercle=input("Dans quel cercle souhaitez-vous rajouter des membres?")
                    for valeur in cercles_dict:
                        if cercle==valeur:
                            confirmation=0
                            break
                        else:
                            confirmation=1
                    if confirmation==1:
                        print("Le cercle renseigné n'existe pas") 
                    if confirmation==0:
                        while True:#boucle tant que les membres ne sont pas rajoutés
                                s=input("combien de membres souhaitez-vous supprimer du cercle "+cercle+" ?")
                                cercles_dict,controle_main3=suppression_membre(s,cercle,cercles_dict)
                                if controle_main3==0:
                                    break
                        break
        if enter==4:
            """if cercle_list==[]:#pareil que if cercle_list
                print("Aucun cercle n'est crée pour le moment.Faites le d'abord")
            else:
                cercle=input("Quel cercke recherchez-vous")
                recherche_cercle(cercle,cercle_list)"""
            if not cercle_list:
                cercle=input("Quel cercke recherchez-vous")
                recherche_cercle(cercle,cercle_list)
            else :
                print("Aucun cercle n'est crée pour le moment.Faites le d'abord")



        if enter==5:
            affichage_cercle(cercle_list)
        while True: #Boucle tant que le choix n'est pas entre 0 et 1
            decision=input('Souhaitez-vous continuez? Si oui taper 0 sinon taper 1:   ')
            try:
                decision=int(decision)
                if decision>1 or decision<0:
                    print("Merci de choisir entre 0 et 1")    
            except ValueError:
                print("Merci de choisir entre 0 et 1")
            if decision==0 or decision==1:
                    break
        if decision==0:
            print('Ravie de continuer')
        else:
            print('A bientot')
            break
        
        
        