import csv

def nestdict2csv(path,nestdict):
    with open(path, "w",newline='') as f:
        w = csv.writer(f)
        rows = list(nestdict.values())
        cols = rows[0].keys()
        w.writerow([''] + list(cols))
        for key in nestdict.keys():
            w.writerow([key] + [nestdict[key][col] for col in cols])


if __name__=='__main__':
	dict_data={
        'col_1':{
            'Key':'Value',
            'Name':'Test',
            'Number':25,
            'Job, Position':'Teacher, Homeroom Teacher'
        },
        'col_2':{
            'Key':'Value2',
            'Name':'Test2',
            'Number':26,
            'Job, Position':'Teacher, Homeroom Teacher'
        },
        'col_3':{
            'Key':'Value3',
            'Name':'Test3',
            'Number':27,
            'Job, Position':'Teacher, Homeroom Teacher'
        }
		
	}
	
	import os
	path=os.path.join(os.getcwd(),'data\\example_nestdict.csv')
	nestdict2csv(path,dict_data)