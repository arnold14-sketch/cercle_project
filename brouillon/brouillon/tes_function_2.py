from etape3.cercle import creation_cercle
from abc import abstractmethod,ABC
from typing import Any
from etape3.employe import creation_membre


#creation de mes jeux de données test
@pytest.fixture# create a ressource that will be used in each test function
def cercle_1():
    cercle_1=cercle("cercle_1","Discuss about AI topics",['a','b','c'])#the ressource's name and function's name should be the same
    return cercle_1

@pytest.fixture
def cercle_2():
    cercle_2=cercle("cercle_2","Discuss about cloud topics",['a','b','c'])#the ressource's name and function's name should be the same
    return cercle_2

@pytest.fixture
def cercle_3 ():
    return lambda name,description,membres : cercle(name,description,membres)


@pytest.fixture
def cercles():
    c2=cercle("cercle_2","Discuss about AI topics",['a','b','c'])
    c3=cercle("cercle_3","Discuss about AI topics",['ta','ti','te'])
    c4=cercle("cercle_4","Discuss about AI topics",['to','tu','tw','ts','tx','tv','tb','tn'])
    cercles={'cercle_2':c2,
             'cercle_3':c3,
             'cercle_4':c3
             }
    return cercles



                            ####DEBUT DES TESTS ###

def test_cercle_creation(cercle_1: cercle):
    assert cercle_1.name =="cercle_1" and cercle_1.description != "" and len(cercle_1.list_membres)>=3 and len(cercle_1.list_membres)<=8



def test_cercle_peu_members(cercle_3):
    with pytest.raises(ValueError,match="Motif: Le cercle doit avoir entre 3 et 8 membre"):
        cercle_3 ("cercle_3 ", "Discuss",['a','b'])

def test_cercle_trop_members(cercle_3):
    with pytest.raises(ValueError,match="Motif: Le cercle doit avoir entre 3 et 8 membre"):
        cercle_3 ("cercle_3 ", "Discuss",['a','b','e','f','g','h','i','j','k'])

def test_cercle_controle_absence_name(cercle_3):
    with pytest.raises(ValueError,match="Nom obligatoire"):
        cercle_3 (" ", "Discuss",['a','b','c'])


def test_cercle_controle_absence_description(cercle_3):
    with pytest.raises(ValueError,match="Description obligatoire"):
        cercle_3("cercle_4"," ",['a','b','c'])


def test_cercle_controle_pas_inputs(cercle_3):
    with pytest.raises(ValueError,match="Motif: Nom,description et liste de membre obligatoires"):
        cercle_3(" "," ",[])

#ajout d'un membre dans la liste de membres
def test_cercle_ajout_membre(cercle_1: cercle):
    cercle_1.c_ajout_membre('d')
    assert 'd' in cercle_1.list_membres



#suppression d'un membre dans la liste de membres
def test_cercle_suppression_membre(cercle_1: cercle):
    cercle_1.suppression_membre('a')
    assert 'a' not in cercle_1.list_membres

#suppression d'un membre dans la liste de membres(rejet car n'appartient pas au cercle)
def test_cercle_suppression_membre_error(cercle_1: cercle):
    with pytest.raises(ValueError,match="Motif:Motif:Ce membre n'appartient pas au cercle"):
        cercle_1.suppression_membre('e')




def test_f_creation_cercle_OK(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):

    def fake_demander_entier (message : str,minimum : int | None=None,maximum : int | None=None):
        return 3
    
    monkeypatch.setattr(etape,"demander_entier",fake_demander_entier )
    simulated_inputs = iter(["description", "membre1","membre2","membre3"])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_inputs))
    creation_cercle("new_one",cercles)
    assert "new_one" in cercles and cercles["new_one"].description=="description" and cercles["new_one"].list_membres==["membre1","membre2","membre3"]
    

def test_f_creation_cercle_wrong_nbre_membre_KO(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):

    def fake_demander_entier (message : str,minimum : int | None=None,maximum : int | None=None):
        return None
    
    monkeypatch.setattr(etape,"demander_entier",fake_demander_entier )
    simulated_inputs = iter(["description", "membre1","membre2","membre3"])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_inputs))
    with pytest.raises(ValueError,match="Motif: Merci de renseigner un nbre de membre conforme"):
        creation_cercle("new_one",cercles)
    
     
