# -*- coding:utf-8 -*-

import donnees
import fonctions

liste_lettres_saisies = []
tentatives_restantes = 8
mot_choisi = fonctions.choisir_un_mot_aleatoirement()
nom_joueur = fonctions.valider_saisie_nom()
mot_affiche = fonctions.masquer_mot_a_trouver(mot_choisi)


while tentatives_restantes>0:
    lettre_saisie=input("Reste " + str(tentatives_restantes) + " tentative(s). Votre saisie : ")
    lettre_validee, tentatives_restantes, liste_lettres_saisies = fonctions.valider_saisie_utilisateur(lettre_saisie, tentatives_restantes, liste_lettres_saisies)
    mot_affiche = fonctions.verification_lettre_saisie_presente_dans_mot(mot_choisi, lettre_validee, mot_affiche)

    if "*" in mot_affiche:
        if tentatives_restantes>0:
            print("------------------------------------------------------------------------------------------------------------------")
            print("Votre mot : "+str(mot_affiche))
        else:
            print("PERDU "+str(nom_joueur)+" !!! Le mot était : "+str(mot_choisi))
    else:
        print ("BRAVO "+str(nom_joueur)+" !!! Vous avez trouvé : "+str(mot_choisi))
        break