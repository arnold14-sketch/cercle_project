from typing import Any
import pytest
from src.etape3.functions_all.function import ajouter_membre,retirer_membre,afficher_tous_les_cercles,creer_cercle
from src.etape3.employe import Employe_CB
from src.etape3.functions_all import function as f


cercles = { 'cercle_1' : {'leader':'Arnold','Membres':['m_c_11','m_c_12','m_c_13']},
            'cercle_2' : {'leader':'Clement','Membres':['m_c_21','m_c_22','m_c_23']}
        }

@pytest.fixture
def employes ():
    employe_1=Employe_CB('Antoine','La fontaine','10/05/2026','Platform engineering','employe')
    employe_2=Employe_CB('Arnold','Jacques','09/05/2026','Platform engineering','employe')
    employe_3=Employe_CB('Tony','La Montagne','11/05/2026','Platform engineering','employe')
    return  employe_1,employe_2,employe_3

#creation de mes jeux de données test
def test_creation_cercle(monkeypatch: pytest.MonkeyPatch,cercles:dict[str, dict[str,Any]],employe_1,employe_2,employe_3):

    def fake_demander_entier (message : str,minimum : int | None=None,maximum : int | None=None):
        return 3

    def fake_demander_nom (message :str):
        return 'nouveau_leader'

    def fake_membre_appartient_a_un_cercle(cercles ,leader):
        return None 
    

    monkeypatch.setattr(f,"demander_entier",fake_demander_entier)
    monkeypatch.setattr(f,"demander_nom",fake_demander_nom)
    simulated_inputs = iter([employe_1,employe_2,employe_3])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_inputs))
    
    with pytest.raises(ValueError,match="Motif: Un cercle existe deja sous ce nom"):
        creation_cercle("cercle_2",cercles)

#creation de mes jeux de données test


@pytest.fixture
def cercle_3 ():
    return lambda name,description,membres : cercle(name,description,membres)




                            ####DEBUT DES TESTS ###



#ajout d'un membre dans la liste de membres
def test_cercle_ajout_membre(employe_a_ajouter,cercle_1: cercle):
    
    assert 'd' in cercle_1.list_membres



#suppression d'un membre dans la liste de membres
def test_cercle_suppression_membre(cercle_1: cercle):
    cercle_1.suppression_membre('a')
    assert 'a' not in cercle_1.list_membres

#suppression d'un membre dans la liste de membres(rejet car n'appartient pas au cercle)
def test_cercle_suppression_membre_error(cercle_1: cercle):
    with pytest.raises(ValueError,match="Motif:Motif:Ce membre n'appartient pas au cercle"):
        cercle_1.suppression_membre('e')
