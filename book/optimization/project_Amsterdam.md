(optimization_project)=
# Amsterdam HoReCa Waterborne Logistics Network Design

% START-CREDIT
% source: optimization
```{attributiongrey} Attribution
:class: attribution
This section of the optimization chapter incorporates content from [Nadia Pourmohammad-Zia (2024)](https://www.sciencedirect.com/science/article/pii/S2210670724001628#sec0011).
```
% END-CREDIT

During Friday’s session, you will work on an urban waterborne logistics planning problem: selecting transfer points (TPs) for HoReCa supplies in the historic center of Amsterdam and assigning HoReCa demand to them. You will explore two optimization approaches side by side:

* a Mixed-Integer Linear Program (MILP) in Pyomo + HiGHS, and
* a Genetic Algorithm (GA) using PyMOO for multi-objective exploration.

The problem description, mathematical formulation, and guidance for Python implementations are provided below so you can prepare in advance.

```{admonition} MUDE Exam Information
:class: tip, dropdown
The Amsterdam HoReCa Logistics Problem serves as an example for solving a complex optimization problem. You're not expected to understand the problem details for the exam.
```

## Problem description

Amsterdam’s historic city center is characterized by dense urban development, narrow streets, and an extensive system of canals and quay walls. While these waterways historically formed the backbone of urban logistics, modern freight transport has increasingly shifted to road-based delivery systems. As a result, heavy truck traffic now contributes significantly to congestion, air pollution, and accelerated degradation of quay walls and bridges, which are already under substantial structural strain.

In recent years, the Municipality of Amsterdam (MoA) has explored the potential of reactivating urban waterways to support sustainable logistics. One promising opportunity lies in serving the city’s Hotels, Restaurants and Cafés (HoReCa), which generate frequent and predictable supply demand. Using vessels to transport goods through the canals and then transferring cargo to light vehicles (LVs) for last-mile delivery allows pressure on road infrastructure to be reduced, while improving environmental performance.

To enable this system, the city must establish Transfer Points (TPs): locations along the canal network where vessels can dock and supplies can be transshipped onto LVs. These transfer points must be carefully selected, as space is limited and development is constrained by quay wall conditions, bridge clearances, and spatial compatibility with surrounding urban functions.

In this assignment, you take the role of an urban logistics planner tasked with designing an optimal HoReCa supply network for the historical center of Amsterdam. MoA has pre-identified several potential candidate locations for these TPs. Each location has an associated establishment cost and limited handling capacity. At the same time, multiple HoReCa demand zones across the city center require regular deliveries of goods.

Your task is to determine:
* Which transfer points should be established, and
* How much HoReCa demand from each zone should be routed through each established TP.

Opening additional TPs improves proximity and service quality for Horeca businesses but increases investment and operational costs. Routing flow over long distances increases emissions and delivery times. Furthermore, each TP has limited capacity and cannot serve unlimited demand. These competing considerations lead to a trade-off between cost efficiency, environmental performance, and service accessibility.

```{figure} https://files.mude.citg.tudelft.nl/MoA_map.png
---
height: 250px
---
Amsterdam Canal Network and Historic Center
```

### 1. Core assumptions
To maintain focus on core optimization concepts, we make the following simplifying assumptions:

* **Static and known HoReCa demand**  
   We assume that weekly demand at each HoReCa demand zone ($i$) is known and fixed. This demand, measured in delivery units (e.g., containers or pallets), is denoted by $d_i$. Each zone represents a cluster of Restaurants, Cafés or Hotels. Demand from each zone may be served through multiple transfer points (multi-sourcing), although real operations may prefer fewer supply points.
   
* **Two-leg logistics chain: vessels + LVs**  
   All goods originate from a central consolidation hub outside the historic center to TP $j$ using a vessel via canals. They must ultimately reach HoReCa demand zone $i$ using an LV. Thus, each TP acts as an interface between waterborne transport and low-emission last-mile delivery.
   
* **Generalized transport cost**  
Total transport cost to serve zone $i$ via TP $j$ is modeled as a linear function of distance moved and cargo volume. Because each unit must travel both legs, we define a combined cost:

     $ {CT}_{ij} = c^{water}. t_{0j}^{water} + c^{road}. t_{ij}^{road}$ 

  where:

  * $c^{water}$ is the cost per unit distance by vessel. 
  * $c^{road}$ is the cost per unit distance by LV. 

  This formulation captures major energy, time, and operating components of freight transport.
   
* **Transfer point capacity and opening cost**  
   Each candidate TP ($j$) has a maximum handling capacity (${cap}_j$).  
   Opening a TP incurs a fixed cost $f_j$, representing quay adjustments, infrastructure, and operational setup. If not opened, its capacity cannot be used.

* **Service distance limit**  
   To ensure feasible LV delivery, each TP can only serve zones within a maximum road delivery distance $D_{max}$. Assignments beyond this threshold are forbidden.

* **Budget or siting constraints**  
   The planner must stay within investment limits. Two common policies are:
   - A total budget ($B$) restricting total fixed cost.
   - A maximum number of TPs ($K$) that can be developed.  
   These reflect financial and organisational constraints.

