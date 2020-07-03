import numpy as np
import string
import pandas as pd
def text_mining(path,remove_punctuation=False,lower_case=False):
	'''Bug
		There is bug if '‘' is used in the raw data of text. 
		Sadly, this symbols is pretty common in text title.
	'''
	def _remove_punctuation(input_string):
		input_string=input_string.translate(str.maketrans('', '', string.punctuation))
		return(input_string)

	def _lower_case(input_string):
		input_string=input_string.lower()
		return(input_string)

	#line_flat
	line_flat=[]
	with open(path) as txt_in:
		for line in txt_in:
			if remove_punctuation==True:
				line=_remove_punctuation(line)
			if lower_case==True:
				line=_lower_case(line)
			line_flat.extend(line.split())
		
	#dict_normal
	dict_normal={}
	for text in line_flat:
		if text in dict_normal:
			dict_normal[text]=dict_normal[text]+1
		else:
			dict_normal[text]=1
	return dict_normal
	
if __name__=='__main__':
	import os
	path=os.path.join(os.getcwd(),'data\\poems_by_choiril_anwar.txt')

	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_normal.csv')
	result_raw=text_mining(path,remove_punctuation=True)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_raw.items():
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_raw)

	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_lower_case.csv')
	result_lower_case=text_mining(path,remove_punctuation=True,lower_case=True)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_lower_case.items():
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_lower_case)