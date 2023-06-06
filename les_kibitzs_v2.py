# Groupe : Les Kibitzs
# Membres : Alexandre ROBERT et Younes BOKHARI

import time
start_time = time.time()

# lecture des données
def recuperer_donnees(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        donnees = fichier.readlines()

    # ligne 2 = longueur du pont, ligne 4 = capacité du pont
    pont = [int(donnees[1]), int(donnees[3])]

    # ligne 6 = nombre de personnes
    nb_personnes = int(donnees[5])

    # les autres lignes sont les personnes
    personnes = []
    for i in range(6, 6 + (2 * nb_personnes), 2):
        poids = int(donnees[i].strip())
        vitesse = int(donnees[i+1].strip())
        personnes.append([poids, vitesse])

    return pont, personnes

# jeu de données à changer ici
pont, personnes = recuperer_donnees(r'jeu1.txt')

# fonctions de tri
def tri_poids_croissant(personnes):
    return sorted(personnes, key=lambda personne: personne[0])

def tri_poids_decroissant(personnes):
    return sorted(personnes, key=lambda personne: personne[0], reverse=True)

def tri_vitesse_croissante(personnes):
    return sorted(personnes, key=lambda personne: personne[1])

def tri_vitesse_decroissante(personnes):
    return sorted(personnes, key=lambda personne: personne[1], reverse=True)

# faire traverser les personnes sur le pont de singe
def traverser_personnes(pont, personnes):
    i = 0
    temps_calcule = 0
    poids_total = 0
    personnes_sur_pont = []

    for i in range(len(personnes)):
        poids_personne, vitesse_personne = personnes[i]
        # la personne peut monter sur le pont
        if poids_total + poids_personne <= pont[1]:
            personnes[i][1] = min(vitesse_personne, personnes[i-1][1])
            personnes_sur_pont.append(personnes[i])
            poids_total += poids_personne
        else:
            est_premiere_personne = True
            for personne_sur_pont in personnes_sur_pont:
                poids_personne_sur_pont, vitesse_personne_sur_pont = personne_sur_pont
                if est_premiere_personne:
                    vitesse_premiere_personne = vitesse_personne_sur_pont
                    poids_total -= poids_personne_sur_pont
                    personnes_sur_pont.remove(personne_sur_pont)
                    est_premiere_personne = False
                else:
                    if vitesse_personne_sur_pont == vitesse_premiere_personne:
                        poids_total -= poids_personne_sur_pont
                        personnes_sur_pont.remove(personne_sur_pont)
                    else:
                        temps_calcule += pont[0] / vitesse_premiere_personne
                        break
            i -= 1
    
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Temps calculé :", temps_calcule, "s")
    print("Temps d'exécution:", execution_time, "ms")

# ordre initial des données
print("1. Ordre initial des données")
traverser_personnes(pont, personnes)
print("_________________________________________________________________")
print("")

# ordre des données triées par vitesse décroissante
print("2. Ordre des données triées par vitesse décroissante")
personnes_triees_vitesse_decroissante = tri_vitesse_decroissante(personnes)
traverser_personnes(pont, personnes_triees_vitesse_decroissante)
print("_________________________________________________________________")
print("")

# ordre des données triées par poids croissant
print("3. Ordre des données triées par poids croissant")
personnes_triees_poids_croissant = tri_poids_croissant(personnes)
traverser_personnes(pont, personnes_triees_poids_croissant)
print("_________________________________________________________________")
print("")