from src.etape3.cercle import creation_cercle
from src.etape3.employe import creation_membre
import pytest

#creation de mes jeux de données test
"TEST DE LA CLASSE CERCLE"
@pytest.fixture
def jeu_de_donnees_membre ():

    m1=creation_membre.membre()
    b=creation_membre.builder_creation_membre()
    bo=creation_membre.builder_creation_membre_ordinaire()
    bl=creation_membre.builder_creation_membre_leader()
   
    return  m1,b,bo,bl
"""
@pytest.fixture
def jeu_de_donnees_membre ():

    membre=creation_membre.membre()  
    leader=creation_membre.membre() 
    return membre,leader
"""

def test_initialisation_membre (jeu_de_donnees_membre):
    m1,b,bo,bl=jeu_de_donnees_membre
    assert m1._membre_informations=={}

"""
def afficher_informations_membre(jeu_de_donnees_membre):
    m1,b,bo,bl=jeu_de_donnees_membre
    m1.nom,m1.prenom,m1.role,m1.statut="nom_membre","prenom_membre","Ordinaire","Actif"
    assert m1.nom=="cercle_1"
"""
def test_set_leader(jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_membre
    c1.leader=creation_membre.membre()

    assert isinstance(c1.leader,creation_membre.membre) is True

def test_set_liste_des_membres (jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_membre
    m1=creation_membre.membre()
    m2=creation_membre.membre()
    c1.Liste_des_membres=[m1,m2]
    assert len(c1.Liste_des_membres)==2

def test_ajout_membre_cercle (jeu_de_donnees_membre,jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_membre
    m=jeu_de_donnees_membre
    c1.ajouter_membre(m)
    assert m in c1.Liste_des_membres

"TEST DE LA CLASSE BUILDER_CERCLE"

def test_initialisation_builder_cercle(jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_membre
    assert isinstance(b._cercle,creation_cercle.cercle) is True

def test_builder_creation_nom(jeu_de_donnees_membre,jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_membre
    b.creation_nom("new_cercle")
    assert b._cercle.nom=="new_cercle"

def test_builder_creation_leader(jeu_de_donnees_membre,jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_membre
    membre,leader=jeu_de_donnees_membre
    b.creation_leader(leader)
    b._cercle.leader==leader
    #assert isinstance(b._cercle.leader,creation_membre.membre)












