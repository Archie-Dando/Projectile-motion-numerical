# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:29:38 2025

@author: archi
"""
#This file contains code to answer bonus question 2D from the coursework using the velocity verlet method
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':9})
def verlet(theta=60, dt = 0.01): #creates a function and specifies inputs
    t = 0 #define initial time
    v = 10 #define initial speed
    x0, y0 = 0.0, 0.0 #define initial coordinates
    angle_rad = np.radians(theta) #conversion of the angle of projection from degrees to radians
    a_x = 0 #acceleration in the x direction
    a_y = -9.81 #acceleration in the y direction
    xpositions = [x0] #creates a list to store data for each variable
    ypositions = [y0]
    time = [t]
    vx = v * np.cos(angle_rad) #calculates the initial speed of the projectile in each direction
    vy = v * np.sin(angle_rad)
    vxs = [vx] #stores the speed of the projectile in each direction
    vys = [vy]
    while ypositions[-1] >= 0: #limits the model to when the projectile hits the ground
        xn = xpositions[-1] + vx * dt + 1/2 * a_x * dt**2 #calculates the new position of the projectile using the average velocity across the time step and the average acceleration across the timestep
        yn = ypositions[-1] + vys[-1] * dt + 1/2 * a_y * dt**2
        vxn = vxs[-1]  #calculates the new velocity of the projectile in each direction
        vyn = vys[-1] + a_y * dt
        xpositions.append(xn) #updates the postion of each variable in the model
        ypositions.append(yn)
        time_n = time[-1] + dt
        time.append(time_n)
        vxs.append(vxn)
        vys.append(vyn)
    xpositions_array = np.array(xpositions) #converts each list of data for the variables into arrays so operation can be performed
    ypositions_array = np.array(ypositions)
    vxa = np.array(vxs)
    vya = np.array(vys)
    time_array = np.array(time)
    return xpositions_array, ypositions_array, vxa, vya, time_array #returns data from the function
def plot_function_verlet(x=30, a=0.15, b=0.1, c=0.05, d=0.01): #creates a function and defines input variables
    fig, axs = plt.subplots(1, 3, figsize=(10, 5)) #creates a figure and specifies the size and dimensions of the subplots
    theta_r = [x] #specifies a range of values for theta to be used as inputs for the function
    dt_r = [a, b, c, d] #specifies a range of time steps to be used in the function
    for theta in theta_r: #loops the range of theta_r values through the function
        for dt in dt_r: #loops the time steps through the function
            xpositions_array, ypositions_array, vxa, vya, time_array = verlet(theta=theta, dt=dt)
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
            axs[0].scatter(time_array, ypositions_array, color=color, marker=marker, label=label) #plots three scatter graphs of the different variables against each other
            axs[1].scatter(time_array, xpositions_array, color=color, marker=marker, label=label)
            axs[2].scatter(xpositions_array, ypositions_array, color=color, marker=marker, label=label)
    axs[0].set_xlabel('time (s)') #creates the annotations for each individual subplot
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
    fig.suptitle('data on projectile motion using the euler method') #title for the whole figure
    fig.tight_layout() #prevents overlap between subplots
    plt.show()
plot_function_verlet(x=30, a=0.15, b=0.1, c=0.05, d=0.01)