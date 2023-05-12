# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:45:44 2023

@author: NewUser
"""


from random import randint

def lancer_de():
    resultat = randint(1,6)
    return resultat

resultat_lancer = lancer_de()

a = int(input("Veuillez choisir un nombre : "))

if a == resultat_lancer:
    print("Vous avez gagné !!!!")
else:
    print("Vous avez perdu, le résultat est :", resultat_lancer)