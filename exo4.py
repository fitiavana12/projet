# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:01:38 2023

@author: NewUser
"""
#ecrire une fonction "positif L" qui renvvoie la liste des termes strictement positifs de L dans le meme orderes
from random import randint

def L(n, a, b):
    return [randint(a, b) for _ in range(n)]
n = int(input('entrez un nombre entier n:'))
a = int(input('entrez un nombre entier a:'))
b = int(input('entrez un nombre entier b:'))
liste = L(n, a, b)
positifs = [x for x in liste if x > 0]
print("Liste aléatoire :", liste)
print("Éléments positifs :", positifs)
