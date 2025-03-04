import pulp

# Define the Linear Programming problem (Maximization)
model = pulp.LpProblem("Factory_Production_Optimization", pulp.LpMaximize)

# Define Decision Variables
x_A = pulp.LpVariable("Product_A", lowBound=0, cat="Continuous")  # Number of Product A
x_B = pulp.LpVariable("Product_B", lowBound=0, cat="Continuous")  # Number of Product B

# Objective Function: Maximize profit
model += 40 * x_A + 30 * x_B, "Total_Profit"

# Constraints
model += 2 * x_A + 1 * x_B <= 100, "Labor_Hours_Constraint"  # Labor limit
model += 3 * x_A + 2 * x_B <= 120, "Raw_Materials_Constraint"  # Material limit

# Solve the Linear Programming problem
model.solve()

# Print Results
print("🔹 Optimization Results 🔹")
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal Production of Product A: {x_A.varValue}")
print(f"Optimal Production of Product B: {x_B.varValue}")
print(f"Maximum Profit: ${pulp.value(model.objective)}")
