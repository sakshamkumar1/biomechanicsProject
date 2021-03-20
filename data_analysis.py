# Python code to plot the graphs of speed vs time and acceleration vs time
# The graphs help us in knowing the speeds and accelerations at different instants.

# First, importing the necessary packages for our program.
import math
import matplotlib.pyplot as plt 
import os
import numpy as np
from scipy import integrate
from scipy.optimize import curve_fit

# This code takes input from a text file named <data.txt> for the coordinates at different time.
# This command checks if the file data.txt> is present in the directory.
exists = os.path.isfile("data.txt")

if exists:
	# Creating empty arrays for storing x, y and z coordinates and corresponding time.
	x_coordinate = []
	y_coordinate = []
	z_coordinate = []
	time = []

	# variable for counting the line number
	line_count = 1

	# Going line by line in the file and extracting different values
	for line in open("data.txt"):
		time.append(float(line.split("	")[0]))
		x_coordinate.append(float(line.split("	")[1]))
		y_coordinate.append(float(line.split("	")[2]))
		z_coordinate.append(float(line.split("	")[3]))

		line_count += 1

	# Now that we have the coordinates, we calculate speeds and accelerations at different instants.
	# Creating empty arrays for storing speeds and corresponding time.
	speed = []
	time2 = []

	# Since the time interval is small, we can calculate speed as change in coordinate by time interval.
	for j in range(0, len(time)-1):
		time2.append(time[j])
		current_speed = (pow((pow((x_coordinate[j+1] - x_coordinate[j]),2) + pow((y_coordinate[j+1] - y_coordinate[j]),2) + pow((z_coordinate[j+1] - z_coordinate[j]),2)),0.5))/(time[j+1] - time[j])
		speed.append(current_speed)

	# Now that we have discreet points for speeds at different instants, we need to do curve-fitting.
	# The curve fitting will help us in obtaining the expression of speed as a function of time.
	# Defining a function for speed as a function of time.  
	def func(t,a,b,c,d,e):
		return a*pow(t,4) + b*pow(t,3) + c*pow(t,2) + d*t + e

	# Calculating different coefficients a, b, c, d and and e using curve fitting.
	popt, pcov = curve_fit(func,time2,speed)
	# We get our curve-fitted function of speed as a function of time.
	fit_cp = func(np.array(time2),*popt)

	# Now, we plot the graph of speed vs time.
	plt.plot(time2, fit_cp, color = "red", linewidth = 3)
	plt.xlabel("Time (in seconds)")
	plt.ylabel("Speed (in m/s)")
	plt.ylim([-3,3])
	plt.show()

	# Just like what we did for speed, we will do similar things for getting acceleration.
	# Creating empty arrays for storing acceleration and corresponding time.
	acceleration = []
	time3 = []

	# Calculating accelerations at different time instants.
	for k in range(0, len(speed)-1):
		time3.append(time[k])
		current_acceleration = (speed[k+1] - speed[k])/(time[k+1] - time[k])
		acceleration.append(current_acceleration)

	# Now, doing curve fitting.
	# Extracting the different coefficients - a, b, c, d and e.
	popt2, pcov2 = curve_fit(func,time3,acceleration)
	# We plug the obtained coeeficients to the curve fitting function.
	# We obtain the expression of acceleration as a function of time.
	fit_cp2 = func(np.array(time3),*popt2)

	# Finally, we plot the graphs of acceleration vs time.
	plt.plot(time3, fit_cp2, color = "green", linewidth = 3)
	plt.xlabel("Time (in seconds)")
	plt.ylabel("Acceleration (in m/s²)")
	plt.ylim([-10,10])
	plt.show()

# The above code was all for the case if the file <data.txt> exists.
# We need to take of the case if no such file exists.
# This ensures that our code will exit peacefully rather than displaying errors.

else:
	print("The file containing the required data, data.txt does not exist.")
	print("Please provide that file with the same name in the directory of this code.")