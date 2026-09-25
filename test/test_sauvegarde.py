from src.etape3.cercle import creation_cercle
from src.etape3.employe import creation_membre
from src.etape3.save_functions import sauvegarde
import pytest

#creation de mes jeux de données test
@pytest.fixture
def jeu_de_donnees_membre ():

    m1=creation_membre.membre()
    m2=creation_membre.membre()
    m3=creation_membre.membre()
   
    return m1,m2,m3

@pytest.fixture
def jeu_de_donnees_cercle ():

    c1=creation_cercle.cercle()
    c2=creation_cercle.cercle()
    c3=creation_cercle.cercle()
   
    return c1,c2,c3


@pytest.fixture
def jeu_de_donnees_sauvegarde (jeu_de_donnees_cercle,jeu_de_donnees_membre):
    m1,m2,m3=jeu_de_donnees_membre
    c1,c2,c3=jeu_de_donnees_cercle
    sc=sauvegarde.sauvegarde_cercle([c1,c2,c3])
    sm=sauvegarde.sauvegarde_membre([m1,m2,m3])
   
    return sc,sm



def test_initialisation_sauvegarde (jeu_de_donnees_cercle,jeu_de_donnees_membre,jeu_de_donnees_sauvegarde):
    m1,m2,m3=jeu_de_donnees_membre
    c1,c2,c3=jeu_de_donnees_cercle
    sc,sm =jeu_de_donnees_sauvegarde

    assert sc._liste_cercles==[c1,c2,c3] and sm._liste_membres==[m1,m2,m3]

def test_save_membre(jeu_de_donnees_sauvegarde):
    sc,sm =jeu_de_donnees_sauvegarde
    m4=creation_membre.membre()
    sm.save(m4)
    assert m4 in sm._liste_membres

def test_save_cercle(jeu_de_donnees_sauvegarde):
    sc,sm =jeu_de_donnees_sauvegarde
    c4=creation_cercle.cercle()
    sc.save(c4)
    assert c4 in sc._liste_cercles










