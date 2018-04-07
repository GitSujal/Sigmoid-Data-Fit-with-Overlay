# Python Program to fit sigmoid graph to the given points in X-Y co-ordinates
import numpy as np 
import pylab
from scipy.optimize import curve_fit

# def sigmoid(x, x0, b,a):
# 	y = 1/ (1 + a*np.exp(b*(x-x0)))
#     return y
# 	''' Defining a sigmoid graph using mathematical equation. 
# 	A sigmoid graph is a S-shaped curve and we will be using only a part of sigmoid curve to fit our data.'''

def sigmoid(x,x0,b,a):
	y = 1/(1 + a*np.exp(b*(x-x0)) )
	return y;

class returnvalues:
	def __init__(self, x,y,values):
		self.x = x
		self.y = y
		self.values = values


def fitsigmoidcurve (actual_gain, mean_probability,sigmoidfunction= 'sigmoid'):
	popt, pcov = curve_fit(sigmoid, actual_gain, mean_probability)
	x = np.linspace(0.4,1.6 ,5000)
	y = sigmoid(x, *popt)
	a = popt[2]
	b = popt[1]
	x0 = popt[0]

	#Calculating different xvalues corresponding to 25, 50 and 75 on y-scale
	xvalue = x0-(np.log(a))/b;
	x25value = x0-(np.log(a/3))/b;
	x75value = x0-(np.log(3*a))/b;

	#Printing the equation and values
	print("The required equation first is ",popt)
	print("PSE = " ,xvalue)

	#Formatting values for return 
	Values = [x25value, xvalue, x75value]
	return returnvalues(x,y,Values)