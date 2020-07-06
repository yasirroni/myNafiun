import numpy as np
import string
import pandas as pd
def text_mining(path,white_list=None,black_list=None,lower_case=False,remove_punctuation=False,encoding='utf-8',char_counting=False):
	'''Manual
	white_list			: None or str containing white list
	black_list			: None or str containing black list
	lower_case			: If True, convert text to lower_case
	remove_punctuation	: remove punctuation listed in string.punctuation and predefined black list
	encoding			: default is utf-8
	char_counting		: If True, count char instead of text
	'''
	def _remove(input_string,black_list):
		return(input_string.translate(str.maketrans('', '', black_list)))

	def _lower_case(input_string):
		return(input_string.lower())

	def _dict(key,dict_keys):
		if key in dict_keys:
			return dict_keys[key]+1
		else:
			return 1

	def _char_counting(txt_in,white_list=white_list,black_list=black_list,lower_case=lower_case):
		dict_result={}
		if white_list == None:
			#black_list_method
			for line in txt_in:
				line=_remove(input_string=line,black_list=black_list)
				if lower_case==True:
					line=_lower_case(line)
				for text in line.split():
					for char in text:
						dict_result[char]=_dict(char,dict_result)
		else:
			#white_list_method
			for line in txt_in:
				if lower_case==True:
					line=_lower_case(line)
				for text in line.split():
					for char in text:
						if char in white_list:
							dict_result[char]=_dict(char,dict_result)
		return dict_result

	def _text_mining(txt_in,white_list=white_list,black_list=black_list,lower_case=lower_case):
		dict_result={}
		if white_list == None:
			#black_list_method
			for line in txt_in:
				line=_remove(input_string=line,black_list=black_list)
				if lower_case==True:
					line=_lower_case(line)
				for text in line.split():
					dict_result[text]=_dict(text,dict_result)
		else:		
			#white_list_method
			for line in txt_in:
				if lower_case==True:
					line=_lower_case(line)
				for text in line.split():
					text_white=''
					for char in text:
						if char in white_list:
							text_white=text_white+char
					dict_result[char]=_dict(char,dict_result)
		return dict_result
	
	if black_list == None:
		black_list = ''

	if remove_punctuation == True:
		punctuation=string.punctuation
		black_list = black_list+punctuation
		
	with open(path,encoding=encoding) as txt_in:
		if char_counting == True:
			dict_result=_char_counting(txt_in,white_list=white_list,black_list=black_list,lower_case=lower_case)
		else:
			dict_result=_text_mining(txt_in,white_list=white_list,black_list=black_list,lower_case=lower_case)
	
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
			if ',' in key:
				key='"'+key+'"'
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	for k, v in result_raw.items():
		print("{:<10} {:<3}".format(k,v));
	# print(result_raw)

	black_list='‘’' + '…' +'â€˜' + 'â€™'
	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_lower_case.csv')
	result_lower_case=text_mining(path,remove_punctuation=True,lower_case=True,black_list=black_list)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_lower_case.items():
			if ',' in key:
				key='"'+key+'"'
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_lower_case)

	white_list=string.ascii_letters+string.digits+'_'
	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_white_list_method.csv')
	result_lower_case=text_mining(path,remove_punctuation=True,lower_case=True,white_list=white_list)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_lower_case.items():
			if ',' in key:
				key='"'+key+'"'
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_lower_case)

	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_char_counting.csv')
	result_lower_case=text_mining(path,char_counting=True)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_lower_case.items():
			if ',' in key:
				key='"'+key+'"'
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	print(result_lower_case)

	save_path=os.path.join(os.getcwd(),'data\\[RESULT]_text_minning_char_counting_lower_case.csv')
	result_lower_case=text_mining(path,lower_case=True,char_counting=True)
	with open(os.path.join(save_path),'w') as txt_out:
		for key,value in result_lower_case.items():
			if ',' in key:
				key='"'+key+'"'
			txt_out.write(key+','+str(value))
			txt_out.write('\n')
	for k, v in result_lower_case.items():
		print("{:<10} {:<3}".format(k,v));
	# print(result_lower_case)
