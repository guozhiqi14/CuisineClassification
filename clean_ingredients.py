'''
Clean ingredients list by removing all useless symbols & numbers & punctuation Marks etc.
Inputs: An Ingredients list(all_ingredients in notebook) which contains all uniques ingredients in data set
'''
import re
from nltk.stem import PorterStemmer


def clean_ingredients(all_ingredients):
	all_ingredients = [ingredient.lower() for ingredient in all_ingredients]
	all_ingredients = [ingredient.replace('&','').replace('%','').replace('(','').replace(')','').\
								  replace('®','').replace('.','').replace('/','')\
								  for ingredient in all_ingredients]


	all_ingredients = [re.sub("\d+", "", ingredient) for ingredient in  all_ingredients]
	all_ingredients = [re.sub(r'[?|$|.|!+]',r'',ingredient) for ingredient in  all_ingredients]
	all_ingredients = [re.sub(r'\\\\',r'',ingredient) for ingredient in  all_ingredients]

	stemmer=PorterStemmer()
	all_ingredients = [stemmer.stem(ingredient) for ingredient in all_ingredients]

	#stemming words
	new_ingredients = ['' for _ in range(len(all_ingredients))]
	for i in range(len(all_ingredients)):
		ingredient = all_ingredients[i]
		for word in ingredient.split():
			word = stemmer.stem(word)
			new_ingredients[i] = new_ingredients[i] + ' '+ word


	#remove whitespace at the beginning
	new_ingredients = [ingredient.replace(' ','',1) for ingredient in new_ingredients]

	return new_ingredients





