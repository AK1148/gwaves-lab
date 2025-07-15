import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#this will track how fast orbital velocty changes over time, so just dv/dt in eq.

'''
 def F(v):
    return (32/5) * (mu / m)**2 * v**10  # energy flux

def E_prime(v):
    return -mu * v      # derivative of binding energy

def dvdt(v, t):
    return -F(v) / E_prime(v)      # ode: change of velocity
'''

#model how fast energy changes with velocity and it uses flux

# constants
m1 = m2 = 5               # assumed solar mass
m = m1 + m2
mu = m1 * m2 / m      #reduced mass formula (bc spinning black holes)

# functions defined. F(v) is energy flux, E_prime(v) is derivative of binding energy.
def F(v):
    return (32 / 5) * (mu / m)**2 * v**10

def E_prime(v):
    return -mu * v

def dvdt(v, t):   #change in velocity as ODE
    return -F(v) / E_prime(v)

# initial conditions
v0 = 0.3
t = np.linspace(0, 100, 1000)

# solve ODE
v = odeint(dvdt, v0, t).flatten()

# plot figure (should be linear relationship)
plt.plot(t, v)
plt.title("Part 1: Velocity evolution v(t)")
plt.xlabel("Time")
plt.ylabel("Velocity v")
plt.grid()
plt.show()

#should simulate the velocity decay of inspiralling black holes using eq. check plot (figure1)