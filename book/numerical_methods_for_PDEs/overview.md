(NumMethPDE)=
# Numerical Methods for PDEs

% START-CREDIT
% source: numerical_methods_for_PDEs
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Marcel Zijlema. {ref}`Find out more here <numerical_methods_for_pdes_credit>`.
```
% END-CREDIT

In Chapter {ref}`numerical_modelling` ordinary differential equations (ODEs) have been treated.
Their solutions are simply functions of a single independent variable representing time.
Frequently, physical systems often evolve not only in time but also in at least one spatial dimension (usually $x$).

In this chapter, first, a brief review of **partial differential equations** (PDEs) is provided. Next, discretizations of the **diffusion
equation** by employing the **finite difference method** are considered. This is followed by the approximatons of the **advection
equation** and the **advection-diffusion equation**.

Also, special attention is paid to the notion of **consistency** and **stability** of a numerical scheme applied to PDEs.
