import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np

# Function
def func_grow(x,g,n_0):
    return n_0*np.power(1+g,x)

if __name__=="__main__":
    # Data
    x_samp = np.array([1,2,3,4,5,6])
    y_samp = np.array([3,4,5,6,6,11]) 

    # Estimate
    w, _ = opt.curve_fit(func_grow, x_samp, y_samp)

    # Print
    print('Estimated Parameters', w)
    print('Growth rate: ',w[0])
    print('Initial value: ',w[1])

    # Model
    x_lin = np.linspace(0, x_samp.max(), 50) # a number line, 50 evenly spaced digits between 0 and max
    y_model = func_grow(x_lin, *w)

    # Plot
    plt.plot(x_samp, y_samp, "ko", label="Data")
    plt.plot(x_lin, y_model, "k--", label="Fit")
    plt.title("Least squares regression")
    plt.legend(loc="upper left")
    plt.show()

