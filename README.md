# Gravitational waveforms numerical simulation using post-Newtonian approximation equations, scipy odeint for binary black hole system (AK B'lore July 2025)

## A simple exercise in modelling the inspiral of two compact objects i.e. black holes as they approach each other. 
It's a scientific programming demonstration of essentially what interferometers like LIGO and VIRGO do when the detect gravitational waves (ripples in spacetime). Each black hole has original masses m1= m2 of 5 solar masses, initial velocity 0.2c (v; changed from initial 0.3c because it was too quick), initial orbital phase (phi) 0. Then used equations to compute:

1. velocity evolution due to loss in gravitational wave energy
2. orbital phase evolution
3. gravitational wave polarization signal generation h+ (vertical, horizontal) and hx (diagonal)
4. challenge- using adaptive-stepping ODE solvers to increase accuracy of results (adaptive Runge-Kutta DOPRI or Dormand-Prince method)

figures created with matplotlib: test graph, velocity, plus/cross polarization, adaptive (you should see them uploaded)

*LOOK AT FIG 4* it's beautiful and actually quite theoretically accurate (cosine, sine waves out of phase, amplitude gradually grows larger until merger is completed. What happens after is beyond the scope of this project). The whole merger, if you check fig 4 (GW Polarizations subplot) happens in about 2.27 seconds.

<ins>important note:</ins> I started by setting up a virtual environment (venv) in VS Code, then did pip install for numpy, scipy, matplotlib for THAt specific environment. it was a headache (also I'm an amateur) so should use anaconda. still, it's a short project and the latex file probably took longer to make

<ins>important note 2:</ins> the GW polarization plot initially had some arbitrary dimensionless values for time that weren't really relevant (so G=1, c=1, which is naturally not true). After consulting some sources, realized this was due to a "hidden factor" in mass. This hidden factor,found to be GM/c^3 with some algebra + dimensional analysis, is of course the gravitational time unit. After accounting for this, I ended up with tangible physical time (used range 3s)

THIS IS WHY FIG1, FIG2, FIG3 aren't useful. they only range minutely from 0-100 of some dimensionless time. this issue was fixed in FIG4

*CURRENT ISSUE:* For the adaptive runge-kutta implementation, I get a warning saying that dopri5 step size is too small. I've tried a lot of values and it doesn't seem to generate a good graph. Any tips are welcome

<ins>important note 3:</ins> if running the code results in two weird-looking lines or empty space, make sure to increase the range. if you don't convert time, this will be 1e6 or 5e5 (otherwise 3-5s). Once you do this, you should see something like fig4). 

Playing around with the parameters (e.g. 10 solar mass, initial speed etc) can be really informative. *part2 is the main file*

I referred to https://arxiv.org/abs/0712.0343 and scipy lib

:D
