import icf
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import numpy as np
import math

xdata, ydata = icf.load_2col("Line1angle90stage11.csv")
xdata *= 60.0/1000.0

# This function will generate a perfect Gaussian 
# You can replace this function with any other you want to fit with...
def gaussian(x, *params):

	A = params[0]
	x0 = params[1]
	c = params[2]
	y0 = params[3]
    
	
	return y0-(A/2)*np.exp(-((x-x0)/math.sqrt(2)*c)**n)

guess = [1,1,1,1]

popt, pcov = curve_fit(gaussian, xdata, ydata, p0=guess)

for i in range(len(popt)):
	print ("Parameter",i,":",popt[i],"+/-",np.sqrt(pcov[i][i]))

yfit = gaussian(xdata, *popt)	

icf.fit_plot(xdata, ydata, yfit)

plt.show()

