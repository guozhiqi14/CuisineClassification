
'''
User defined stemmer for stemming before one can CountVectorize the ingredients 
In this module, stemmers might include PorterStemmer,SnowballStemmer,LancasterStemmer
'''


from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer


#porter_stemmer
def porter_stemmer(ingredient):
	temp_lst = []
	stemmer=PorterStemmer()

	for i in ingredient:
		words = ' '.join([stemmer.stem(word) for word in i.split()])
		temp_lst.append(words)

	return temp_lst


#Snowball_Stemmer
def snowball_stemmer(ingredient):
	temp_lst = []
	stemmer = SnowballStemmer("english")

	for i in ingredient:
		words = ' '.join([stemmer.stem(word) for word in i.split()])
		temp_lst.append(words)

	return temp_lst

#Lancaster_Stemmer
def Lancaster_stemmer(ingredient):
	temp_lst = []
	stemmer = LancasterStemmer()

	for i in ingredient:
		words = ' '.join([stemmer.stem(word) for word in i.split()])
		temp_lst.append(words)

	return temp_lst