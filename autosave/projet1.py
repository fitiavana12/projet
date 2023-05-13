# -*- coding: utf-8 -*-
"""
Created on Thu May 11 07:17:10 2023

@author: NewUser
"""

'''
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
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("housing.csv")
data.dropna(inplace=True)

x = data.drop(['median_house_value'], axis=1)
y = data['median_house_value']

print(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
train_data = x_train.join(y_train)

train_data.hist(figsize=(15,8))

#plt.figure(figsize=(15,8))
#sns.heatmap(train_data.corr(), annot=True, cmap="YlOrBr")

train_data['total_rooms'] = np.log(train_data['total_rooms'] + 1)
train_data['total_bedrooms'] = np.log(train_data['total_bedrooms'] + 1)
train_data['population'] = np.log(train_data['population'] + 1)
train_data['households'] = np.log(train_data['households'] + 1)

train_data['bedrooms_ration'] = train_data['total_bedrooms'] / train_data['total_rooms']
train_data['houseold_rooms'] = train_data['total_rooms'] / train_data['households']
train_data = train_data.join(pd.get_dummies(train_data.ocean_proximity)).drop(['ocean_proximity'], axis = 1)


scaler = StandardScaler()

x_train, y_train = train_data.drop(['median_house_value'], axis=1), train_data['median_house_value']
x_train_s = scaler.fit_transform(x_train)
x_test_s = scaler.transform(x_test)


print(x_train)