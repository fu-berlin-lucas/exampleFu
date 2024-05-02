import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("SimpleLP")

# Add decision variables
x1 = model.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = model.addVar(vtype=GRB.CONTINUOUS, name="x2")

# Set the objective function
model.setObjective(3 * x1 + 4 * x2, GRB.MAXIMIZE)

# Add constraints
model.addConstr(2 * x1 + x2 <= 10, "c1")
model.addConstr(x1 + 3 * x2 <= 15, "c2")

# Optimize the model
model.optimize()

# Display results
if model.status == GRB.OPTIMAL:
    print(f"Optimal solution found:")
    print(f"x1 = {x1.x}")
    print(f"x2 = {x2.x}")
    print(f"Objective value = {model.objVal}")

else:
    print(f"Optimization was not successful. Status: {model.status}")