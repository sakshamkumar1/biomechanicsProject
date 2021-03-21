# Python code to plot the graphs of speed vs time and acceleration vs time of the centre of mass (COM) of thigh.
# The graphs help us in knowing the speeds and accelerations at different instants.

# First, importing the necessary packages for our program.
import math
import matplotlib.pyplot as plt 
import os
import numpy as np
from scipy import integrate
from scipy.optimize import curve_fit

# This code takes input from a text file named <data2.txt> for the coordinates of the two body markers at different time instants.
# This command checks if the file data2.txt> is present in the directory.
exists = os.path.isfile("data2.txt")

if exists:
	# Creating empty arrays for storing x, y and z coordinates and corresponding time.
	# We know the coordinates of body markers 3 and 7 which we'll use to calculate the parameters for COM of the thigh.
	x_coordinate_marker3 = []
	y_coordinate_marker3 = []
	z_coordinate_marker3 = []

	x_coordinate_marker7 = []
	y_coordinate_marker7 = []
	z_coordinate_marker7 = []
	
	time = []

	# variable for counting the line number
	line_count = 1

	# Going line by line in the file and extracting different values
	for line in open("data2.txt"):
		time.append(float(line.split("	")[0]))
		x_coordinate_marker3.append(float(line.split("	")[1]))
		y_coordinate_marker3.append(float(line.split("	")[2]))
		z_coordinate_marker3.append(float(line.split("	")[3]))

		x_coordinate_marker7.append(float(line.split("	")[4]))
		y_coordinate_marker7.append(float(line.split("	")[5]))
		z_coordinate_marker7.append(float(line.split("	")[6]))

		line_count += 1

	# Now that we have the coordinates of the markers, we calculate speeds and accelerations of COM at different instants.
	# Creating empty arrays for storing speeds and corresponding time of the COM.
	xSpeedCOM = []
	ySpeedCOM = []
	zSpeedCOM = []
	time2 = []
	# This is the speed of the COM of thigh which we are interested in.
	speed = []


	# Since the time interval is small, we can calculate speed as change in coordinate by time interval.
	for j in range(0, len(time)-1):
		time2.append(time[j])
		# current_speed = (pow((pow((x_coordinate_marker3[j+1] - x_coordinate_marker3[j]),2) + pow((y_coordinate_marker3[j+1] - y_coordinate_marker3[j]),2) + pow((z_coordinate_marker3[j+1] - z_coordinate_marker3[j]),2)),0.5))/(time[j+1] - time[j])
		x_speed_marker3 = (x_coordinate_marker3[j+1] - x_coordinate_marker3[j])/(time[j+1] - time[j])
		y_speed_marker3 = (y_coordinate_marker3[j+1] - y_coordinate_marker3[j])/(time[j+1] - time[j])
		z_speed_marker3 = (z_coordinate_marker3[j+1] - z_coordinate_marker3[j])/(time[j+1] - time[j])

		x_speed_marker7 = (x_coordinate_marker7[j+1] - x_coordinate_marker7[j])/(time[j+1] - time[j])
		y_speed_marker7 = (y_coordinate_marker7[j+1] - y_coordinate_marker7[j])/(time[j+1] - time[j])
		z_speed_marker7 = (z_coordinate_marker7[j+1] - z_coordinate_marker7[j])/(time[j+1] - time[j])		

		# Utilising the table of anthropometric data to calculate the x, y and z components of speeds of the COM
		x_speed_COM = x_speed_marker3 + 0.433 * (x_speed_marker7 - x_speed_marker3)
		y_speed_COM = y_speed_marker3 + 0.433 * (y_speed_marker7 - y_speed_marker3)
		z_speed_COM = z_speed_marker3 + 0.433 * (z_speed_marker7 - z_speed_marker3)

		xSpeedCOM.append(x_speed_COM)
		ySpeedCOM.append(y_speed_COM)
		zSpeedCOM.append(z_speed_COM)
		
		# Now, we get the net magnitude of speed.
		speed_COM = pow((pow(x_speed_COM, 2) + pow(y_speed_COM, 2) + pow(z_speed_COM, 2)), 0.5)
		speed.append(speed_COM)

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
	plt.ylim([0,2])
	plt.show()

	# Just like what we did for speed, we will do similar things for getting acceleration.
	# Creating empty arrays for storing acceleration and corresponding time.
	# This is the acceleration of the COM of thigh which we are interested in.
	acceleration = []
	time3 = []

	# Calculating accelerations at different time instants.
	for k in range(0, len(speed)-1):
		acceleration.append((speed[k+1] - speed[k])/(time[k+1] - time[k]))
		time3.append(time[k])

	# Now, doing curve fitting.
	# Extracting the different coefficients - a, b, c, d and e.
	popt2, pcov2 = curve_fit(func,time3,acceleration)
	# We plug in the obtained coeeficients to the curve fitting function.
	# We obtain the expression of acceleration as a function of time.
	fit_cp2 = func(np.array(time3),*popt2)

	# Finally, we plot the graphs of acceleration vs time.
	plt.plot(time3, fit_cp2, color = "green", linewidth = 3)
	plt.xlabel("Time (in seconds)")
	plt.ylabel("Acceleration (in m/s²)")
	plt.ylim([-6, 6])
	plt.show()

# The above code was all for the case if the file <data2.txt> exists.
# We need to take care of the case if no such file exists.
# This ensures that our code will exit peacefully rather than displaying errors.

else:
	print("The file containing the required data, data2.txt does not exist.")
	print("Please provide that file with the same name in the directory of this code.")