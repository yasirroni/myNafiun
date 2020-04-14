import pandas as pd
import os

def csv2dict(path,column_as_key,column_as_value):
	df=pd.read_csv(path,header=None)
	df=df.set_index([column_as_key])
	result_dic=df.loc[:,column_as_value].to_dict()
	return result_dic

if __name__=="__main__":
	path=os.path.join(os.getcwd(),'example_csv.csv')
	column_as_key=0
	column_as_value=1
	dictData=csv2dict(path,column_as_key,column_as_value)
	print(dictData)