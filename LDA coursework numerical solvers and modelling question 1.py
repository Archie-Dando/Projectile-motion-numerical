# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:27:58 2025

@author: archi
"""
#This file contains code to answer the 1st question from the coursework and to answer questions 2A, 2B and 2C
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':9}) #sets font size to allow more control of how the plot looks
def simulation(theta=60, dt = 0.01): #input variables for the model
    t = 0 #define initial time
    v = 10 #define initial speed of projectile
    x0, y0 = 0.0, 0.0 #define starting coordinates of the projectile
    angle_rad = np.radians(theta) #conversion of angle of projection from degrees to radians
    a_x = 0 #acceleration in the x-direction, equal to 0 as there is no drag force in this model
    a_y = -9.81 #acceleration in the y-direction, equal to gravity in this model as drag is being ignored
    xpositions = [x0] #creating list to store the data for different variables from the model
    ypositions = [y0]
    time = [t]
    vx = v * np.cos(angle_rad) #calculation of initial speed in each direction
    vy = v * np.sin(angle_rad)
    vxs = [vx] #list to store the velocities in each direction
    vys = [vy]
    while ypositions[-1] >= 0: #creates a loop to stop the model once the projectile hits the ground
        xn = xpositions[-1] + vx * dt #calculates the new x-coordinate of the projectile
        yn = ypositions[-1] + vys[-1] * dt #calculates the new y-position of the projectile
        vxn = vxs[-1] #Calculation of  the new velocity of the projectile in each direction
        vyn = vys[-1] + a_y * dt
        xpositions.append(xn) #updates the new coordinates of the projectile
        ypositions.append(yn)
        time_n = time[-1] + dt #calculates the new time of the simulation
        time.append(time_n) #updates the time of the model
        vxs.append(vxn) #updates the velocity of the projectile in each direction
        vys.append(vyn)
    xpositions_array = np.array(xpositions) #converts the lists used to store variables into arrays so operations can be performed on them
    ypositions_array = np.array(ypositions)
    vxa = np.array(vxs)
    vya = np.array(vys)
    time_array = np.array(time)
    return xpositions_array, ypositions_array, vxa, vya, time_array #outputs variables calculated from the function
def plot_function(x=30, a=0.15, b=0.1, c=0.05, d=0.01): #creates a funciton to create a plot through a series of inputs
    fig, axs = plt.subplots(1, 3, figsize=(10,5)) #creates a figure and specifies the size
    theta_r = [x] #specifies a range of values for theta to be used as inputs for the function
    dt_r = [a, b, c, d] #specifies a range of time steps to be used in the function
    for theta in theta_r: #loops the range of theta_r values through the function
        for dt in dt_r: #loops the time steps through the function
            xpositions_array, ypositions_array, vxa, vya, time_array = simulation(theta=theta, dt=dt)
            if theta == x and dt == d: #specifies variables that can be added to a single plot for multiple input variables
                color = 'r'
                label = f"theta = {x} dt = {d}"
                marker = 'o'
            elif theta == x and dt == c:
                 color = 'b'
                 label = f"theta = {x} dt = {c}"
                 marker = 'v'
            elif theta == x and dt == b:
                 color = 'y'
                 label = f"theta = {x} dt = {b}"
                 marker = 's'
            elif theta == x and dt == a:
                 color = 'k'
                 label = f"theta = {x} dt = {a}"
                 marker = 'p'
            axs[0].scatter(time_array, ypositions_array, color=color, marker=marker, label=label) #specifies how to plot the data and where each data set is added to the overall figure
            axs[1].scatter(time_array, xpositions_array, color=color, marker=marker, label=label)
            axs[2].scatter(xpositions_array, ypositions_array, color=color, marker=marker, label=label)
    axs[0].set_xlabel('time (s)')
    axs[0].set_ylabel('height (m)')
    axs[0].set_title('change in height')
    axs[0].legend()
    axs[1].set_xlabel('time (s)')
    axs[1].set_ylabel('horizontal displacement (m)')
    axs[1].set_title('change in horizontal displacement')
    axs[1].legend()
    axs[2].set_xlabel('horizontal displacement (s)')
    axs[2].set_ylabel('height (m)')
    axs[2].set_title('change in position')
    axs[2].legend()
    fig.suptitle('data on projectile motion using the euler method')
    fig.tight_layout() #prevents overlap
    plt.show()
    
plot_function(x=30, a=0.15, b=0.1, c=0.05, d=0.01)