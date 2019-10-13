# -*- coding:utf-8 -*-

import donnees
import json
import random

def choisir_un_mot_aleatoirement():
    global mot_choisi
    mot_choisi = random.choice(donnees.liste_des_mots)
    return mot_choisi

def masquer_mot_a_trouver(mot_choisi):
    mot_masque = "*"*len(mot_choisi)
    print("Mot à trouver : "+str(mot_masque))
    return mot_masque

def valider_saisie_nom():
    nom_joueur = input("Veuillez saisir votre nom : ")
    if not nom_joueur:
        valider_saisie_nom()
    return nom_joueur

def valider_saisie_utilisateur(saisie, tentatives_restantes, liste_lettres_saisies):
    saisie_formatee = saisie.upper()

    if saisie_formatee == mot_choisi :
        saisie_formatee = mot_choisi
    else :
        if saisie_formatee in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
            if saisie_formatee not in liste_lettres_saisies:
                tentatives_restantes-=1
                liste_lettres_saisies.append(saisie_formatee)
            else:
                liste_triee_lettres_saisies = sorted(liste_lettres_saisies)
                print("Lettre déjà saisie !!! Vos lettres : "+str(liste_triee_lettres_saisies))
        else :
            print("Votre saisie est incorrecte")

    return saisie_formatee, tentatives_restantes, liste_lettres_saisies

def verification_lettre_saisie_presente_dans_mot(mot_choisi, saisie_validee, mot_affiche):

    if saisie_validee == mot_choisi:
        mot_a_afficher = mot_choisi
    else :
        lettres_mot_choisi = list(mot_choisi)
        lettres_mot_affiche = list(mot_affiche)

        for position_lettre, lettre_courante in enumerate(lettres_mot_choisi):
            if lettre_courante == saisie_validee:
                lettres_mot_affiche[position_lettre] = saisie_validee

        mot_a_afficher = ''.join(lettres_mot_affiche)
    
    return mot_a_afficher

def enregistrer_score(score):

    with open('scores.json','a') as fichier_scores:
        json.dump(score, fichier_scores)