* **${CO}_2$ emissions factor**  
Both vessel transport and LV deliveries generate emissions:

     $ {Em}_{ij} = e^{water}. t_{0j}^{water} + e^{road}. t_{ij}^{road}$ 

  where:

  * $e^{water}$ is ${CO}_2$ is emission per unit distance by vessel. 
  * $e^{road}$ is ${CO}_2$ is the cost per unit distance by LV.

  Vessel transport is comparatively efficient, whereas last-mile delivery contributes increasingly if distances become long.

## Mathematical formulation
This section presents the mathematical formulation of the problem.

---
### Sets

- $I$: set of HoReCa demand zones  
- $J$: set of candidate transfer points
- $A = \{(i,j) \in I \times J\}$:  zone–TP pairs  

---
### Parameters

- $d_i$: demand at zone $i$
- ${cap}_j$: capacity of TP $j$ 
- $f_j$: fixed cost of establishing TP $j$
- $t^{\text{water}}_{0j}$: water distance from consolidation hub to TP $j$  
- $t^{\text{road}}_{ij}$: LV road distance from TP $j$ to zone $i$ 
- $c^{water}$: unit water transport cost  
- $c^{road}$: unit road transport cost 
- $e^{water}$: unit emission factor for vessels  
- $e^{road}$: unit emission factor for LVs  
- $D_{max}$: maximum delivery distance  
- $\delta_{ij}$: if TP $j$ is allowed to serve zone $i$ ($ t^{\text{road}}_{ij} \leq D_{max}$)
- $B$: investment budget  
- $K$: maximum number of TPs allowed 
- $\lambda \ge 0$: emission penalty factor  

---

### Decision variables

- $x_j \in \{0,1\}$: 1 if TP $j$ is opened; 0 otherwise  
- $y_{ij} \geq 0$: flow from TP $j$ to demand zone $i$

---

### Objective function
$$Z = \underbrace{\sum_{j \in J} f_j\,x_j}_{\text{Fixed establishment cost}}
+
\underbrace{\sum_{(i,j)\in A}
{CT}_{ij}.y_{ij}}_{\text{Transport cost}}
+
\lambda
\underbrace{\sum_{(i,j)\in A}
{Em}_{ij}.y_{ij}}_{\text{Emission penalty cost}}$$

The parameter $\lambda$ represents an emission penalty factor, expressed in monetary units. nstead of treating emissions as a separate objective, emissions are internalised into the total cost through this penalty.

### Constraints
#### 1. Demand fulfillment
Each demand zone must be fully served (multi-sourcing allowed).

$$ \sum_{j \in J} y_{ij} = d_i
\qquad \forall i \in I$$

#### 2. TP capacity
Total flow through an opened TP cannot exceed its capacity.

$$\sum_{i \in I} y_{ij} \leq {cap}_jx_j
\qquad \forall j \in J$$

#### 3. Budget constraint
Total investment in opened TPs must remain within the available budget.

$$\sum_{j \in J} f_j x_j \leq B$$


#### 4. Siting limit
A maximum of $K$ terminals can be opened.

$$\sum_{j \in J} x_j \leq K$$


#### 5. Service distance feasibility
Connections exceeding the road distance limit $D_{max}$ are not allowed

$$y_{ij} \leq M \delta_{ij} \qquad \forall i \in I,\forall j \in J$$


#### 6. Domain of variables
Connections exceeding the road distance limit $D_{max}$ are not allowed

$$ x_{j} \in \{0,1\}$$
$$ y_{ij} \geq 0$$

### Conclusions

Here is the complete problem formulation.

$$\begin{align*}
min \quad  & Z = {\sum_{j \in J} f_j\,x_j}+{\sum_{(i,j)\in A}{CT}_{ij}.y_{ij}}+\lambda{\sum_{(i,j)\in A}{Em}_{ij}.y_{ij}}\\
\text{s.t.} \quad \\
& \sum_{j \in J} y_{ij} = d_i
\qquad \forall i \in I\\
& \sum_{i \in I} y_{ij} \leq {cap}_jx_j
\qquad \forall j \in J\\
& \sum_{j \in J} f_j x_j \leq B\\
& \sum_{j \in J} x_j \leq K\\
& y_{ij} \leq M \delta_{ij} \qquad \forall i \in I,\forall j \in J\\
& x_{j} \in \{0,1\}\\
& y_{ij} \geq 0
\end{align*}$$

## Adaption for GA
The Amsterdam HoReCa Transfer Point Siting & Flow Assignment problem can also be solved using a Genetic Algorithm (GA). While the MILP formulation determines the transfer point locations and flow assignments simultaneously and guarantees optimality (for the chosen objective), a GA provides a heuristic alternative that explores the solution space through evolutionary search.

In order to make the GA implementation efficient and manageable, we decompose the problem into two linked sub-problems:

1. Network design sub-problem (handled by GA): The GA decides which transfer points (TPs) are opened.

