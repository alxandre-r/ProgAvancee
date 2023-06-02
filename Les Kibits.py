# GROUPE : LES KIBITS
# Membres : Alexandre ROBERT et Younes BOKHARI

import time
start_time = time.time()

# Lecture des données
def lire_donnees_fichier(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        donnees = fichier.readlines()

    # ligne 2 = longueur du pont, ligne 4 = capacité du pont
    pont = (int(donnees[1]), int(donnees[3]))

    # ligne 6 = nombre de personnes
    nb_personnes = int(donnees[5])

    # les lignes après la ligne 5 sont les personnes
    personnes = []
    for i in range(6, 6 + (2 * nb_personnes), 2):
        poids = int(donnees[i].strip())
        vitesse = int(donnees[i+1].strip())
        personnes.append((poids, vitesse))

    return pont, personnes

#changer ici le jeu de données
pont, personnes = lire_donnees_fichier(r'C:\Users\dubte\COURS A1\Programmation Avancée\ExamProgAvancee\jeu2.txt')

# trie les personnes par leurs poids croissant
def tri_personnes_poids_croissant(personnes):
    return sorted(personnes, key=lambda personne: personne[0])

# tri les personnes par leurs poids décroissant
def tri_personnes_poids_decroissant(personnes):
    return sorted(personnes, key=lambda personne: personne[0], reverse=True)

# trie les personnes par leurs vitesse croissant
def tri_personnes_vitesse_croissant(personnes):
    return sorted(personnes, key=lambda personne: personne[1])

# trie les personnes par leurs vitesse décroissant
def tri_personnes_vitesse_decroissant(personnes):
    return sorted(personnes, key=lambda personne: personne[1], reverse=True)

# Affichage des données
print("Longueur du pont :", pont[0])
print("Capacité du pont :", pont[1])
print("Nombre de personnes :", len(personnes))
#print("Détails des personnes :")
#for i, (poids, vitesse) in enumerate(personnes):
    #print(f"Personne {i + 1} - Poids : {poids}, Vitesse : {vitesse}")
    
print("")
print 

    # =================================================================================================================== #
    
def fait_passer_personnes(pont, personnes):
    temps_total = 0
    i = 0
    while personnes:
        temps_passage = 0
        poids_total = 0

        # Sélectionner les personnes qui peuvent traverser dans ce tour
        personnes_traverser = []
        for personne in personnes:
            poids_personne, vitesse_personne = personne
            if poids_total + poids_personne <= pont[1]:
                personnes_traverser.append(personne)
                poids_total += poids_personne

        # Faire traverser les personnes sélectionnées
        for personne in personnes_traverser:
            poids_personne, vitesse_personne = personne
            temps_personne = pont[0] / vitesse_personne
            temps_passage = max(temps_passage, temps_personne)

        # Mettre à jour le temps total et les personnes restantes
        temps_total += temps_passage
        personnes = [personne for personne in personnes if personne not in personnes_traverser]
        
        i+=1
        # Afficher les résultats
        print(f"Tour {i} : {len(personnes_traverser)} personnes traversent en {temps_passage} secondes")
        # vitesse de ce tour
        print(f"Vitesse des personnes de ce tour :")
        for personne in personnes_traverser:
            poids_personne, vitesse_personne = personne
            print(vitesse_personne, end=' ')
        print (f"Temps de passage total: {temps_total} secondes")
        print(f"Personnes restantes: {len(personnes)}")
        print("")
        
    end_time = time.time()  # Temps de fin
    execution_time = (end_time - start_time) * 1000  # Temps d'exécution en millisecondes
    print("Temps d'exécution:", execution_time, "ms")

# 1. Ordre initial des données
print("1. Ordre initial des données")
fait_passer_personnes(pont, personnes)
print("_________________________________________________________________")
print("")

# 2. Ordre des données triées par vitesse décroissante
print("2. Ordre des données triées par vitesse décroissante")
personnes_triees_vitesse_decroissante = tri_personnes_vitesse_decroissant(personnes)
fait_passer_personnes(pont, personnes_triees_vitesse_decroissante)
print("_________________________________________________________________")
print("")

# 3. Ordre des données triées par poids croissant
print("3. Ordre des données triées par poids croissant")
personnes_triees_poids_decroissante = tri_personnes_poids_decroissant(personnes)
fait_passer_personnes(pont, personnes_triees_poids_decroissante)
print("_________________________________________________________________")
print("")

