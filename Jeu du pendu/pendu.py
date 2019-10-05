# -*- coding:utf-8 -*-

import donnees
import fonctions

tentatives_restantes = 8
mot_affiche = str("********")
liste_lettres_saisies = []

mot_choisi = fonctions.choisir_un_mot_aleatoirement()
# pour le debug evidemment
#print("Le mot à trouver est : "+mot_choisi)

while tentatives_restantes>0:
    lettre_saisie=input("Reste " + str(tentatives_restantes) + " tentative(s). Votre saisie : ")
    lettre_validee, tentatives_restantes, liste_lettres_saisies = fonctions.valider_saisie_utilisateur(lettre_saisie, tentatives_restantes, liste_lettres_saisies)
    mot_affiche = fonctions.verification_lettre_saisie_presente_dans_mot(mot_choisi, lettre_validee, mot_affiche)

    if "*" in mot_affiche:
        if tentatives_restantes>0:
            print("--------------------------------------------")
            print("Votre mot : "+str(mot_affiche))
        else:
            print("PERDU !!! Le mot était : "+str(mot_choisi))
    else: 
        print ("BRAVO !!! Vous avez trouvé : "+str(mot_affiche))
        break