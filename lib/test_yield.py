def test_yield(inp):
    for x in inp:
        if x < 10:
            yield x*x
        else:
            yield x+x

def opener(generator):
    for val in generator:
        print(val)
inp=[2,4,6,8,10,12]
result=test_yield(inp)
print(result)
print(result)

print('before open')
opener(result)
print('after open')
opener(result)
for i in result:
    print(i)
print(result)
# for i in result:
#     print(i)