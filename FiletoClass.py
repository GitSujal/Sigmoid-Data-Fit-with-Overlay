# -*- coding: utf-8 -*-
import numpy as np

class dataholder:
	#A class to hold data read from the file.
	def __init__ (self, data):
		self.actual_gain = data[:,0] #taking out actual gain from data at column 1
		self.mean_probability = data[:,1] #Taking out mean from the data at column 2 




def fileopen (filename):
	# Function to read the data from the file using numpy genfrom text function
	try:
		data_from_file = np.genfromtxt (filename, delimiter=",")
		print("Reading Successful",filename)
		return dataholder(data_from_file);

	except:
		print("Error!! Filename not found.")
		return;


		