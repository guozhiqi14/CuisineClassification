import numpy as np
import pandas as pd
import sklearn.feature_selection
#read in training data
train_set = pd.read_json('train.json') 
ingred = []
for x in train_set['ingredients']:
    for ingre in x:
        ingred.append(ingre)
        
#get a set of unique ingredients
ingredients = set(ingred)

#build up sparse matrix: each column name is a unique ingredient, and each row corresponding to a recipe.
ingredient_matrix = pd.DataFrame(np.zeros([train_set.shape[0],len(ingredients)]),columns = list(ingredients))
for i in range(train_set.shape[0]):
    for ingredient in train_set.iloc[i][2]:
        ingredient_matrix.iloc[i][ingredient] +=1

#calculate the mutual information of all the variables.
mutual_info = sklearn.feature_selection.mutual_info_classif(ingredient_matrix,train_set['cuisine'])
mu = mutual_info.argsort() #get sorted index for mutual information 
mutual_information = np.zeros(len(mu))
for i in range(len(mu)):
    mutual_information[i] = mutual_info[mu[i]] #get sorted mutual information

    
mutual_information_ingredient = np.zeros(len(mu))
for i in range(len(mu)):
    mutual_information_ingredient.append([mutual_info[mu[i]],mu[i]]) #a tuple of ingredient and multual information

top_mutual = (mutual_info.shape - sum(mutual_info == 0)) #the number of ingredients that have most multual info 
index = [x[1] for x in mutual_information[-top_mutual:]]
[(list(ingredients)[ind],mutual_info[ind]) for ind in index] #print the ingredients that have mutual information
ingred_mutual = [list(ingredients)[ind] for ind in index]

#cleansed matrix that have only ingredients that have most multual information
cleansed_ind_matrix = ingredient_matrix[ingred_mutual]
