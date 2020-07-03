import pandas as pd

def pd_csv2dict(path,column_as_key,column_as_value):
	df=pd.read_csv(path,header=None)
	df=df.set_index([column_as_key])
	result_dic=df.loc[:,column_as_value].to_dict()
	return result_dic

if __name__=="__main__":
	import os
	path=os.path.join(os.getcwd(),'data\\example_csv.csv')
	column_as_key=0
	column_as_value=1
	dict_data=pd_csv2dict(path,column_as_key,column_as_value)
	print(dict_data)