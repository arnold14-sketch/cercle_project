from src.etape3.cercle import creation_cercle
from src.etape3.employe import creation_membre
import pytest

#creation de mes jeux de données test
"TEST DE LA CLASSE CERCLE"
@pytest.fixture
def jeu_de_donnees_cercle ():

    c1=creation_cercle.cercle()
    b=creation_cercle.builder_creation_cercle()
   
    return  c1,b

@pytest.fixture
def jeu_de_donnees_membre ():

    membre=creation_membre.membre()  
    leader=creation_membre.membre() 
    return membre,leader

def test_initialisation_cercle (jeu_de_donnees_cercle):
    c1,b =jeu_de_donnees_cercle
    assert c1.nom is None and c1.leader is None and c1.Liste_des_membres==[]

def test_set_nom_cercle(jeu_de_donnees_cercle):
    c1,b =jeu_de_donnees_cercle
    c1.nom="cercle_1"
    assert c1.nom=="cercle_1"

def test_set_leader(jeu_de_donnees_cercle):
    c1,b =jeu_de_donnees_cercle
    c1.leader=creation_membre.membre()

    assert isinstance(c1.leader,creation_membre.membre) is True

def test_set_liste_des_membres (jeu_de_donnees_cercle):
    c1,b =jeu_de_donnees_cercle
    m1=creation_membre.membre()
    m2=creation_membre.membre()
    c1.Liste_des_membres=[m1,m2]
    assert len(c1.Liste_des_membres)==2

def test_ajout_membre_cercle (jeu_de_donnees_cercle,jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_cercle
    m=jeu_de_donnees_membre
    c1.ajouter_membre(m)
    assert m in c1.Liste_des_membres

"TEST DE LA CLASSE BUILDER_CERCLE"

def test_initialisation_builder_cercle(jeu_de_donnees_cercle):
    c1,b =jeu_de_donnees_cercle
    assert isinstance(b._cercle,creation_cercle.cercle) is True

def test_builder_creation_nom(jeu_de_donnees_cercle,jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_cercle
    b.creation_nom("new_cercle")
    assert b._cercle.nom=="new_cercle"

def test_builder_creation_leader(jeu_de_donnees_cercle,jeu_de_donnees_membre):
    c1,b =jeu_de_donnees_cercle
    membre,leader=jeu_de_donnees_membre
    b.creation_leader(leader)
    b._cercle.leader==leader
    #assert isinstance(b._cercle.leader,creation_membre.membre)












