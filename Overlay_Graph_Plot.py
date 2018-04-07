
#Importing Necessary Models
import numpy as np
import matplotlib.pyplot as plt
import FiletoClass as Ftc
import sigmoidGraphFit as Sgf

def graphfunction(nameofthegraph):
	'''  Graph function takes one argument that is the label of the graph. 
	1.0. The function asks for the name of the file holding the data in CSV format.
	1.1. Data is loaded using FiletoClass module which return an object with required data.
	1.2. The data is then plotted on the graph.
	1.3. The data is used to fit sigmoid curve using sigmoidgraphfit module
	1.4. The sigmoid curve fit reutrn a class object with x,y values of curve and PSE values.
	1.5. The sigmoid fit is plotted in the graph along with the previous scatter data.
	1.6. The values are printed along with a directional arrow.'''

	print("Enter the name of the file containing data in csv format: ")
	filename_input = raw_input()
	data_from_file = Ftc.fileopen(filename=filename_input)



	#Plotting Actual Data
	plt.plot(data_from_file.actual_gain,data_from_file.mean_probability,'o',label=nameofthegraph,color="blue",alpha=0.75)


	#Fit the curve using sigmoidgraphfit and get return values 
	Sigmoid_graph_results = Sgf.fitsigmoidcurve(data_from_file.actual_gain,data_from_file.mean_probability)

	#Plotting Sigmoid Fit
	plt.plot(Sigmoid_graph_results.x,Sigmoid_graph_results.y,label="Sigmoid Fit",color="blue",linewidth=2.5)

	# Printing the PSE values and Plotting the Refrence Lines
	print (Sigmoid_graph_results.values)
	plt.plot([0.4,Sigmoid_graph_results.values[0]],[25,25],'b--',linewidth=2.0,alpha=0.9)
	plt.plot([Sigmoid_graph_results.values[0],Sigmoid_graph_results.values[0]],[0,25],'b--',linewidth=2.0,alpha=0.9)
	plt.plot([0.4,Sigmoid_graph_results.values[2]],[75,75],'b--',linewidth=2.0,alpha=0.9)
	plt.plot([Sigmoid_graph_results.values[2],Sigmoid_graph_results.values[2]],[0,75],'b--',linewidth=2.0,alpha=0.9)



	#Printing the values of 25 and 75 Values in graph that helps comparision

	valuetext = str('%.3f'% Sigmoid_graph_results.values[2])+ "                         " + str('%.3f'% Sigmoid_graph_results.values[0])

	plt.annotate("",xy=(Sigmoid_graph_results.values[2], 3),xytext=(Sigmoid_graph_results.values[0], 3),arrowprops=dict(arrowstyle="<->",connectionstyle="arc3",color="blue",linewidth=2.5),fontsize=10,)

	return; 

#Overlaying two graphs on top of each to facilitate comparision
graphfunction(nameofthegraph= 'Referenced')
graphfunction(nameofthegraph= 'Unreferenced')


'''Formatting the graph defining axis labels title of the graph and grids'''

#Plotting Legends
plt.legend(loc='upper right',scatterpoints=1,numpoints=1,ncol=2,fontsize=15)


#Plotting X label, Y label and Title of Graph
plt.ylabel('Probability of < responses', fontsize=15)
plt.xlabel('Value of applied Gain', fontsize=15)
plt.grid(color='b', linestyle='--',linewidth=1,alpha=0.25)

#Title of the Graph
plt.title("Comparision of Rotational gain threshold for Referenced and Unreferenced environment",fontsize=15)
ax = plt.subplot()
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='1', color='black',alpha=0.75)

# Customize the minor grid
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='red',alpha=0.5)
ax.tick_params(which='both', # Options for both major and minor ticks
                top='off', # turn off top ticks
                left='off', # turn off left ticks
                right='off',  # turn off right ticks
                bottom='off') # turn off bottom ticks
ax.set_axisbelow(True)


#Show the plot
plt.show()

