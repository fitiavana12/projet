# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:16:40 2023

@author: NewUser
"""


from random import randint

def lancer_des(n):
    """Simule le lancer de n dés."""
    resultat = []
    for i in range(n):
        resultat.append(randint(1, 6))
    return resultat
n = int(input('veuillez entrez le nombre n:'))
resultat1 = lancer_des(n)
print("Les résultats des lancers de dés sont :", resultat1)



