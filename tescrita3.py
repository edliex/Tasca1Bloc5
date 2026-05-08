"""
Exercici 2 (3 punts)
Escriu una funció trobar_edat_maxima(persones) que rebi una llista de diccionaris amb claus 'nom' (string) i 'edat' (int), i retorni l'edat més alta. Valida que 
la llista no sigui buida i que tots els diccionaris tinguin les claus correctes, sinó retorna -1. Dóna la sortida de les crides de prova.
def trobar_edat_maxima(persones):
    # El teu codi aquí

"""

def trobar_edat_maxima(persones):
    if not persones:
        return -1
    for persona in persones:
        if not isinstance(persona, dict) or "nom" not in persona or "edat" not in persona:
            return -1
        
    edats = [persona["edat"] for persona in persones]
    return max(edats)

"""
Exercici 3 (2 punts)
Fes una funció trobar_producte_mes_car() que retorni el diccionari del producte amb el preu més alt de la variable global productes. Si la llista global està buida, retorna None.
# Variable global

"""
productes = [
        {
        'nom': 'Portàtil Dell XPS 15',
        'preu': 1299.99,
        'categoria': 'Informàtica',
        'stock': 5
    },
    {
        'nom': 'Ratolí Logitech MX Master',
        'preu': 89.99,
        'categoria': 'Perifèrics',
        'stock': 15
    },
    {
        'nom': 'Monitor Samsung 27"',
        'preu': 349.50,
        'categoria': 'Monitors',
        'stock': 8
    }]

def trobar_producte_mes_car(productes):
    # El teu codi aquí
    if not productes:
        return None
    producte_mes_car = productes[0]
    #print(preu_max)
    
    for producte in productes:
        if producte["preu"] > producte_mes_car["preu"]:
            print("producte actualitzat")
            producte_mes_car = producte    
    return producte_mes_car


producte = trobar_producte_mes_car(productes)
print(producte)


"""
Exercici 4 (3 punts)
Escriu una funció comptar_empleats_per_departament(empresa) que rebi una diccionari amb claus 'nom' i 'departaments' on departaments és una llista de diccionaris amb 'nom' i 'empleats', i retorni un diccionari amb el nom de cada departament i el seu número d'empleats. Fes un exemple de crida de la funció i dóna la sortida per les dades de prova empresa_de_prova.


"""
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

def comptar_empleats_per_departament(empresa):
    # El teu codi aqui
    departaments = {}
    if not empresa:
        return {}
    for departament in empresa["departaments"]:
        departaments[departament["nom"]] = len(departament["empleats"])
    return departaments