2. Flow assignment sub-problem (solved for each GA solution):Given the selected TPs, HoReCa demand is assigned optimally using a simpler linear optimization model.

This decomposition significantly reduces the size of the search space and ensures stable evaluation of candidate solutions.

### Network Design sub-problem (Handled by GA)
The Network Design sub-problem determines the set of TPs to be opened. The GA attempts to minimise the total system cost:

$$\begin{align*}
min \quad  & Z(x) = {\sum_{j \in J} f_j\,x_j}+{\sum_{(i,j)\in A}{CT}_{ij}.y_{ij}(x)}+\lambda{\sum_{(i,j)\in A}{Em}_{ij}.y_{ij}(x)}\\
\text{s.t.} \quad \\
& \sum_{j \in J} f_j x_j \leq B\\
& \sum_{j \in J} x_j \leq K\\
& x_{j} \in \{0,1\}\\
\end{align*}$$

In the objective function, only the first term depends directly on the chromosome. The remaining two terms depend on the flows $y_{ij}(x)$, which are unknown until the flow-assignment sub-problem is solved. 

Each GA individual consists of a binary vector:
$$x=(x_1,x_2,...,x_{|J|}), \qquad x_j \in \{0,1\}$$

where $x_j=1$ indicates that TP $j$ is opened. The GA explores different combinations of these TP-opening decisions using crossover and mutation.

### Flow Assignment sub-problem (MILP)
For each candidate TP configuration $x$ produced by the GA, we solve the following linear optimisation problem to compute the optimal flows:

$$\begin{align*}
min \quad  & Z(y) = {\sum_{(i,j)\in A}{CT}_{ij}.y_{ij}}+\lambda{\sum_{(i,j)\in A}{Em}_{ij}.y_{ij}}\\
\text{s.t.} \quad \\
& \sum_{j \in J} y_{ij} = d_i
\qquad \forall i \in I\\
& \sum_{i \in I} y_{ij} \leq {cap}_jx_j
\qquad \forall j \in J\\
& y_{ij} \leq M \delta_{ij} \qquad \forall i \in I,\forall j \in J\\
& y_{ij} \geq 0
\end{align*}$$

This model determines how HoReCa demand is distributed across open TPs such that transport cost and emissions are minimized, while respecting TP capacities and service distance limits.

### Feasibility
Since the GA generates terminal-opening patterns freely, some candidate solutions will violate constraints. We distinguish between two types of infeasibility and treat them differently.

#### Flow infeasibility
Flow infeasibility occurs when no valid cargo assignment exists for a given TP configuration. In these cases, the flow-assignment sub-problem has no solution and the objective function cannot be evaluated. These situations must therefore be corrected before evaluation. Two common causes are:

1. Insufficient total capacity: If the total capacity of selected TPs is less than total demand, there is no feasible way to serve all demand.

2. If a demand zone $i$ has no open terminal within the maximum service distance, then its demand cannot be assigned. 

In such cases, a repair operator is applied before evaluation. This operator modifies the solution by activating additional TPs until sufficient capacity is available, and every demand zone has at least one reachable open terminal.

The choice of which TPs to activate can follow a simple rule, such as selecting the nearest or lowest-cost feasible terminal. After repair, the flow-assignment problem becomes solvable and the full objective function can be evaluated.

#### Policy infeasibility
Policy constraints reflect strategic or institutional limits rather than physical impossibility, including budget and maximum number of established TPs. If these constraints are violated, a feasible flow assignment can still be computed: all demand can still be routed and flow balance can be satisfied. Therefore, these solutions remain technically evaluable. Instead of repairing such solutions, we apply a penalty approach: 
$$Z_{final}​(x)= Z(x)+P. v(x)$$
where $v(x)$ represents the magnitude of violation and P is the violation penalty factor.

### Summary
The following figure illustrates the flowchart of steps requierd to be taken to solve this problem with GA.

```{figure} https://files.mude.citg.tudelft.nl/Flowchart.png
---
height: 250px
---
Solution flowchart
```
## Implementation 
We implement the Genetic Algorithm using the Python library PyMOO, which provides ready-made tools for evolutionary search, including population initialization, crossover, mutation, and constraint handling. Although PyMOO is designed to support multi-objective optimization, in this assignment we use it in a single-objective setting to minimize the same weighted objective function as in the MILP model.

Each GA individual is a binary vector indicating which TPs are opened. PyMOO evaluates an individual by first applying the repair operator (to ensure that the flow-assignment problem is feasible) and then solving this sub-problem to compute the flows $y_{ij}(x)$. Only at that point can the transport and emission terms be calculated, and the full fitness value $Z(x)$ obtained. Budget and maximum-terminal violations do not prevent the assignment step, so they are handled by adding a large penalty to the objective. PyMOO then evolves the population across generations based on these fitness values.

% START-CREDIT
% source: optimization
```{attributiongrey} Attribution
:class: attribution
This section of the optimization chapter is written by Nadia Pourmohammadzia. {ref}`Find out more here <optimization_credit>`.
```
% END-CREDIT
