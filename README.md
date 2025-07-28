# Gravitational waveforms numerical simulation using post-Newtonian approximation equations, scipy odeint for binary black hole system (July 2025)

## A simple exercise in modelling the inspiral of two compact objects i.e. black holes as they approach each other. 
It's a scientific programming demonstration of essentially what interferometers like LIGO and VIRGO do when the detect gravitational waves (ripples in spacetime). Each black hole has original masses m1= m2 of 5 solar masses, initial velocity 0.2c (v; changed from initial 0.3c because it was too slow), initial orbital phase (phi) 0. Then used equations to compute:

1. velocity evolution due to loss in gravitational wave energy
2. orbital phase evolution
3. gravitational wave polarization signal generation h+ (vertical, horizontal) and hx (diagonal)
4. challenge- using adaptive-stepping ODE solvers to increase accuracy of results (adaptive Runge-Kutta DOPRI or Dormand-Prince method)

figures created with matplotlib: test graph, velocity, plus/cross polarization, adaptive dopri5(you should see them uploaded). after making some improvements, fig4 and fig5 have both velocity evolution and gw polarization in one image after I started using subplots in part2.py

*Fig 4* is quite theoretically accurate (cosine, sine waves out of phase, amplitude gradually grows larger until merger is completed. What happens after is beyond the scope of this project). The whole merger, if you check fig 4 (GW Polarizations subplot) happens in about 2.27 seconds. Later, after modifications, it came to be 1.5 s.

<ins>important note:</ins> I started by setting up a virtual environment (venv) in VS Code, then did a pip install for numpy, scipy, matplotlib for THAt specific environment

<ins>important note 2:</ins> the GW polarization plot initially had some arbitrary dimensionless values for time that weren't really relevant (so assumed G=1, c=1, which is of course not true). After consulting some sources, realized this was due to a "hidden factor" in mass. This hidden factor, found to be GM/c^3 with some algebra + dimensional analysis, is known as the gravitational time unit. After accounting for this, I ended up with tangible physical time (with range 3s)

This is why FIG1, FIG2, FIG3 aren't great. They show only the process. they only range minutely from 0-100 of some dimensionless time. this issue was fixed in FIG4

*CURRENT ISSUE:* For the adaptive runge-kutta implementation, I get a warning saying that dopri5 step size is too small. I've tried a lot of values and it doesn't seem to generate a good graph. Any tips are welcome, and I will be working on refining it

<ins>important note 3:</ins> if running the code results in two weird-looking lines or empty space, make sure to increase the range. if you don't convert time, this will be 1e6 or 5e5 (otherwise 3-5s). Once you do this, you should see something like fig4. 

Playing around with the parameters (e.g. 10 solar mass, initial speed etc) can be really informative. *part2 is the main file*

I referred to https://arxiv.org/abs/0712.0343 and scipy lib