def test_f_creation_cercle_existing_name_KO(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):

    def fake_demander_entier (message : str,minimum : int | None=None,maximum : int | None=None):
        return 3
    
    monkeypatch.setattr(etape,"demander_entier",fake_demander_entier )
    simulated_inputs = iter(["description", "membre1","membre2","membre3"])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_inputs))
    with pytest.raises(ValueError,match="Motif: Un cercle existe deja sous ce nom"):
        creation_cercle("cercle_2",cercles)




simulated_inputs_1=iter(["description", "membre1","membre2", "membre3","membre4", "membre5","membre6", "membre7","membre8", "membre9","membre10"])
simulated_inputs_2= iter(["description", "membre1","membre2"])
@pytest.mark.parametrize("test_input,expected",
                          [(simulated_inputs_1,ValueError ), 
                           (simulated_inputs_2, ValueError)])

def test_f_creation_cercle_nbre_membres_KO(test_input: Iterator[str],expected: type[ValueError],monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):

    def fake_demander_entier (message : str,minimum : int | None=None,maximum : int | None=None):
        return 2
    
    monkeypatch.setattr(etape,"demander_entier",fake_demander_entier )
    #simulated_inputs = iter(["description", "membre1","membre2"])
    monkeypatch.setattr("builtins.input", lambda _: next(test_input))
    with pytest.raises(ValueError,match="Motif: Le cercle doit avoir entre 3 et 8 membres"):
        creation_cercle("new_one",cercles)



#ajout membre reussi
def test_function_ajout_membre_OK(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):
    simulated_inputs_3=iter(["cercle_3","nouveau"])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_inputs_3))
    ajout_membre(cercles)
    assert "nouveau" in cercles["cercle_3"].list_membres


#ajout membre existant dans le cercle
def test_function_ajout_membre_existant_cercle_ko(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):
    simulated_inputs_4= iter(["cercle_3", "ta"])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_inputs_4))
    with pytest.raises(ValueError,match="Ce membre appartient à un cerlce"):
        ajout_membre(cercles)

#ajout membre existant dans un autre cercle
def test_function_ajout_membre_existant_autre_cercle_ko(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):
    simulated_inputs_4= iter(["cercle_3", "ta"])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_inputs_4))
    with pytest.raises(ValueError,match="Ce membre appartient à un cercle"):
        ajout_membre(cercles)



#supprimer un membre dans une liste
def test_function_suppression_membre_existant(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):
    
    monkeypatch.setattr("builtins.input",lambda _: "ta")
    suppression_membre(cercles)
    "ta" not in cercles["cercle_3"].list_membres

#suppression d'un membre qui n'existe pas 
def test_function_suppression_membre_existant(monkeypatch: pytest.MonkeyPatch,cercles: dict[str, cercle]):
    
    monkeypatch.setattr("builtins.input",lambda _: "t")
    with pytest.raises(ValueError,match="Le membre renseigné n'existe pas"):
        suppression_membre(cercles)
    
#renseigner un entier valide fonctionne
def test_function_demande_entier(monkeypatch: pytest.MonkeyPatch):
    
    monkeypatch.setattr("builtins.input",lambda _: "2")
    choix=demander_entier("Sasir votre choix",1,5)
    assert choix==2

#test entier pas dans l'intervalle
def test_function_demande_entier_invalide(monkeypatch: pytest.MonkeyPatch):
    
    monkeypatch.setattr("builtins.input",lambda _: "7")
    choix=demander_entier("Sasir votre choix",1,5)
    assert choix==None
    
def test_function_demande_entier_type_invalide(monkeypatch: pytest.MonkeyPatch):
    
    
    with pytest.raises(ValueError,match="Renseigner un entier"):
        monkeypatch.setattr("builtins.input",lambda _: "a")
        choix=demander_entier("Sasir votre choix",1,5)
   
    

        