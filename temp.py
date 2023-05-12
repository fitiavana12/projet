Z'''
j=1
while j < 11 :
    print(j,'* 5 =',j*5)
    j=j+1
x = input("Entrez un nombre : ")
entier = int (x)
if x = 3 :
    print('True')
else:
    print('false')
'''
#Boucle for
'''
for i in [1,5,10,15,20]:
    root_i = i**2
    print( i,'*',i,'=',root_i)
'''
#Boucle while
'''
j=1
while j <= 20 :
    root_j = j**2
    print( j,'*',j,'=',root_j)
    j = j+5
'''
'''
x = int(input('Veuillez entrez un entier x='))
if x < 0 :
    y = x+1
if x > 0:
    y = x-1
print('x=', x,'y=', y)
'''
'''
a=int(input('Veuillez entrez un entier a:'))
b=int(input('Veuillez entrez un entier b:'))
if a == 0 & b == 0:
    print('la solution est dans R')
elif a == 0 & b != 0:
    print('pas de solution')
else:
    x=(-b/a)
    print('la solution S=',x)
'''
'''
import math
import cmath
# Fonction qui résout l'équation du second degré
a=int(input('Veuillez entrez un entier a:'))
b=int(input('Veuillez entrez un entier b:'))
c=int(input('Veuillez entrez un entier c:'))
delta = b**2 - 4*a*c   
if delta < 0: 
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print('Les solutions sont x1 =', x1,'et x2 =', x2) 
elif delta == 0:   
    x = -b / (2*a)
    print('La solution unique est x =', x)
else:   
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('Les solutions sont x1 =', x1,'et x2 =', x2) 
'''
'''
i=1
a=int(input('Veuillez entrez un nombre:'))
if a < 11:
    while i <= 10:
        x=a*i
        print(a,'*', i,'=', x)
        i= i+1
elif a > 11:
    b=int(input('Veuillez entrez un autre nombre inferieur a 10:'))
    while i <= 10:
        x=b*i
        print(b,'*', i,'=', x)
        i= i+1
'''
#Dictionnary
#D={'Andry':5 , 'Mirana':2}
'''
x=int(input("Veuillez entrez un nombre:"))
table=[]
for i in range (0,11):
    table.append(i*x)
for i in range (11) :
    print (x, "*", i, "= ", table[i])
'''
#break and continue
'''
j=0
n=int(input("Veuillez entre un nombre:"))
for i in range (n):
    if i < n:
        j=n+i
        print(n,'+', i, '=', j)
'''
#table de multiplication
'''
P=0
j=5
x = int(input("entre un valeur strictement entre 0 a 11:"))
while P==0 :
    Q = (x < 1)
    R = (x > 10)
    if Q or R:
        x=int(input("Entrez une autre valeur strictement entre 0 a 11)
    else:
        P=P+1
        print('Merci','\nTable de multiplication par ',x)
table=[]
for i in range (0,11):
    table.append(i*x)
for i in range (11) :
    print (x, "*", i, "= ", table[i])
'''
'''
import tkinter as tk

# Créer une fenêtre racine
root = tk.Tk()

# Créer un bouton
button = tk.Button(root, text="Cliquez-moi!")

# Afficher le bouton
button.pack()

# Lancer la boucle principale de la fenêtre
root.mainloop()
'''
'''
import matplotlib.pyplot as plt
x = range(1,10)
y = [1, 1.23, 1.41, 1.7, 1.79, 1.98, 2.25, 2.4, 2.39]
plt.scatter(x,y, marker='o',color='red', label = 'IndividuA')
plt.title ('Dissolution d alcool dans le sang')
plt.xlabel('Temps')
plt.ylabel('Alcool')
plt.grid()
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt

# Définir les valeurs de x
x = np.linspace(-2, 2, 500)

# Définir les fonctions de la courbe en forme de cœur
y1 = np.sqrt(1 - np.abs(x)) * np.sqrt(np.abs(x))
y2 = -3 * np.sqrt(1 - np.abs(x)) * np.sqrt(np.abs(x + 1))

# Afficher la courbe
plt.plot(x, y1 + y2, color='red', linewidth=2)

# Afficher les axes et le titre
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.title('Courbe en forme de cœur')

# Afficher la courbe
plt.show()
'''
'''
def fois (x,y):
    z=x*y
    return z
def cc(nom):
    print ("Bonjour",Nom)
    return
def largest(a,b,c):
    if a < b:
        if b < c:
            return c
        else:
            return b
    elif a < c:
        return c 
    else:
       return a
x = largest (4, 8, 6)
'''



import math

print('Calcul de surfaces')

forme_geometrique = input('Veuillez entrer une forme géométrique pour laquelle vous souhaitez calculer la surface: ')


if forme_geometrique.lower() == "cercle":
    
    rayon = int(input('rayon = '))
    
    
    surface = rayon * rayon * math.pi
    
    print("surface =", surface)
    

elif forme_geometrique =="rectangle":
    
    longueur = float (input('longueur='))
    
    largeur = float (input('largeur='))
    
    surface = longueur * largeur
    
    print("surface=", surface)

elif forme_geometrique == carre:
    
    cote = int(input('cote='))
    
    surface = cote * cote 
    
    print('surface=',surface)

elif forme_geometrique == trapeze:
    
    petit_base = float(input('petit_base='))
    
    grand_base = float (input('grand_base='))
    
    hauteur = float (input('hauteur='))
    
    surface = ( (petit_base + grannd_base) * hauteur) / 2
    
    print('surface=',surface)








    

    