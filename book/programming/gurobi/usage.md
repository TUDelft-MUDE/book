(gurobi-usage)=
# Gurobi Usage

```{note}
This is taken from the WS for Week 2.5. It needs to be:
- generalized and the OOP connection illustrated
- a PA needs to be made to illustrate improper use of the gurobi model (or a generic class) to avoid the issue of updating constraints
- note also that the sand and clay problem illustrates a python implementation (not interactive)
```

## This is the outline proposed by Robert in WS 2.5 for this year

## Create model with Gurobi

Remember that examples of using Gurobi to create and optimize a model are provided in the online textbook, and generally consist of the following steps (the first instantiates a class and the rest are executed as methods of the class):

1. Define the model (instantiate the class)
2. Define variables
3. Define objective function
4. Add constraints
5. Optimize the model

Remember, you can always ask for help to understand a function of Gurobi
```
help(gurobipy.model.addVars)
```



## this is from WS 2.5

You can always ask for help to understand a function of gurobi

```
help(gurobipy.model.addVars)
```

Create a Gurobi model

```
model = gp.Model("Project_Selection")
```

Define variables (binary, in this case):

```
x = model.addVars(num_projects, vtype=gp.GRB.BINARY, name="x")
```

Objective function: Minimize environmental impact

```
model.setObjective(sum(I[i] * x[i] for i in range(num_projects)), gp.GRB.MINIMIZE)
```

Constraint: Select exactly 3 projects
```
model.addConstr(x.sum() == 3, "Select_Projects")
```

Constraint: Number of type 2 projects must be at least as many as type 1 projects selected
```
model.addConstr(sum(x[i] for i in range(num_type2_projects, num_projects)) - sum(x[i] for i in range(num_type1_projects)) >= 0, "Type_Constraint")
```

Constraint: Minimum profit requirement
```
model.addConstr(sum(P[i] * x[i] for i in range(num_projects)) >= beta, "Minimum_Profit")
```

Optimize the model
```
model.optimize()
```