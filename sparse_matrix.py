import numpy as np
import pandas as pd
train_set = pd.read_json('train.json') 
ingred = []
for x in train_set['ingredients']:
    for ingre in x:
        ingred.append(ingre)

ingredients = set(ingred)
ingredient_matrix = pd.DataFrame(np.zeros([train_set.shape[0],len(ingredients)]),columns = list(ingredients))
for i in range(train_set.shape[0]):
    for ingredient in train_set.iloc[i][2]:
        ingredient_matrix.iloc[i][ingredient] +=1