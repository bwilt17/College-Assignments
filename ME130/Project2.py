''' Simulation of Mass-Spring System with user inputs and plot output. Made for course project at SJSU in SP21. '''
''' Written by Beverly Wilt (beverly.wilt@sjsu.edu) '''

import numpy as np
from scipy.integrate import odeint
import matplotlib
import matplotlib.pyplot as plt

#user inputs
m = float(input("Input mass value (m) in kg:"))
k = float(input("Input spring constant (k) in N/m:"))
B = float(input("Input damping coefficient (B) in kg/s:"))
F0 = float(input("Input amplitude of force function (F0) in N:"))
w0 = float(input("Input frequency of force function (w0) in rad/s:"))
x0 = float(input("Input initial position in m:"))
v0 = float(input("Input initial speed in m/s:"))
tstop = int(input("Input time range for plot in s:"))

#defines t value range for calculation/plotting
t = np.linspace(0, tstop, 200)

#initial conditions
init = [x0,v0]

#natural frequency
w = np.sqrt(k/m) 

#turns second order ode into first order ode system to be solved by odeint
def f(i, t):
    return (i[1], (F0*np.sin(w0*t)-B*i[1]-k*i[0])/m)

#solves ODE
x = odeint(f,init,t)  

loc = x[:,1] 
vel = x[:,0]

#plotting/formatting
plt.plot(t,loc)
plt.plot(t,vel)
plt.title("Mass-Spring System")
plt.xlabel("time, t (s)")
plt.legend(["location, x(t) (m)", "velocity, x'(t) (m/s)"])

plt.grid()
plt.show()
