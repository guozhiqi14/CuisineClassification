import numpy as np
import pandas as pd
import sklearn.feature_selection

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


#calculate the mutual information of all the variables 
mutual_info = sklearn.feature_selection.mutual_info_classif(ingredient_matrix,train_set['cuisine'])
mu = mutual_info.argsort()
mutual_information = np.zeros(len(mu))
for i in range(len(mu)):
    mutual_information[i] = mutual_info[mu[i]]
for i in range(len(mu)):
    mutual_information.append([mutual_info[mu[i]],mu[i]])
top_mutual = 200
index = [x[1] for x in mutual_information[-top_mutual:]]
[(list(ingredients)[ind],mutual_info[ind]) for ind in index]
