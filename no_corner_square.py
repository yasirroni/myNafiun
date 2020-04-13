def no_corner_square(number_of_x):
    if number_of_x > 0:
        print(f' {"x"*number_of_x} ')
        for _ in range(number_of_x):
            print(f'x{" "*number_of_x}x')
        print(f' {"x"*number_of_x} ')
    else:
        print('Please insert a valid number')

if __name__=='__main__':
    no_corner_square(5)