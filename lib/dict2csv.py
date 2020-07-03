def dict2csv(path,dict_data,comma_handler=True):
	with open(path,'w') as csv_out:
		for key,value in dict_data.items():
			if comma_handler==True:
				if ',' in key:
					key='"'+key+'"'
				if ',' in str(value):
					value='"'+str(value)+'"'
			csv_out.write(key+','+str(value))
			csv_out.write('\n')


if __name__=='__main__':
	dict_data={
		'Key':'Value',
		'Name':'Test',
		'Number':25,
		'Job, Position':'Teacher, Homeroom Teacher'
	}
	
	import os
	path=os.path.join(os.getcwd(),'data\\example_csv.csv')
	dict2csv(path,dict_data)