def removeRow(inp,mode='all',lb=None,ub=None):
    '''
    Remove a row of list if condition meet.
    Default mode is all condition.

    Usage:
    arr=[
        [-3,-2,-1],
        [0,1,2],
        [3,4,5]
    ]
    result=removeRow(arr,lb=0,ub=2)
    '''
    if mode=='all':
        inp=removeRow_all(inp,lb,ub)
    elif mode=='any':
        inp=removeRow_any(inp,lb,ub)
    return inp

def removeRow_all(inp,lb=None,ub=None):
    maxIdx=len(inp)-1
    for idx,row in enumerate(reversed(inp)):
        if lb != None:
            if all(val<lb for val in row):
                del inp[maxIdx-idx]
        if ub != None:
            if all(val>ub for val in row):
                del inp[maxIdx-idx]
    return inp

def removeRow_any(inp,lb=None,ub=None):
    maxIdx=len(inp)-1
    for idx,row in enumerate(reversed(inp)):
        if lb != None:
            if any(val<lb for val in row):
                del inp[maxIdx-idx]
        if ub != None:
            if any(val>ub for val in row):
                del inp[maxIdx-idx]
    return inp