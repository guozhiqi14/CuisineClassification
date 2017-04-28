'''
Calculate misclassification rate be if one were to randomly assign a recipe to a cuisine, 
according to the proportion of recipes in the training data that fell into that cuisine.
Serving as the baseline performance compared to the training model. 
'''

import numpy as np 

#Generate samples based on distribution for cuisines in the original dataset 
def get_sample():
	sample = np.random.choice(np.arange(1, 21), p=[0.197063, 0.161865, 0.108614, 0.075502, 0.067205,\
									  0.066526, 0.038870, 0.038694, 0.035777, 0.029542,\
									  0.024865, 0.020868, 0.020742, 0.020642, 0.020214,\
									  0.018982, 0.016770, 0.013225, 0.012294, 0.011740])
	return sample 


cuisine_dict = {'italian':1, 'mexican':2, 'southern_us':3, 'indian':4, 'chinese':5, \
				'french':6, 'cajun_creole':7, 'thai':8,'japanese':9, 'greek':10, \
				'spanish':11, 'korean':12, 'vietnamese':13, 'moroccan':14, 'british':15, \
				'filipino':16, 'irish':17, 'jamaican':18, 'russian':19, 'brazilian':20}


#Get the baseline accuracy by loop whole dataset five times and average the score
def Base_accuracy(train_set):
	counter = 0
	accuracy = 0
	iteration  = len(train_set)
	while counter < 5:
		for i in range(iteration):
			sample = get_sample()
			if cuisine_dict[train_set['cuisine'][i]] == sample:
				accuracy += 1
		counter+=1

	return accuracy/(counter*iteration)

