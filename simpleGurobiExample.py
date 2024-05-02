import gurobipy as gp
from gurobipy import GRB

model = gp.Model("SimpleLP")

x1 = model.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = model.addVar(vtype=GRB.CONTINUOUS, name="x2")

model.setObjective(3 * x1 + 4 * x2, GRB.MAXIMIZE)

model.addConstr(2 * x1 + x2 <= 10, "c1")
model.addConstr(x1 + 3 * x2 <= 15, "c2")

model.optimize()

if model.status == GRB.OPTIMAL:
    print(f"Optimal solution found:")
    print(f"x1 = {x1.x}")
    print(f"x2 = {x2.x}")
    print(f"Objective value = {model.objVal}")

else:
    print(f"Optimization was not successful. Status: {model.status}")