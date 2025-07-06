(fvm)=
# PDEs and the Finite Volume Method

% START-CREDIT
% source: finite_volume_method
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Robert Lanzafame and Jaime Arriaga Garcia. `{ref}`Find out more here <finite_volume_method_credit>`.
```
% END-CREDIT

The Finite Volume Method (FVM) is a numerical approach for solving partial differential equations (PDEs); it builds on many of the concepts covered by the Finite Difference Method (FDM), covered earlier in this textbook. The method evaluates a quantity of interest in space and time, $\phi(\mathbf{x},t)$, over a domain of interest, $\Omega$.  One main advantage of the finite volume method is that it is well-suited to flow-based problems (e.g., computational fluid dynamics), but it is also a relatively simple method that can be applied to a wide variety of physics-based conservation laws (e.g., mass, momentum and energy). 

The general scheme for FV problems is as follows:

1. Convert the PDE to integral formulation, over a volume of interest
2. Apply Gauss's Theorem on the bounding surface
3. Discretize domain into finite volumes and apply the integral equations (spatial discretization)
4. Apply a numerical scheme to discretize equations in time, then solve

These topics will be discussed in more detail after the discretizing of a general problem into finite volumes is introduced below.

**Why is FVM useful?**

One of the reasons FVM is useful is because it uses a Cartesian-based reference frame that stays fixed in time to describe the time-evolution of the quantity of interest at discretized locations within a domain. Taking fluid flow as an example, FVM can be thought of as a series of containers (the "volumes"), each of which tracks the amount of fluid entering and leaving (fluxes), as well as a number of other changes in time within the container, for example, velocity or pressure.

Other numerical modelling methods for solving PDEs (e.g., finite difference or finite element methods) are often formulated to track a quantity of interest with a reference point that moves in time, such as deformation of a solid. This type of approach is generally inconvenient for fluid dynamics problems because of the complex geometry and motion that a fluid can take; for example, imagine describing the motion of a fluid subject to turbulence within a centrifugal pump. This topic is further covered in {ref}`fvm_frames`, but a formal derivation is generally outside the scope of this textbook.

To give an idea for how FVM is used in various civil and environmental engineering and geosciences applications, a few examples are provided here:

* **Fluid mechanics and dynamics**: simulating the flow in rivers and reservoirs, predicting flood propagation, analyzing groundwater flow, pipe and open-channel flows and conduits. FVM allows the discretization of complex spaces to estimate properties such as velocity, pressure and even concentration.  

* **Heat transfer**: conduction through different materials, optimizing heating and cooling systems in buildings and analyzing the thermal behavior of structures.  

* **Contaminant or pollutant transport**: simulate the impact of pollutants in the atmosphere or water bodies. This is crucial for designing pollution control systems and assessing contamination. 

* **Structural analysis**: although less common, FVM can be adapted for stress and deformation in solid bodies. This technique is particularly useful in geotechnical engineering and civil infrastructure where large deformations can occur. 

* **Multi-physics problems**: FVM can handle multi-physics simulations by combining fluid flow, heat transfer, chemical reactions, stress analysis, chemical transport and other processes in a single model. For example, FVM can analyze the thermal behavior of a dam holding back sediment-laden water. 