import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#repeat from part 1 but now also with orbit phase. this is what ligo (etc interferometers) needs
#GW depends on two things. v(t) so speed already calculated and where the objects are so phi(t)
#so this gives the full orbital picture. it needs to be solved as a coupled ode
#plus polarization: gw's vertical/horizontal stretching
#cross polarization: gw's diagonal stretching

# constants
m1 = m2 = 5
m = m1 + m2
mu = m1 * m2 / m

# functions
def F(v):
    return (32 / 5) * (mu / m)**2 * v**10

def E_prime(v):
    return -mu * v

# Coupled system: y = [v, phi]
def system(y, t):
    v, phi = y
    dvdt = -F(v) / E_prime(v)
    dphidt = v**3 / m
    return [dvdt, dphidt]

# initial conditions
v0 = 0.3
phi0 = 0.0
y0 = [v0, phi0]
t = np.linspace(0, 100, 1000)

# solve
sol = odeint(system, y0, t)
v = sol[:, 0]
phi = sol[:, 1]

# now theyre plugged into the provided equations for strain i.e. gw polarizations
# gravitational wave polarizations
h_plus = 4 * (mu / m) * v**2 * np.cos(phi)
h_cross = 4 * (mu / m) * v**2 * np.sin(phi)

# plot h+ and h×
plt.plot(t, h_plus, label='h+', color='green')
plt.plot(t, h_cross, label='h×', color='red')
plt.title("Part 2: Gravitational Wave Polarizations")
plt.xlabel("Time")
plt.ylabel("Strain")
plt.legend()
plt.grid()
plt.show()

#check plot (figure2)

