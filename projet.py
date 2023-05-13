# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:24:29 2023

@author: NewUser
"""
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("housing.csv")
data.dropna(inplace=True)

x = data.drop(['median_house_value'], axis=1)
y = data['median_house_value']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
train_data = x_train.join(y_train)

train_data.hist(figsize=(15,8))

plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(), annot=True, cmap="YlOrBr")

train_data['total_rooms'] = np.log(train_data['total_rooms'] + 1)
train_data['total_bedrooms'] = np.log(train_data['total_bedrooms'] + 1)
train_data['population'] = np.log(train_data['population'] + 1)
train_data['households'] = np.log(train_data['households'] + 1)

train_data.hist(figsize=(15,8))

#print(train_data.ocean_proximity.value_counts())
train_data = train_data.join(pd.get_dummies(train_data.ocean_proximity)).drop(['ocean_proximity'], axis = 1)
plt.figure(figsize=(15,8))
sns.scatterplot(x="latitude", y="longitude", data = train_data, hue="median_house_value", palette="coolwarm")

train_data['bedrooms_ration'] = train_data['total_bedrooms'] / train_data['total_rooms']
train_data['houseold_rooms'] = train_data['total_rooms'] / train_data['households']
plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(), annot=True, cmap="YlOrBr")

x_train, y_train = train_data.drop(['median_house_value'], axis=1), train_data['median_house_value']
reg = LinearRegression()
reg.fit(x_train, y_train)
LinearRegression()
test_data = x_test.join(y_test)

test_data['total_rooms'] = np.log(test_data['total_rooms'] + 1)
test_data['total_bedrooms'] = np.log(test_data['total_bedrooms'] + 1)
test_data['population'] = np.log(test_data['population'] + 1)
test_data['households'] = np.log(test_data['households'] + 1)

#train_data = train_data.join(pd.get_dummies(train_data.ocean_proximity).add_suffix('_proximity')).drop(['ocean_proximity'], axis = 1)
test_data = train_data.join(pd.get_dummies(test_data.ocean_proximity)).drop(['ocean_proximity'], axis = 1)

test_data['bedrooms_ration'] = test_data['total_bedrooms'] / test_data['total_rooms']
test_data['houseold_rooms'] = test_data['total_rooms'] / test_data['households']
'''




import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.svm import svr
#from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("housing.csv")
data.dropna(inplace=True)
print(data)

x = data.drop(['median_house_value'], axis=1)
y = data['median_house_value']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
train_data = x_train.join(y_train)

train_data.hist(figsize=(15,8))

#plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(), annot=True, cmap="YlOrBr")

train_data['total_rooms'] = np.log(train_data['total_rooms'] + 1)
train_data['total_bedrooms'] = np.log(train_data['total_bedrooms'] + 1)
train_data['population'] = np.log(train_data['population'] + 1)
train_data['households'] = np.log(train_data['households'] + 1)

#train_data.hist(figsize=(15,8))



#print(train_data.ocean_proximity.value_counts())
#train_data = train_data.join(pd.get_dummies(train_data.ocean_proximity)).drop(['ocean_proximity'], axis = 1)
train_data = pd.get_dummies(train_data, columns=['ocean_proximity'], prefix='ocean_proximity')

plt.figure(figsize=(15,8))
sns.scatterplot(x="latitude", y="longitude", data = train_data, hue="median_house_value", palette="coolwarm")

train_data['bedrooms_ration'] = train_data['total_bedrooms'] / train_data['total_rooms']
train_data['houseold_rooms'] = train_data['total_rooms'] / train_data['households']
plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(), annot=True, cmap="YlOrBr")

scaler = StandardScaler()

x_train, y_train = train_data.drop(['median_house_value'], axis=1), train_data['median_house_value']
x_train_s = scaler.fit_transform(x_train)
x_test_s = scaler.transform(x_test)

reg = LinearRegression()
reg.fit(x_train_s, y_train)
LinearRegression()

test_data = x_test.join(y_test)

test_data['total_rooms'] = np.log(test_data['total_rooms'] + 1)
test_data['total_bedrooms'] = np.log(test_data['total_bedrooms'] + 1)
test_data['population'] = np.log(test_data['population'] + 1)
test_data['households'] = np.log(test_data['households'] + 1)

test_data = test_data.join(pd.get_dummies(test_data.ocean_proximity)).drop(['ocean_proximity'], axis = 1)

test_data['bedrooms_ration'] = test_data['total_bedrooms'] / test_data['total_rooms']
test_data['houseold_rooms'] = test_data['total_rooms'] / test_data['households']

x_test, y_test = test_data.drop(['median_house_value'], axis=1), test_data['median_house_value']
x_test_s = scaler.transform(x_test)
reg.score(x_test_s, y_test)

# Prédiction sur les données de test
y_pred = reg.predict(x_test_s)

# Affichage des prédictions
print("Prédictions :", y_pred)

data.dropna(inplace=True)

# Demander les facteurs à l'utilisateur
print("Entrez les facteurs pour afficher les valeurs médianes de la maison correspondantes : ")
longitude = float(input("Longitude : "))
latitude = float(input("Latitude : "))
housing_median_age = int(input("Âge médian du logement : "))
total_rooms = int(input("Nombre total de chambres dans le bloc de logements : "))
total_bedrooms = int(input("Nombre total de chambres dans le bloc de logements : "))
population = int(input("Population totale dans le bloc de logements : "))
households = int(input("Nombre total de ménages dans le bloc de logements : "))
median_income = float(input("Revenu médian des ménages dans le bloc de logements : "))
ocean_proximity = input("Proximité de l'océan (1 s'il est proche, 0 sinon) : ")

# Créer une nouvelle ligne avec les facteurs entrés par l'utilisateur
new_row = pd.DataFrame({
    'longitude': [longitude],
    'latitude': [latitude],
    'housing_median_age': [housing_median_age],
    'total_rooms': [total_rooms],
    'total_bedrooms': [total_bedrooms],
    'population': [population],
    'households': [households],
    'median_income': [median_income],
    'ocean_proximity_<1H OCEAN': [1 if ocean_proximity == '1' else 0],
    'ocean_proximity_INLAND': [1 if ocean_proximity == '0' else 0],
    'ocean_proximity_ISLAND': [0],
    'ocean_proximity_NEAR BAY': [0],
    'ocean_proximity_NEAR OCEAN': [0]
})

# Ajouter la nouvelle ligne au dataset
data_with_new_row = pd.concat([data, new_row], ignore_index=True)

# Calculer la valeur médiane de la maison pour la nouvelle ligne
median_house_value = data_with_new_row['median_house_value'].median()

# Afficher la valeur médiane de la maison pour les facteurs entrés
print("La valeur médiane de la maison pour les facteurs entrés est :", median_house_value)












