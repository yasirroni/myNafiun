import pandas as pd

def pd_dict2csv(path,dict_data):
	df=pd.DataFrame.from_dict(dict_data, orient='index')
	df.to_csv(path,header=False)

if __name__=="__main__":
	import os
	dict_data={
		'Key':'Value',
		'Name':'Test',
		'Number':25
	}
	if not os.path.isdir('data'):
		os.mkdir('data')
	path=os.path.join(os.getcwd(),'data\\example_csv.csv')
	pd_dict2csv(path,dict_data)