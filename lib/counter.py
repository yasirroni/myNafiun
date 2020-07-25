def gen(inp,idx=0,lower=1,upper=10):
    if sum(inp) == len(inp) * upper:
        print('Upper Limit Reached: ',inp)
        return (inp)
    inp[idx] = inp[idx]+1
    if inp[idx] > upper:
        if idx < len (inp) - 1:
            inp[idx] = lower
            inp = gen(inp,idx=idx+1,lower=lower,upper=upper)
        else:
            inp[idx] = upper
            print('Upper Limit Reached: ',inp)
    return inp

if __name__=='__main__':
    print('BEFORE LOOP:')
    result = [1,1,1]
    print(result)
    print('LOOP BELOW:')
    while True:
        upper=4
        result = gen(result,upper=upper)
        print(result)
        if sum(result) -1 == len(result) * upper:
            break