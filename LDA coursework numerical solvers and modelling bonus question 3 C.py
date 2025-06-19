# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:32:47 2025

@author: archi
"""
#This file contains code to answer the bonus question 3C from the coursework adding drag to the model
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12})
def drag(theta=90, dt = 0.01, r = 0.005, rho_f = 1.293, rho_s = 7700 ):
    t = 0 #define initial time
    v = 0 #initial speed
    rest = 0.8 #coefficient of restitution
    C_d = 0.8
    A = np.pi * r**2
    vol = 4/3 * np.pi * r**3
    m = vol * rho_s
    x0, y0 = 0.0, 0.0 #define initial position
    angle_rad = np.radians(theta) #converts the angle of projection from degrees to radians
    a_x = 0 #define acceleration of the projectile in each direction
    g = -9.81
    xpositions = [x0] #stores the variables in the list
    ypositions = [y0]
    time = [t]
    vx = v * np.cos(angle_rad) #calculates the initial velocity of the projectile in each direction
    vy = v * np.sin(angle_rad)
    vxs = [vx] #stores variables in a list
    vys = [vy]
    B = rho_f * abs(g) * vol
    D_i = 1/2 * rho_f * g * v**2 * C_d
    a_y = ((m*g)+B)/m
    a_ys = [a_y]
    while time[-1] <= 3: #creates a loop that ends the model once a specific amount of time has passed
        xn = xpositions[-1] + vxs[-1] * dt #calculates the new position of the projectile
        yn = ypositions[-1] + vys[-1] * dt
        vxn = vxs[-1]  #calculates the new velocity in each direction of the projectile
        vyn = vys[-1] + a_ys[-1] * dt
        D_n = 1/2 * rho_f * A * (vys[-1]**2) * C_d #calculates the new drag force that is acting on the projectile using the new veloctiy
        drag = -np.sign(vys[-1]) * D_n #ensures drag always opposes the direction of motion
        a_yn = ((m*g)+drag+B)/m #calculates the new acceleration of the projectile using the new drag force
        xpositions.append(xn) #updates the new position of the projectile
        ypositions.append(yn)
        time_n = time[-1] + dt #calculates the new time of the model
        time.append(time_n) #updates the time of the model
        vxs.append(vxn) #updates the velocity in each direction of the model
        vys.append(vyn)
        a_ys.append(a_yn)
        if a_ys[-1] == 0: #ends the loop once terminal velocity is achieved
            break
    xpositions_array = np.array(xpositions) #converts the lists used to store the variables into arrays
    ypositions_array = np.array(ypositions)
    vxa = np.array(vxs)
    vya = np.array(vys)
    time_array = np.array(time)
    ya_array = np.array(a_ys)
    max_location = np.argmax(np.abs(vya)) #finds the point in the array which contains the terminal velocity
    terminal_velocity = vya[max_location] #finds the value of the terminal velocity
    print(f"terminal velocity is {terminal_velocity} m/s")
    return xpositions_array, ypositions_array, vxa, vya, time_array, ya_array #outputs data calculated from the function
def plot_terminal(x=30, y = 2, c=0.05, b = 0.01):
    fig, axs = plt.subplots(1, 3, figsize=(10, 5)) #creates a figure and specifies the size
    rho_s1 = [y] #specifies a range of values for theta to be used as inputs for the function
    rho_f1 = [b, c] #specifies a range of time steps to be used in the function
    for rho_s in rho_s1: #loops the range of theta_r values through the function
        for rho_f in rho_f1: #loops the time steps through the function
            xpositions_array, ypositions_array, vxa, vya, time_array, ya_array = drag(rho_s = rho_s, rho_f = rho_f)
            if rho_s == y and rho_f == b: #specifies variables that can be added to a single plot for multiple input variables
                color = 'r'
                label = f"fluid density = {b}"
                marker = 'o'
            elif rho_s == y and rho_f == c:
                 marker = 's'
                 color = 'g'
                 label = f"fluid density = {c}"
            else:
                color = 'b'
                label = f"solid density = {rho_s} fluid density = {rho_f}"
                marker = 'x'
            axs[0].scatter(time_array, ypositions_array, color=color, marker=marker, label=label)
            axs[1].scatter(time_array, vya, color=color, marker=marker, label=label)
            axs[2].scatter(time_array, ya_array, color=color, marker=marker, label=label)
    axs[0].set_xlabel('time (s)')
    axs[0].set_ylabel('height (m)')
    axs[0].set_title('change in height')
    axs[0].legend()
    axs[1].set_xlabel('time (s)')
    axs[1].set_ylabel('velocity in the y-direction (m/s)')
    axs[1].set_title('vertical velocity ')
    axs[1].legend()
    axs[2].set_xlabel('time (s)')
    axs[2].set_ylabel('vertical accleration (m/s^2)')
    axs[2].set_title('vertical acceleration')
    axs[2].legend()
    fig.suptitle('motion of a nylon ball (1138.4 kg/m^3) dropped through water (998.24 kg/m^3) and glycerine (1261.3 kg/m^3)')
    fig.tight_layout()
    plt.show()
drag(theta=90, dt = 0.01, r = 0.05, rho_f = 1.293, rho_s = 7700 )
plot_terminal(y = 1138.4, b = 998.24, c = 1261.3)