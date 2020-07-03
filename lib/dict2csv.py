def dict2csv(path,dict_data):
	with open(path,'w') as csv_out:
		for key,value in dict_data.items():
			csv_out.write(key+','+str(value))
			csv_out.write('\n')


if __name__=='__main__':
	dict_data={
		'Key':'Value',
		'Name':'Test',
		'Number':25
	}
	
	import os
	path=os.path.join(os.getcwd(),'data\\example_csv.csv')
	dict2csv(path,dict_data)