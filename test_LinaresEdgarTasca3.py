from tescrita3 import trobar_edat_maxima, trobar_producte_mes_car, comptar_empleats_per_departament
import pytest

######################################################################
############################# EXERCICI 2 #############################
######################################################################

# RESULTAT OK: 42
# NO HI HA ERRORS
@pytest.mark.parametrize("llista, res_esperat", [(
        [{'nom': 'Anna Garcia', 'edat': 25}, {'nom': 'Marc Puig', 'edat': 42},{'nom': 'Laura Martí', 'edat': 35}], 42
                                                )] )
def test1_trobar_edat_maxima(llista, res_esperat):
    """
    Test de cas correcte.    
    Comprova que la funció retorna l'edat màxima quan rep una llista de diccionaris correcta.

    Args:
        llista (list): Llista d'empleats.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = trobar_edat_maxima(llista)
    assert resultat == res_esperat

# RESULTAT KO: -1
# LI ESTEM DONANT UNA LLISTA VUIDA
@pytest.mark.parametrize("llista, res_esperat", [ ( [], -1 ) ])
def test2_trobar_edat_maxima(llista, res_esperat):
    """
    Test de validació.    
    Comprova que la funció retorna -1 degut a la llista buida.

    Args:
        llista (list): Llista buida.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = trobar_edat_maxima(llista)
    assert resultat == res_esperat

# RESULTAT KO: -1
# EL PRIMER ELEMENT ES UNA LLISTA EN COMPTES D'UN DICCIONARI
@pytest.mark.parametrize("llista, res_esperat", [(
        [['nom', 'Anna Garcia', 'edat', 25], {'nom': 'Marc Puig', 'edat': 42},{'nom': 'Laura Martí', 'edat': 35}], -1
                                                )] )
def test3_trobar_edat_maxima(llista, res_esperat):
    """
    Test de validació.    
    Comprova que la funció retorna -1 degut a la llista en comptes de diccionari.

    Args:
        llista (list): Llista d'empleats.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = trobar_edat_maxima(llista)
    assert resultat == res_esperat

# RESULTAT KO: -1
# LA CLAU "nom" DEL PRIMER DICCIONARI ES INCORRECTA
@pytest.mark.parametrize("llista, res_esperat", [(
        [{'ñom': 'Anna Garcia', 'edat': 25}, {'nom': 'Marc Puig', 'edat': 42},{'nom': 'Laura Martí', 'edat': 35}], -1
                                                )] )
def test4_trobar_edat_maxima(llista, res_esperat):
    """
    Test de validació.    
    Comprova que la funció retorna -1 degut a clau "nom" incorrecte.

    Args:
        llista (list): Llista d'empleats.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = trobar_edat_maxima(llista)
    assert resultat == res_esperat

# RESULTAT KO: -1
# LA CLAU "edat" DEL PRIMER DICCIONARI ES INCORRECTA
@pytest.mark.parametrize("llista, res_esperat", [(
        [{'nom': 'Anna Garcia', 'eñat': 25}, {'nom': 'Marc Puig', 'edat': 42},{'nom': 'Laura Martí', 'edat': 35}], -1
                                                )] )
def test5_trobar_edat_maxima(llista, res_esperat):
    """
    Test de validació.    
    Comprova que la funció retorna -1 degut a clau "edat" incorrecte.

    Args:
        llista (list): Llista d'empleats.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = trobar_edat_maxima(llista)
    assert resultat == res_esperat

######################################################################
############################# EXERCICI 3 #############################
######################################################################

# RESULTAT OK: {'nom': 'Portàtil Dell XPS 15','preu': 1299.99}
# NO HI HA ERRORS
@pytest.mark.parametrize("llista, res_esperat", [(
        [{'nom': 'Ratolí Logitech MX Master','preu': 89.99},{'nom': 'Portàtil Dell XPS 15','preu': 1299.99}], {'nom': 'Portàtil Dell XPS 15','preu': 1299.99} )] )
def test1_trobar_producte_mes_car(llista, res_esperat):
    """
    Test de cas correcte.    
    Comprova que la funció retorna el diccionari correcte amb el preu màxim.

    Args:
        llista (list): Llista dels productes.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = trobar_producte_mes_car(llista)
    assert resultat == res_esperat
    
# RESULTAT KO: None
# LI ESTEM DONANT UNA LLISTA VUIDA
@pytest.mark.parametrize("llista, res_esperat", [(
        [], None )] )
def test2_trobar_producte_mes_car(llista, res_esperat):
    """
    Test de validació.    
    Comprova que la funció retorna None degut a que introduim una llista buida.

    Args:
        llista (list): Llista buida.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = trobar_producte_mes_car(llista)
    assert resultat == res_esperat
    
######################################################################
############################# EXERCICI 4 #############################
######################################################################

# Diccionari de l'empresa de prova
empresa_de_prova = {
    'nom': 'TechCorp',
    'departaments': [
        {
            'nom': 'Informàtica',
            'empleats': [
                {'nom': 'Anna Garcia', 'càrrec': 'Desenvolupadora'},
                {'nom': 'Marc Puig', 'càrrec': 'Analista'},
                {'nom': 'Laura Martí', 'càrrec': 'DevOps'}
            ]
        },
        {
            'nom': 'Recursos Humans',
            'empleats': [
                {'nom': 'Jordi Soler', 'càrrec': 'Director RRHH'},
                {'nom': 'Marta Vidal', 'càrrec': 'Tècnica de selecció'}
            ]
        }]}

# RESULTAT OK: {'Informàtica': 3, 'Recursos Humans': 2}
# NO HI HA ERRORS
@pytest.mark.parametrize("llista, res_esperat", [(
        empresa_de_prova, {'Informàtica': 3, 'Recursos Humans': 2} )] )
def test1_comptar_empleats_per_departament(llista, res_esperat):
    """
    Test de cas correcte.    
    Comprova que la funció retorna el diccionari correcte amb els empleats per departament.

    Args:
        llista (dic): Diccionari del l'empresa amb els departaments.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = comptar_empleats_per_departament(llista)
    assert resultat == res_esperat

# RESULTAT KO: EL PYTEST FALLA
# LI ESTEM PASANT UN DICCIONARI BUIT I LA FUNCIO NO TE CONTROL D'AQUEST ERROR
@pytest.mark.parametrize("llista, res_esperat", [(
        {}, {} )] )
def test2_comptar_empleats_per_departament(llista, res_esperat):
    """
    Test de validació.    
    En aquest test fa fallar el pytest ja que no controla l'error.

    Args:
        llista (dic): Diccionari buit.
        res_esperat (int): Resultat esperat de l'execucio de la funció.
    """
    resultat = comptar_empleats_per_departament(llista)
    assert resultat == res_esperat
