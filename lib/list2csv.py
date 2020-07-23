def list2csv(path,list_data,sep=',',sep_handler=True):
    '''list2csv
    Convert list (also accept other iterable) into csv.
    '''
    with open(path,'w') as csv_out:
        for row in list_data:
            for col,val in enumerate(row):
                if col != 0:
                    csv_out.write(sep)
                if sep_handler==True:
                    try:
                        if sep in val:
                            val='"'+val+'"'
                    except:
                        pass
                csv_out.write(str(val))
            csv_out.write('\n')

if __name__=='__main__':
    list_data=[
        [1,2],
        ['3',4.0],
        ['5.5','a']
    ]
    
    import os
    path=os.path.join(os.getcwd(),'data\\example_list.csv')
    list2csv(path,list_data)