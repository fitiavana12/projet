# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:24:57 2023

@author: NewUser
"""


import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice")

        # Créer un champ de texte pour afficher les résultats
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Créer des boutons pour les opérations arithmétiques de base
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]
        for i, button in enumerate(buttons):
            row = i // 4 + 1
            col = i % 4
            btn = tk.Button(master, text=button, width=5, height=2)
            btn.grid(row=row, column=col, padx=3, pady=3)
            btn.bind("<Button-1>", lambda e, button=button: self.append_to_display(button))
            
        # Créer le bouton d'égalité et le lier à la méthode calculate
        equal_button = tk.Button(master, text="=", width=5, height=2)
        equal_button.grid(row=5, column=2, padx=3, pady=3)
        equal_button.bind("<Button-1>", lambda e: self.calculate())

    def append_to_display(self, text):
        self.display.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()






                       