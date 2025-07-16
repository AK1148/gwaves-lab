# Gravitational waveforms numerical simulation using post-Newtonian approximation equations, scipy odeint for binary black hole system (AK B'lore July 2025)

## A simple exercise in modelling the inspiral of two compact objects i.e. black holes as they approach each other. 
It's a scientific programming demonstration of essentially what interferometers like LIGO and VIRGO do when the detect gravitational waves (ripples in spacetime). Each black hole has original masses m1= m2 of 5 solar masses, initial velocity 0.2c (changed from initial 0.3c because it was too quick), initial orbital phase 0. Then used equations to compute:

1. velocity evolution due to loss in gravitational wave energy
2. orbital phase evolution
3. gravitational wave polarization signal generation h+ (vertical, horizontal) and hx (diagonal)
4. challenge- using adaptive-stepping ODE solvers to increase accuracy of results (adaptive Runge-Kutta DOPRI or Dormand-Prince method)

figures created with matplotlib: test graph, velocity, plus/cross polarization, adaptive (you should see them uploaded)

*LOOK AT FIG 4* it's BEAUTIFUL and actually quite accurate (cosine, sine waves out of phase, amplitude gradually grows larger until merger is completed. What happens after is beyond the scope of this project). The whole merger, if you check fig 4 (GW Polarizations subplot) happens in about 2.27 seconds.

important note: I started by setting up a virtual environment (venv) in VS Code, then did pip install for numpy, scipy, matplotlib for THAt specific environment. it was a headache (also I'm an amateur) so should use anaconda. still, it's a short project and the latex file probably took longer to make

I referred to https://arxiv.org/abs/0712.0343 and scipy lib

:D
