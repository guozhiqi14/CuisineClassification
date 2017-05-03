'''
Maintain only noun in the ingredients and remove all adj/adv etc.

Input: A list with all ingredeients(all_ingredients)
'''

import nltk
from nltk import word_tokenize,sent_tokenize

def remove_adj(all_ingredients):
	new_ingredients = ['' for _ in range(len(all_ingredients))]
	for i in range(len(all_ingredients)):
		ingredient = all_ingredients[i]

		words = word_tokenize(ingredient)
		tagged = nltk.pos_tag(words)

		nouns = [word for word,pos in tagged \
		if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]

		for item in nouns:
			new_ingredients[i] = new_ingredients[i] + ' '+ item


	#remove whitespace at the beginning
	new_ingredients = [ingredient.replace(' ','',1) for ingredient in new_ingredients]

	#remove repetitive ingredients 
	new_ingredients = list(set(new_ingredients))

	#remove blank space
	new_ingredients = list(filter(None, new_ingredients))

	return new_ingredients


