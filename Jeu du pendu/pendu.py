# -*- coding:utf-8 -*-

import donnees
import fonctions
import os

# Variables
liste_lettres_saisies = []
tentatives_restantes = 8
mot_choisi = fonctions.choisir_un_mot_aleatoirement()
nom_joueur = fonctions.valider_saisie_nom()
mot_affiche = fonctions.masquer_mot_a_trouver(mot_choisi)

# Boucle principale du jeu
while tentatives_restantes>0:
    saisie=input("Reste " + str(tentatives_restantes) + " tentative(s). Votre saisie : ")
    saisie_validee, tentatives_restantes, liste_lettres_saisies = fonctions.valider_saisie_utilisateur(saisie, tentatives_restantes, liste_lettres_saisies)
    mot_affiche = fonctions.verification_lettre_saisie_presente_dans_mot(mot_choisi, saisie_validee, mot_affiche)

    if "*" in mot_affiche:
        if tentatives_restantes>0:
            print("------------------------------------------------------------------------------------------------------------------")
            print("Votre mot : "+str(mot_affiche))
        else:
            os.system("cls")
            print("PERDU "+str(nom_joueur)+" !!! Le mot à trouver était : "+str(mot_choisi))
    else:
        os.system("cls")
        print ("BRAVO "+str(nom_joueur)+" !!! Vous avez trouvé : "+str(mot_choisi))
        print("Votre score est de "+str(tentatives_restantes)+" point(s).")
        score = {nom_joueur : tentatives_restantes}
        fonctions.enregistrer_score(score)
        break