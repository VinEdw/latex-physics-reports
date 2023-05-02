import sympy as sp

# Define symbols
E = sp.symbols("E")
R_1 = sp.symbols("R_1")
R_2 = sp.symbols("R_2")
R_3 = sp.symbols("R_3")
i_1 = sp.symbols("i_1")
i_2 = sp.symbols("i_2")
i_3 = sp.symbols("i_3")
C = sp.symbols("C")
q = sp.Function("q")
t = sp.symbols("t")

# Solve system of equations
soln = sp.solve([i_1 - i_2 - i_3,
                 E - i_1 * R_1 - i_2 * R_2,
                 E - i_1 * R_1 - i_3 * R_3 - q(t) / C],
                [i_1, i_2, i_3],
                dict = True)

# Solve the DE for i_3
result = sp.dsolve(soln[0][i_3] - sp.Derivative(q(t), t), ics = {q(0): 0})
sp.pprint(result)

# Substitute values into the expression
expr = result.rhs
time = float(input("Input a t value in seconds\n>>> ").strip())
subs = {E: 15, R_1: 10, R_2: 20, R_3: 30, C: 4, t: time}
charge = expr.subs(subs)
voltage = charge / subs[C]
print(f"V = {voltage} V")
