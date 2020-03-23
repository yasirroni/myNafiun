import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np

# Data
x_samp = np.array([1,2,3,4,5,6])
y_samp = np.array([3,4,5,6,6,11]) 

# initialGuess
initialGuess=[1000,0.29,15] #0.29 from predictGrowth

# Function
def func_grow(x,L,k,x_0):
    return L/(1+np.exp(-k*(x-x_0)))

# Estimate
w, _ = opt.curve_fit(func_grow, x_samp, y_samp,p0=initialGuess,maxfev=100000)     

# Print
print('Estimated Parameters: ', w)
print('Maximum value: ',w[0])
print('Growth rate: ',w[1])
print('Mid Point: ',w[2])

# Model
x_lin = np.linspace(0, x_samp.max(), 50) # a number line, 50 evenly spaced digits between 0 and max
y_model = func_grow(x_lin, *w)

# Plot
plt.plot(x_samp, y_samp, "ko", label="Data")
plt.plot(x_lin, y_model, "k--", label="Fit")
plt.title("Least squares regression")
plt.legend(loc="upper left")
plt.show()