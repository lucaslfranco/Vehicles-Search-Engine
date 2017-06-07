import nltk, sys, json, numpy as np


#Read data from stdin
def read_in():
	lines = sys.stdin.readlines()
	#Since our input would only be having one line, parse our JSON data from that
	return json.loads(lines[0])

def classif_data(data):

	train = [
		({'a':'GOL', 'b':'2003', 'c': 'MA'}, 'A'),
		({'a':'GOL', 'b':'2003', 'c': 'SP'}, 'A'),
		({'a':'GOL', 'b':'2003', 'c': 'CE'}, 'A'),
		({'a':'GOL', 'b':'2004', 'c': 'AC'}, 'A'),
		({'a':'GOL', 'b':'2004', 'c': 'RR'}, 'A'),
		({'a':'GOL', 'b':'2005', 'c': 'SP'}, 'A'),
		({'a':'GOL', 'b':'2005', 'c': 'PR'}, 'A'),
		({'a':'GOL', 'b':'2006', 'c': 'PR'}, 'A'),
		({'a':'GOL', 'b':'2006', 'c': 'DF'}, 'B'),
		({'a':'GOL', 'b':'2006', 'c': 'AC'}, 'A'),
		({'a':'GOL', 'b':'2007', 'c': 'CE'}, 'A'),
		({'a':'GOL', 'b':'2007', 'c': 'MA'}, 'A'),
		({'a':'GOL', 'b':'2007', 'c': 'PR'}, 'A'),
		({'a':'GOL', 'b':'2008', 'c': 'SP'}, 'B'),
		({'a':'GOL', 'b':'2008', 'c': 'AC'}, 'A'),
		({'a':'GOL', 'b':'2008', 'c': 'CE'}, 'A'),
		({'a':'GOL', 'b':'2008', 'c': 'PR'}, 'A'),
		({'a':'GOL', 'b':'2008', 'c': 'SP'}, 'B'),
		({'a':'GOL', 'b':'2009', 'c': 'AC'}, 'A'),
		({'a':'GOL', 'b':'2009', 'c': 'DF'}, 'C'),
		({'a':'GOL', 'b':'2009', 'c': 'SP'}, 'B'),
		({'a':'GOL', 'b':'2009', 'c': 'MA'}, 'A'),
		({'a':'GOL', 'b':'2009', 'c': 'CE'}, 'B'),
		({'a':'GOL', 'b':'2009', 'c': 'PR'}, 'B'),
		({'a':'GOL', 'b':'2010', 'c': 'AC'}, 'B'),
		({'a':'GOL', 'b':'2010', 'c': 'PR'}, 'B'),
		({'a':'GOL', 'b':'2010', 'c': 'SP'}, 'B'),
		({'a':'GOL', 'b':'2010', 'c': 'BA'}, 'B'),
		({'a':'GOL', 'b':'2011', 'c': 'PR'}, 'B'),
		({'a':'GOL', 'b':'2011', 'c': 'SP'}, 'C'),
		({'a':'GOL', 'b':'2011', 'c': 'DF'}, 'C'),
		({'a':'GOL', 'b':'2011', 'c': 'MA'}, 'B'),
		({'a':'GOL', 'b':'2011', 'c': 'DF'}, 'C'),
		({'a':'GOL', 'b':'2012', 'c': 'AC'}, 'B'),
		({'a':'GOL', 'b':'2012', 'c': 'SP'}, 'B'),
		({'a':'GOL', 'b':'2012', 'c': 'PR'}, 'C'),
		({'a':'GOL', 'b':'2013', 'c': 'SP'}, 'C'),
		({'a':'GOL', 'b':'2013', 'c': 'MA'}, 'B'),
		({'a':'GOL', 'b':'2014', 'c': 'PR'}, 'C'),
		({'a':'GOL', 'b':'2014', 'c': 'SP'}, 'C'),
		({'a':'GOL', 'b':'2014', 'c': 'AC'}, 'B'),
		({'a':'GOL', 'b':'2014', 'c': 'MA'}, 'C'),
		({'a':'GOL', 'b':'2014', 'c': 'DF'}, 'C'),
		({'a':'GOL', 'b':'2015', 'c': 'SP'}, 'C'),
		({'a':'GOL', 'b':'2015', 'c': 'PR'}, 'C'),
		({'a':'GOL', 'b':'2015', 'c': 'AC'}, 'C'),
		({'a':'GOL', 'b':'2016', 'c': 'DF'}, 'C'),
		({'a':'GOL', 'b':'2016', 'c': 'SP'}, 'C'),
		({'a':'GOL', 'b':'2016', 'c': 'PR'}, 'C'),
		({'a':'GOL', 'b':'2016', 'c': 'CE'}, 'C'),
		({'a':'UNO', 'b':'2005', 'c':'SP'}, 'A'),
		({'a':'UNO', 'b':'2008', 'c':'SP'}, 'A'),
		({'a':'UNO', 'b':'2015', 'c':'SC'}, 'B'),
		({'a':'UNO', 'b':'2009', 'c':'PR'}, 'A'),
		({'a':'UNO', 'b':'2006', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2004', 'c':'CE'}, 'A'),
		({'a':'UNO', 'b':'2007', 'c':'PA'}, 'A'),
		({'a':'UNO', 'b':'2010', 'c':'DF'}, 'B'),
		({'a':'UNO', 'b':'2011', 'c':'RJ'}, 'B'),
		({'a':'UNO', 'b':'2008', 'c':'SP'}, 'A'),
		({'a':'UNO', 'b':'2006', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2005', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2007', 'c':'PR'}, 'A'),
		({'a':'UNO', 'b':'2011', 'c':'SC'}, 'A'),
		({'a':'UNO', 'b':'2016', 'c':'PR'}, 'C'),
		({'a':'UNO', 'b':'2014', 'c':'DF'}, 'C'),
		({'a':'UNO', 'b':'2009', 'c':'SP'}, 'A'),
		({'a':'UNO', 'b':'2008', 'c':'PR'}, 'A'),
		({'a':'UNO', 'b':'2002', 'c':'RJ'}, 'A'),
		({'a':'UNO', 'b':'2001', 'c':'CE'}, 'A'),
		({'a':'UNO', 'b':'2010', 'c':'CE'}, 'A'),
		({'a':'UNO', 'b':'2004', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2003', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2006', 'c':'PR'}, 'A'),
		({'a':'UNO', 'b':'2008', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2009', 'c':'SC'}, 'A'),
		({'a':'UNO', 'b':'2006', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2007', 'c':'SP'}, 'A'),
		({'a':'UNO', 'b':'2008', 'c':'PR'}, 'A'),
		({'a':'UNO', 'b':'2009', 'c':'SC'}, 'A'),
		({'a':'UNO', 'b':'2010', 'c':'DF'}, 'B'),
		({'a':'UNO', 'b':'2011', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2012', 'c':'CE'}, 'B'),
		({'a':'UNO', 'b':'2013', 'c':'AC'}, 'B'),
		({'a':'UNO', 'b':'2014', 'c':'PA'}, 'B'),
		({'a':'UNO', 'b':'2014', 'c':'PR'}, 'B'),
		({'a':'UNO', 'b':'2015', 'c':'AM'}, 'C'),
		({'a':'UNO', 'b':'2003', 'c':'MT'}, 'A'),
		({'a':'UNO', 'b':'2004', 'c':'MS'}, 'A'),
		({'a':'UNO', 'b':'2007', 'c':'RN'}, 'A'),
		({'a':'UNO', 'b':'2002', 'c':'AP'}, 'A'),
		({'a':'UNO', 'b':'2009', 'c':'RS'}, 'A'),
		({'a':'UNO', 'b':'2010', 'c':'SP'}, 'B'),
		({'a':'UNO', 'b':'2012', 'c':'SP'}, 'B'),
		({'a':'UNO', 'b':'2011', 'c':'RJ'}, 'B'),
		({'a':'UNO', 'b':'2013', 'c':'DF'}, 'B'),
		({'a':'UNO', 'b':'2004', 'c':'GO'}, 'B'),
		({'a':'UNO', 'b':'2005', 'c':'MA'}, 'A'),
		({'a':'UNO', 'b':'2006', 'c':'MA'}, 'A'),
		({'a':'FIESTA', 'b':'2007', 'c':'AL'}, 'A'),
		({'a':'FIESTA', 'b':'2004', 'c':'AM'}, 'A'),
		({'a':'FIESTA', 'b':'2010', 'c':'AC'}, 'A'),
		({'a':'FIESTA', 'b':'2012', 'c':'DF'}, 'B'),
		({'a':'FIESTA', 'b':'2001', 'c':'DF'}, 'A'),
		({'a':'FIESTA', 'b':'2002', 'c':'PR'}, 'A'),
		({'a':'FIESTA', 'b':'2003', 'c':'SP'}, 'A'),
		({'a':'FIESTA', 'b':'2004', 'c':'RJ'}, 'A'),
		({'a':'FIESTA', 'b':'2005', 'c':'CE'}, 'A'),
		({'a':'FIESTA', 'b':'2006', 'c':'CE'}, 'A'),
		({'a':'FIESTA', 'b':'2007', 'c':'PA'}, 'A'),
		({'a':'FIESTA', 'b':'2008', 'c':'AP'}, 'A'),
		({'a':'FIESTA', 'b':'2010', 'c':'MS'}, 'B'),
		({'a':'FIESTA', 'b':'2009', 'c':'MT'}, 'B'),
		({'a':'FIESTA', 'b':'2011', 'c':'SP'}, 'B'),
		({'a':'FIESTA', 'b':'2012', 'c':'SP'}, 'B'),
		({'a':'FIESTA', 'b':'2013', 'c':'PR'}, 'B'),
		({'a':'FIESTA', 'b':'2013', 'c':'DF'}, 'C'),
		({'a':'FIESTA', 'b':'2014', 'c':'DF'}, 'C'),
		({'a':'FIESTA', 'b':'2015', 'c':'RJ'}, 'C'),
		({'a':'FIESTA', 'b':'2016', 'c':'SP'}, 'C'),
		({'a':'FIESTA', 'b':'2017', 'c':'PR'}, 'C'),
		({'a':'FIESTA', 'b':'2005', 'c':'MA'}, 'A'),
		({'a':'FIESTA', 'b':'2004', 'c':'MA'}, 'A'),
		({'a':'FIESTA', 'b':'2010', 'c':'RS'}, 'B'),
		({'a':'FIESTA', 'b':'2006', 'c':'PE'}, 'A'),
		({'a':'FIESTA', 'b':'2011', 'c':'AM'}, 'B'),
		({'a':'FIESTA', 'b':'2000', 'c':'CE'}, 'A'),
		({'a':'FIESTA', 'b':'2001', 'c':'MA'}, 'A'),
		({'a':'FIESTA', 'b':'2003', 'c':'SP'}, 'A'),
		({'a':'FIESTA', 'b':'2007', 'c':'SP'}, 'A'),
		({'a':'FIESTA', 'b':'2002', 'c':'SP'}, 'A'),
		({'a':'FIESTA', 'b':'2008', 'c':'RJ'}, 'A'),
		({'a':'FIESTA', 'b':'2010', 'c':'DF'}, 'B'),
		({'a':'FIESTA', 'b':'2012', 'c':'DF'}, 'B'),
		({'a':'FIESTA', 'b':'2004', 'c':'CE'}, 'A'),
		({'a':'FIESTA', 'b':'2002', 'c':'PE'}, 'A'),
		({'a':'FIESTA', 'b':'2004', 'c':'PI'}, 'A'),
		({'a':'FIESTA', 'b':'2005', 'c':'RS'}, 'A'),
		({'a':'FIESTA', 'b':'2012', 'c':'RJ'}, 'B'),
		({'a':'FIESTA', 'b':'2013', 'c':'DF'}, 'C'),
		({'a':'FIESTA', 'b':'2016', 'c':'DF'}, 'C'),
		({'a':'FIESTA', 'b':'2010', 'c':'CE'}, 'A'),
		({'a':'FIESTA', 'b':'2008', 'c':'RJ'}, 'B'),
		({'a':'FIESTA', 'b':'2003', 'c':'CE'}, 'A'),
		({'a':'FIESTA', 'b':'2004', 'c':'PR'}, 'A'),
		({'a':'FIESTA', 'b':'2009', 'c':'SP'}, 'A'),
		({'a':'FIESTA', 'b':'2007', 'c':'GO'}, 'A'),
		({'a':'FIESTA', 'b':'2003', 'c':'AM'}, 'A'),
		({'a':'PRISMA', 'b':'2006', 'c':'CE'}, 'A'),
		({'a':'PRISMA', 'b':'2006', 'c':'SP'}, 'A'),
		({'a':'PRISMA', 'b':'2010', 'c':'SP'}, 'B'),
		({'a':'PRISMA', 'b':'2011', 'c':'RJ'}, 'B'),
		({'a':'PRISMA', 'b':'2006', 'c':'RJ'}, 'A'),
		({'a':'PRISMA', 'b':'2006', 'c':'DF'}, 'A'),
		({'a':'PRISMA', 'b':'2007', 'c':'DF'}, 'A'),
		({'a':'PRISMA', 'b':'2007', 'c':'MA'}, 'A'),
		({'a':'PRISMA', 'b':'2007', 'c':'ES'}, 'A'),
		({'a':'PRISMA', 'b':'2007', 'c':'AM'}, 'A'),
		({'a':'PRISMA', 'b':'2007', 'c':'AP'}, 'A'),
		({'a':'PRISMA', 'b':'2007', 'c':'RS'}, 'A'),
		({'a':'PRISMA', 'b':'2007', 'c':'SC'}, 'A'),
		({'a':'PRISMA', 'b':'2008', 'c':'CE'}, 'A'),
		({'a':'PRISMA', 'b':'2013', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2008', 'c':'RS'}, 'A'),
		({'a':'PRISMA', 'b':'2010', 'c':'MA'}, 'A'),
		({'a':'PRISMA', 'b':'2008', 'c':'MA'}, 'A'),
		({'a':'PRISMA', 'b':'2008', 'c':'AM'}, 'A'),
		({'a':'PRISMA', 'b':'2008', 'c':'SC'}, 'B'),
		({'a':'PRISMA', 'b':'2008', 'c':'SP'}, 'B'),
		({'a':'PRISMA', 'b':'2008', 'c':'DF'}, 'B'),
		({'a':'PRISMA', 'b':'2008', 'c':'RJ'}, 'B'),
		({'a':'PRISMA', 'b':'2008', 'c':'MT'}, 'A'),
		({'a':'PRISMA', 'b':'2009', 'c':'MS'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'PA'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'PR'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'PR'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'MA'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2010', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2010', 'c':'MA'}, 'A'),
		({'a':'PRISMA', 'b':'2010', 'c':'SC'}, 'B'),
		({'a':'PRISMA', 'b':'2010', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2011', 'c':'PA'}, 'B'),
		({'a':'PRISMA', 'b':'2012', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2013', 'c':'SP'}, 'C'),
		({'a':'PRISMA', 'b':'2013', 'c':'ES'}, 'C'),
		({'a':'PRISMA', 'b':'2013', 'c':'SC'}, 'C'),
		({'a':'PRISMA', 'b':'2013', 'c':'DF'}, 'C'),
		({'a':'PRISMA', 'b':'2013', 'c':'DF'}, 'C'),
		({'a':'PRISMA', 'b':'2014', 'c':'RJ'}, 'C'),
		({'a':'PRISMA', 'b':'2014', 'c':'PR'}, 'C'),
		({'a':'PRISMA', 'b':'2014', 'c':'PR'}, 'C'),
		({'a':'PRISMA', 'b':'2015', 'c':'PR'}, 'C'),
		({'a':'PRISMA', 'b':'2016', 'c':'SP'}, 'C'),
		({'a':'PRISMA', 'b':'2016', 'c':'SP'}, 'C'),
		({'a':'PRISMA', 'b':'2016', 'c':'SP'}, 'C'),
		({'a':'PRISMA', 'b':'2016', 'c':'RJ'}, 'C'),
		({'a':'PRISMA', 'b':'2016', 'c':'DF'}, 'C'),
		({'a':'PRISMA', 'b':'2017', 'c':'DF'}, 'C')
	]

	test = [
		({'a':'GOL', 'b':'2003', 'c': 'SP'}, 'A'),
		({'a':'GOL', 'b':'2003', 'c': 'CE'}, 'A'),
		({'a':'GOL', 'b':'2004', 'c': 'PR'}, 'A'),
		({'a':'GOL', 'b':'2004', 'c': 'RR'}, 'A'),
		({'a':'UNO', 'b':'2009', 'c':'SC'}, 'A'),
		({'a':'UNO', 'b':'2015', 'c':'PR'}, 'C'),
		({'a':'UNO', 'b':'2014', 'c':'DF'}, 'B'),
		({'a':'FIESTA', 'b':'2016', 'c':'PR'}, 'C'),
		({'a':'FIESTA', 'b':'2005', 'c':'MA'}, 'A'),
		({'a':'FIESTA', 'b':'2004', 'c':'MA'}, 'A'),
		({'a':'PRISMA', 'b':'2010', 'c':'CE'}, 'B'),
		({'a':'PRISMA', 'b':'2009', 'c':'CE'}, 'B')
	]

	classifier = nltk.classify.NaiveBayesClassifier.train(train)
	# classifier2 = nltk.classify.DecisionTreeClassifier.train(train, entropy_cutoff=0, support_cutoff=0)
	# print(classifier2.pseudocode())
	# print(classifier.show_most_informative_features())
	
	result = [[] for i in range(4)]
	
	#armazena na linha 0 a classificacao feita (classes)
	result[0] = classifier.classify_many(data)
	# result[0].append(classifier2.classify_many(data)[0])
	

	for sample in classifier.prob_classify_many(data):
		#armazena na linha 1 as probabilidades de cada amostra pertencer a classe A
		result[1].append(round(sample.prob('A'), 3))
		#armazena na linha 2 as probabilidades de cada amostra pertencer a classe B
		result[2].append(round(sample.prob('B'), 3))
		#armazena na linha 3 as probabilidades de cada amostra pertencer a classe C
		result[3].append(round(sample.prob('C'), 3))

	return result

def main():
	#get our data as an array from read_in()
	lines = read_in()
	#return the sum to the output stream
	test = classif_data(lines)
	print test



	# ##print('Accuracy: ', nltk.classify.util.accuracy(classifier, test))

	# #print(classifier.show_most_informative_features())

	# import plotly.plotly as py
	# import plotly
	# from plotly.graph_objs import *

	# plotly.tools.set_credentials_file(username='lucasfranco', api_key='XbylJ0SHdLei9Xc2hXY6')

	# data_index = []
	# data = []

	# for feats, classes in train:
	# 	data.append(feats['b'])

	# for index, x in enumerate(data):
	# 	data_index.append(index)

	# trace0 = Scatter(
	# 	x=data_index,
	# 	y=data,
	# 	mode = 'markers'
	# )

	# #print data_index
	# #print data

	# data = Data([trace0])
	# #py.iplot(data, filename = 'basic-line')

	# ##List of states with a enum
	# states = {
	# 	'AC' : 1,
	# 	'AL' : 2,
	# 	'AP' : 3,
	# 	'AM' : 4,
	# 	'BA' : 5,
	# 	'CE' : 6,
	# 	'DF' : 7,
	# 	'ES' : 8,
	# 	'GO' : 9,
	# 	'MA' : 10,
	# 	'MT' : 11,
	# 	'MS' : 12,
	# 	'MG' : 13,
	# 	'PA' : 14,
	# 	'PB' : 15,
	# 	'PR' : 16,
	# 	'PE' : 17,
	# 	'PI' : 18,
	# 	'RJ' : 19,
	# 	'RN' : 20,
	# 	'RS' : 21,
	# 	'RO' : 22,
	# 	'RR' : 23,
	# 	'SC' : 24,
	# 	'SP' : 25,
	# 	'SE' : 26,
	# 	'TO' : 27
	# }

	# print states['SE']

#start process
if __name__ == '__main__':
	main()