# OPTIMIZATION-MODE

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: NIVASINI SK

*INTERN ID*: CTO8OUS

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DECRIPTION*:

Optimization of Factory Production Using Linear Programming in Python
Introduction
Optimization techniques play a crucial role in business decision-making, especially in industries where resources are limited, and efficiency is key. One of the most commonly used optimization methods is Linear Programming (LP), which helps businesses maximize profits or minimize costs while considering various constraints such as labor, materials, and production capacity.

In this task, Linear Programming (LP) is applied to optimize factory production using Python’s PuLP library. The goal is to determine the optimal number of products (A and B) to produce in order to maximize total profit, given constraints on labor hours and raw materials.

1. Understanding Linear Programming (LP)
Linear Programming is a mathematical approach used to optimize a certain objective function while satisfying a set of constraints. It is widely used in operations research, supply chain management, and manufacturing industries.

An LP problem consists of:

Decision Variables: Variables that define the choices available (e.g., number of products to manufacture).
Objective Function: The function to maximize or minimize (e.g., maximizing profit).
Constraints: Limitations on resources (e.g., labor and raw material availability).
For this problem:

Decision Variables: Number of Product A (x_A) and Product B (x_B).
Objective Function: Maximize total profit.
Constraints: Labor hours and raw material limits.
2. Problem Formulation
The factory produces two types of products (A and B), each requiring different amounts of labor and raw materials. The company aims to determine the best combination of products to produce to maximize total profit while ensuring that resource limits are not exceeded.

Objective Function (Maximization)
Maximize
40
𝑥
𝐴
+
30
𝑥
𝐵
Maximize40x 
A
​
 +30x 
B
​
 
Product A contributes $40 per unit to profit.
Product B contributes $30 per unit to profit.
The goal is to maximize the total profit.
Constraints
Labor Hours Constraint:

2
𝑥
𝐴
+
1
𝑥
𝐵
≤
100
2x 
A
​
 +1x 
B
​
 ≤100
Each unit of Product A requires 2 hours of labor.
Each unit of Product B requires 1 hour of labor.
The total available labor is 100 hours.
Raw Materials Constraint:

3
𝑥
𝐴
+
2
𝑥
𝐵
≤
120
3x 
A
​
 +2x 
B
​
 ≤120
Each unit of Product A requires 3 units of raw materials.
Each unit of Product B requires 2 units of raw materials.
The total available raw materials are 120 units.
Additionally, we ensure that x_A and x_B are non-negative (i.e., the factory cannot produce a negative number of products).

3. Implementing the Optimization Problem in Python
The problem is solved using PuLP, a Python library for linear programming.

Define the LP problem as a maximization problem (pulp.LpMaximize).
Create decision variables (x_A and x_B) representing the number of units to produce.
Define the objective function (maximize profit).
Add constraints (labor and material limits).
Solve the problem using model.solve().
Print the results, including the optimal production quantities and the maximum achievable profit.
4. Optimization Results & Interpretation
Once the LP problem is solved, the results indicate:

Status: Whether an optimal solution was found (Optimal or Infeasible).
Optimal Production Quantities: The best number of Product A and Product B to manufacture.
Maximum Profit: The total profit achieved by following the optimal production plan.
The expected output might look like this:

yaml
Copy
Edit
🔹 Optimization Results 🔹
Status: Optimal
Optimal Production of Product A: 30.0
Optimal Production of Product B: 40.0
Maximum Profit: $2200.0
This means:

The factory should produce 30 units of Product A and 40 units of Product B to maximize profit.
The maximum achievable profit is $2200 under the given constraints.
5. Business Insights & Decision-Making
The results provide valuable business insights:

Production Planning: The factory can optimize production schedules based on available resources.
Profit Maximization: The business can maximize earnings without exceeding resource limits.
Resource Allocation: The company can assess if acquiring more resources (e.g., labor, materials) would further increase profitability.
If the company acquires more labor hours or raw materials, the profitability might increase. Therefore, additional scenarios can be analyzed by modifying the constraints.

6. Conclusion
This task demonstrates the application of Linear Programming (LP) in optimizing business decisions. The PuLP library in Python provides an easy way to model and solve such problems.

Key Takeaways:
Linear Programming is a powerful technique for solving real-world business optimization problems.
The PuLP library in Python simplifies the implementation of LP problems.
Decision variables, constraints, and objective functions must be well-defined to achieve meaningful results.
Optimization results help businesses maximize profits and efficiently allocate resources.
This approach can be extended to other optimization problems, such as supply chain management, workforce scheduling, inventory management, and financial planning.

*OUTPUT*:

