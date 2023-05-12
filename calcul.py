# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:31:05 2023

@author: NewUser
"""

from tkinter import*

fenetre = Tk()
boite1 = Frame(fenetre)
fenetre.title('fenetre')
btn2 = Button(boite1,text = '1',width=6,height=1)
btn3 = Button(boite1,text = '+',width=6,height=1)
btn5 = Button(boite1,text = '2',width=6,height=1)
btn6 = Button(boite1,text = '3',width=6,height=1)
btn7 = Button(boite1,text = '4',width=6,height=1)
btn8 = Button(boite1,text = '5',width=6,height=1)
if (btn2):
    valeur1 = 1
if (btn3):
    valeur2 = 3
def calculer():
    reponse = valeur1 + valeur2 
    a.set(reponse)
a = IntVar()   
fenetre.minsize(width=700,height=100)
text = Entry(boite1,textvariable = a)
btn1 = Button(boite1,text = '=',command = calculer)
btn4 = Button(boite1,text = '3',width=6,height=1)



    

















text.pack()
boite1.pack()
btn1.pack(side=LEFT)
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()
fenetre.mainloop()
