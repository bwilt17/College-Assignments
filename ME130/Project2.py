import numpy as np
from scipy.integrate import odeint
import matplotlib
import matplotlib.pyplot as plt

#user inputs
m = float(input("Input mass value in kg:"))
k = float(input("Input spring constant in N/m:"))
B = float(input("Input damping coefficient in kg/s:"))
F0 = float(input("Input amplitude of force function in N:"))
w0 = float(input("Input frequency of force function in rad/s:"))
x0 = float(input("Input initial location in m:"))
v0 = float(input("Input initial speed in m/s:"))
tstop = int(input("Input time range for plot in s:"))

#defines t value range for calculation/plotting
t = np.linspace(0, tstop, 200)

#initial conditions
init = [x0,v0]

#natural frequency
w = np.sqrt(k/m) 

#turns second order ode for system into two first order odes to be solved by odeint
def f(i, t):
    return (i[1], (F0*np.sin(w0*t)-B*i[1]-k*i[0])/m)

#solves ODE
x = odeint(f,init,t)  

loc = x[:,0] 
vel = x[:,1]

#plotting/formatting
plt.plot(t,loc)
plt.plot(t,vel)
plt.title("Mass-Spring System")
plt.xlabel("time, t (s)")
plt.legend(["location, x(t) (m)", "velocity, x'(t) (m/s)"])

plt.grid()
plt.show()
