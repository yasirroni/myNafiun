import pandas as pd

def dict2csv(path,dictData):
	df=pd.DataFrame.from_dict(dictData, orient='index')
	df.to_csv(path,header=False)

if __name__=="__main__":
	import os
	dictData={
		'Key':'Value',
		'Name':'Test',
		'Number':25
	}
	if not os.path.isdir('data'):
		os.mkdir('data')
	path=os.path.join(os.getcwd(),'data\\example_csv.csv')
	dict2csv(path,dictData)