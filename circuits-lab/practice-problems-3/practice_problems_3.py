import math
import numpy as np
import pandas as pd

def print_prob(number: int):
    """
    A helper function to print the problem number with a consistent format.
    """
    eq_bar = "=" * 20
    print(f"{eq_bar} Problem {number} {eq_bar}")

def print_val(symbol: str, value: int|float, units: str, sig_figs: int = 3) -> str:
    """
    A helper function for printing values with the following form.
    f"{symbol} = {value:#.g{sig_figs}}"
    """
    expr = f"{symbol} = {value:#.{sig_figs}g} {units}"
    print(expr)
    return expr

#################### Problem 1 #################### 
print_prob(1)
# Given
r = 2.00e-3
h = 0.450
V = 6.00
I = 0.500

# V = I * R
R = V / I

# R = rho * h / A
A = math.pi * r**2
rho = R * A / h
P = V * I

# E = rho * J
J = I / A
E = rho * J

# Print
print_val("rho", rho, "Ω m")
print_val("P", P, "W")
print_val("E", E, "N/C")

#################### Problem 2 #################### 
print_prob(2)
# Given
E_1 = 100
E_2 = 200
R_1 = 25
R_2 = 55
R_3 = 100
R_4 = 60

# I_1 + I_3 = I_2
# I_1 - I_2 + I_3 = 0

# E_1 - I_1 R_1 - I_2 R_2 - I_1 R_4 = 0
# I_1 (R_1 + R_4) + I_2 R_2 = E_1

# E_2 - I_3 R_3 - I_2 R_2 = 0
# I_2 R_2 + I_3 R_3 = E_2

matrix = [[1, -1, 1],
          [R_1 + R_4, R_2, 0],
          [0, R_2, R_3]]
constants = [0, E_1, E_2]
I_1, I_2, I_3 = np.linalg.solve(matrix, constants)

df_E = pd.DataFrame({"I": [I_1, I_3],
                     "V": [E_1, E_2]},
                    index = ["E_1", "E_2"])
df_R = pd.DataFrame({"I": [I_1, I_2, I_3, I_1]},
                     index = ["R_1", "R_2", "R_3", "R_4"])
df_R["V"] = df_R["I"] * [R_1, R_2, R_3, R_4]
df_full = pd.concat([df_E, df_R])
df_full["P"] = df_full["V"] * df_full["I"]
# Print
print(df_full.to_string(float_format = "%#.3g"))

#################### Problem 3 #################### 
print_prob(3)
# Given
R_1 = R_2 = R_3 = R_4 = R_5 = R_6 = R_7 = R_8 = R_9 = R_10 = 200

R_3_4 = (R_3**-1 + R_4**-1)**-1
R_1_2 = R_1 + R_2
R_5_6 = R_5 + R_6
R_1_2_3_4_5_6 = (R_1_2**-1 + R_3_4**-1 + R_5_6**-1)**-1
R_9_10 = (R_9**-1 + R_10**-1)**-1
R_8_9_10 = R_8 + R_9_10
R_7_8_9_10 = (R_7**-1 + R_8_9_10**-1)**-1
R_eq = R_1_2_3_4_5_6 + R_7_8_9_10
# Print
print_val("R_eq", R_eq, "Ω")

#################### Problem 4 #################### 
print_prob(4)
# Given
A = 3.30
d = 0.0550e-3
V = 12.5
epsilon_0 = 8.854e-12

C = epsilon_0 * A / d
Q = C * V
U = 0.5 * C * V**2

# Print
print_val("Q", Q, "C")
print_val("U", U, "J")

#################### Problem 5 #################### 
print_prob(5)
# Given
C_1 = C_2 = C_3 = C_4 = C_5 = C_6 = C_7 = 2.00

C_6_7 = C_6 + C_7
C_5_6_7 = (C_5**-1 + C_6_7**-1)**-1
C_3_4_5_6_7 = C_3 + C_4 + C_5_6_7
C_eq = (C_1**-1 + C_2**-1 + C_3_4_5_6_7**-1)**-1

# Print
print_val("C_eq", C_eq, "μF")

#################### Problem 6 #################### 
print_prob(6)
# Given
E = 11.9
R = 32.5
C = 5.25e-6
tau = R * C

Q_0 = 0
I_0 = E / R

Q_max = E * C
I_min = 0

t_1 = 0.257e-3
q_1 = Q_max * (1 - math.exp(-t_1 / tau))
i_1 = I_0 * math.exp(-t_1 / tau)

frac = 0.15
t_2 = -tau * math.log(frac)

# Print
print("Part a.")
print_val("Q_0", Q_0, "C")
print_val("I_0", I_0, "A")
print("Part b.")
print_val("Q_max", Q_max, "C")
print_val("I_min", I_min, "A")
print("Part c.")
print_val("q_1", q_1, "C")
print_val("i_1", i_1, "A")
print("Part d.")
print_val("t_2", t_2, "s")


#################### Problem 7 #################### 
print_prob(7)
# Given
E = 15
C_1 = 25.0e-6
C_2 = 35.0e-6
R_1 = 45.0
R_2 = 55.0
R_3 = 65.0

R_2_3 = (R_2**-1 + R_3**-1)**-1
R_eq = R_1 + R_2_3
i_1 = E / R_eq
V_2_3 = i_1 * R_2_3
i_2 = V_2_3 / R_2
i_3 = V_2_3 / R_3
q_1 = 0
q_2 = 0
print("Part a.")
print_val("i_1", i_1, "A")
print_val("i_2", i_2, "A")
print_val("i_3", i_3, "A")
print_val("q_1", q_1, "C")
print_val("q_2", q_2, "C")

C_eq = (C_1**-1 + C_2**-1)**-1
i_3 = 0
i_1 = i_2 = E / (R_1 + R_2)
V_C_eq = i_2 * R_2
q_eq = C_eq * V_C_eq
q_1 = q_2 = q_eq
print("Part b.")
print_val("i_1", i_1, "A")
print_val("i_2", i_2, "A")
print_val("i_3", i_3, "A")
print_val("q_1", q_1, "C")
print_val("q_2", q_2, "C")

U_1 = q_1**2 / (2 * C_1)
U_2 = q_2**2 / (2 * C_2)
print("Part c.")
print_val("U_1", U_1, "J")
print_val("U_2", U_2, "J")

print("Part d.")
print("C_eq = (C_1**-1 + C_2**-1)**-1")
print("R_eq = R_3 + (R_1**-1 + R_2**-1)**-1")
print("V_max = E * R_2 / (R_1 + R_2)")
print("tau = R_eq * C_eq")
print("q_1(t) = C_eq * V_max * (1 - e**(-t / tau ))")
print("q_2(t) = q_1(t)")
print("i_3(t) = V_max / R_eq * e**(-t / tau )")
print("i_2(t) = (i_3(t) * R_3 + q_1(t) / C_1 + q_2(t) / C_2) / R_2")
print("i_1(t) = (E - i_3(t) * R_3 - q_1(t) / C_1 - q_2(t) / C_2) / R_1")
