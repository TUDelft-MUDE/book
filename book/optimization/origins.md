# Optimization origins

In the UK and the US, scientists started to be called between WWI and WWII to collaborate with the military in doing **research** on military **operations**. A second WW was on the horizon and both countries wanted to be prepared by optimizing their logistics to maximize their chances of winning battles.

They created a field of applied sciences known as **Operations Research** in which **Optimization** has been placed.

## The radar

Modern operations research originated in the UK in 1937 and was the result of an initiative of the superintendent, A. P. Rowe.

Rowe conceived the idea to analyze and improve the working of the UK's early warning radar system, Chain Home (CH). Initially, he analyzed the operation of the radar equipment and
its communication networks to provide a complete vision of the south coast of the UK. **How many radars do you need? Where should they be located?**

The analysis was later expanded to include the operating personnel's behavior to plan the Human Resources (HR) of this system.

This revealed unappreciated limitations of the CH network and allowed remedial action to be taken which helped win the war.

## 1947: the Simplex method is developed

George Dantzig worked on planning methods for the US Army Air Force during World War II using a desk calculator. In 1946 he was challenged to mechanize/automated the planning process that he was using.

Dantzig formulated the planning problem, typically a problem of assigning resources to activities, as linear inequalities (or equalities) inspired by the work of Wassily Leontief, however, at that time **he didn't include an objective as part of his formulation**, he was mainly searching for feasible solutions to a problem.

## Leontief's work: The Input Output matrix

![leontief](./figs/leontief.png "leontief")

In this example a simple economy is described through three main products/activities, Coal, Electricity, and Steel. It’s easy to produce linear equations where the interdependencies between these products are apparent once you have the production factors (how much you need from each one of those to produce the other).

Using the right data and this logic it’s possible to describe the functioning of many systems and their corresponding “products". This is what has inspired Dantzig for his mathematical structure of an optimization problem, he economy structure generates the constraints of what is possible to produce (the solution space).

## Adding an objective to the problem

Without an objective, in many systems a vast number of solutions can be feasible, and therefore to find the "best" feasible solution, military-specified objectives - don’t forget that **Dantzig was studying military operations** - must be used that describe how goals can be achieved as opposed to specifying a specific value for this goal on itself. For example, it’s not about transporting 1000 soldiers but finding a way to transport as many as possible with the existing resources.

Dantzig's core insight was to realize that most such ground objectives can many times be translated into a **linear objective function** that needs to be maximized (or minimized) that measures the quality/performance of the solutions.

Development of the final method, the so-called **simplex** method, was evolutionary and happened over a period of about a year.
