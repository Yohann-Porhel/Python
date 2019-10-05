# -*- coding:utf-8 -*-

import donnees
import random

def choisir_un_mot_aleatoirement():
    return random.choice(donnees.liste_des_mots)

def valider_saisie_utilisateur(lettre_saisie, tentatives_restantes, liste_lettres_saisies):
    lettre_formatee = lettre_saisie.upper()
    if lettre_formatee in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
        if lettre_formatee not in liste_lettres_saisies:
            tentatives_restantes-=1
            liste_lettres_saisies.append(lettre_formatee)
        else :
            liste_triee_lettres_saisies = sorted(liste_lettres_saisies)
            print("Lettre déjà saisie !!! Vos lettres : "+str(liste_triee_lettres_saisies))
    else:
        print("Votre saisie est incorrecte")

    return lettre_formatee, tentatives_restantes, liste_lettres_saisies

def verification_lettre_saisie_presente_dans_mot(mot_choisi, lettre_saisie, mot_affiche):

    lettres_mot_choisi = list(mot_choisi)
    lettres_mot_affiche = list(mot_affiche)

    for position_lettre, lettre_courante in enumerate(lettres_mot_choisi):
        if lettre_courante == lettre_saisie:
            lettres_mot_affiche[position_lettre] = lettre_saisie

    mot_a_afficher = ''.join(lettres_mot_affiche)
    return mot_a_afficher