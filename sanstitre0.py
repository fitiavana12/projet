# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:38:01 2023

@author: NewUser
"""
def m0(data):

    n= len(data)

    somme=sum(data)) 
    if n==0:

        return 0

    else:

        return somme/n 

def v0(data):

    n= len(data)

    m=m0(data)

    somme=0 

    for x in data:

        somme somme + (x-m)**2

    return somme/n

def co(datax,datay):

    n= len(datax) # = len(listey) 

    mx = m0(datax)

    my= m0(datay) 

    somme=0

    for i in range(n):

        x = datax[i]

        y= datay[i]

        somme=somme + (x-mx) * (y-my) 

    return somme/n

input = [1, 2, 3, 4, 5]
print("m0(input):", m0(input))

print("v0(input):", v0(input))

datax = [1, 2, 3, 4, 5]
datay = [4, 5, 4, 7, 6]
print("c0(inputx,inputy):", co(datax, datay))



