# -*- coding: utf-8 -*-
"""
Created on Thu May 11 07:17:10 2023

@author: NewUser
"""


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Charger les données dans un DataFrame pandas
data = pd.read_csv('nom_du_fichier.csv')

# Sélectionner les variables indépendantes et dépendante
X = data[['surface', 'nombre_de_pieces', 'annee_de_construction', 'quartier']]
y = data['prix']

# Encodage des variables catégorielles
le = LabelEncoder()
X['quartier'] = le.fit_transform(X['quartier'])

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X, y)

# Entrer les facteurs d'une maison pour prédire le prix
surface = float(input("Entrez la surface de la maison : "))
nombre_de_pieces = int(input("Entrez le nombre de pièces : "))
annee_de_construction = int(input("Entrez l'année de construction : "))
quartier = input("Entrez le quartier : ")

quartier_encoded = le.transform([quartier])[0]
X_pred = np.array([[surface, nombre_de_pieces, annee_de_construction, quartier_encoded]])
y_pred = model.predict(X_pred)

print("Le prix prédit pour la maison est de", round(y_pred[0], 2), "euros.")
