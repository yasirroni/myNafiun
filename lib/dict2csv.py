import pandas as pd
import os

def dict2csv(path,dictData):
	df=pd.DataFrame.from_dict(dictData, orient='index')
	df.to_csv(path,header=False)

if __name__=="__main__":
	dictData={
		'Key':'Value',
		'Name':'Test',
		'Number':25
	}
	path=os.path.join(os.getcwd(),'example_csv.csv')
	dict2csv(path,dictData)