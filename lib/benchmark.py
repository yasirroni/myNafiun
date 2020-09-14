import time
import random
import statistics

def benchmark(functions, iteration, *args):
    times = {f.__name__: [] for f in functions}
    
    for i in range(iteration):
        func = random.choice(functions)
        t0 = time.perf_counter()
        func(*args)
        t1 = time.perf_counter()
        times[func.__name__].append(t1 - t0)
    
    for name, numbers in times.items():
        print('FUNCTION:', name, 'Used', len(numbers), 'times')
        print('\tMEDIAN', statistics.median(numbers))
        print('\tMEAN  ', statistics.mean(numbers))
        print('\tSTDEV ', statistics.stdev(numbers))

if __name__=="__main__":
    # Variables
    divident = 12345600000
    n = 3
    iteration = 1000000

    # The functions to compare
    def f_int(divident,n):
        return int(divident/(10 ** n))

    def f_str_to_int(divident,n):
        return int(str(divident)[:-n])

    functions = f_int, f_str_to_int
    benchmark(functions, iteration, divident, n)