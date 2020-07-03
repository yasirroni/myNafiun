import numpy as np
import string
import pandas as pd
def text_mining(path,white_list=None,black_list=None,remove_punctuation=False,lower_case=False,encoding='utf-8'):
	'''Manual
	white_list			: None or str containing white list
	black_list			: None or str containing black list
	remove_punctuation	: remove punctuation listed in string.punctuation and predefined black list
	lower_case			: If True, convert text to lower_case
	encoding			: default is utf-8
	'''
	if black_list == None:
		black_list = ''

	if remove_punctuation == True:
		punctuation=string.punctuation
		black_list = black_list+punctuation

	def _remove(input_string):
		input_string=input_string.translate(str.maketrans('', '', black_list))
		return(input_string)

	def _lower_case(input_string):
		input_string=input_string.lower()
		return(input_string)

	def _dict(text,dict_result):
		if text in dict_result:
			dict_result[text]=dict_result[text]+1
		else:
			dict_result[text]=1

	dict_result={}
	with open(path,encoding=encoding) as txt_in:
		if white_list == None:
			#black_list_method
			for line in txt_in:
				line=_remove(line)
				if lower_case==True:
					line=_lower_case(line)
				for text in line.split():
					_dict(text,dict_result)
		else:		
			#white_list_method
			for line in txt_in:
				if lower_case==True:
					line=_lower_case(line)
				text=''
				for char in line:
					if char == ' ':
						_dict(text,dict_result)
						text=''
					if char in white_list:
						text=text+char
				_dict(text,dict_result)	
					
	#cleaning
	if '' in dict_result: del dict_result['']
	return dict_result
	
if __name__=='__main__':
	import os
	path=os.path.join(os.getcwd(),'data\\poems_by_choiril_anwar.txt')

	black_list='‘’' + '…' +'â€˜' + 'â€™'
	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_normal.csv')
	result_raw=text_mining(path,remove_punctuation=True,black_list=black_list)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_raw.items():
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_raw)

	black_list='‘’' + '…' +'â€˜' + 'â€™'
	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_lower_case.csv')
	result_lower_case=text_mining(path,remove_punctuation=True,lower_case=True,black_list=black_list)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_lower_case.items():
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_lower_case)

	white_list=string.ascii_letters+string.digits
	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_white_list_methode.csv')
	result_lower_case=text_mining(path,remove_punctuation=True,lower_case=True,white_list=white_list)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_lower_case.items():
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_lower_case)
