# -*- coding: utf-8 -*-
"""Seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ieA-I24dpxuLcXXjyxT6uEAGYeNBsEHg

Seaborn : data visualisation
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""#seaborn has some built in dataset

"""

# total bill vs tip dataset
tips = sns.load_dataset('tips')

tips.head()

# theme of plot
sns.set_theme()
# data visualization 
sns.relplot(data=tips, x ='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')



# load iris dataset
iris = sns.load_dataset("iris")
iris.head()

#scatterplot
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)

#loading titanic dataset
titanic = sns.load_dataset('titanic')
titanic.head()
titanic.shape

#count plot
sns.countplot(x='class',data = titanic)

# Bar plot
sns.barplot(x='sex',y='survived',hue='class',data=titanic)

# load the iris dataset
iris = sns.load_dataset('iris')
iris.head()
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)

sns.scatterplot(x='sepal_length',y='petal_width',hue='species',data=iris)

#houseprice dataset
from sklearn.datasets import load_boston
house_boston = load_boston()

house = pd.DataFrame(house_boston.data, columns=house_boston.feature_names)
house['PRICE'] = house_boston.target

print(house_boston)

house.head()

correlation = house.corr()

#constructing heatmap
plt.figure(figsize=(10,10))
sns.heatmap(cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')