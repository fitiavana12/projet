# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:42:59 2023

@author: NewUser
"""
from random import randint

def L(n, a, b):
    return [randint(a, b) for _ in range(n)]

n = int(input('entrez un nombre entier n:'))
a = int(input('entrez un nombre entier a:'))
b = int(input('entrez un nombre entier b:'))
liste = L(n, a, b)
x = int(input('entrez un nombre entier x:'))

print("Liste aléatoire :", liste)
print("Élément à l'indice {} : {}".format(x, liste[x]))


