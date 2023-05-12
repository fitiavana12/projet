# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:51:24 2023

@author: NewUser
"""


from random import randint

def L(n, a, b):
    return [randint(a, b) for _ in range(n)]
