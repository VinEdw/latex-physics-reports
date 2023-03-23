import math
import pandas as pd

# Constants
R = 8.31

def isothermal_work(n: float, T: float, V_i: float, V_f: float) -> float:
    """
    Return the work done by a gas during an isothermal process.
    """
    return n * R * T * math.log(V_f / V_i)

def adiabatic_work(gamma: float, P_i: float, V_i: float, P_f: float, V_f: float) -> float:
    """
    Return the work done by a gas during an adiabatic process.
    """
    return (P_i * V_i - P_f * V_f) / (gamma - 1)

# Givens
T_H = 490
T_C = 300
P_c = 1.01E5
V_c = 1.90E-3
Q_ab = 300
Q_H = Q_ab
gamma = 1.40

# Temperatures at key points
T_a = T_H
T_b = T_H
T_c = T_C
T_d = T_C

# Moles of gas (n)
n = (P_c * V_c) / (R * T_c)

# Pressure and volume at key points
# Point b
V_b = V_c * (T_c / T_b)**(1 / (gamma - 1))
P_b = n * R * T_b / V_b
# Point a
V_a = V_b * math.exp(-Q_ab / (n * R * T_H))
P_a = n * R * T_a / V_a
# Point d
V_d = V_a * (T_a / T_d)**(1 / (gamma - 1))
P_d = n * R * T_d / V_d
# Put results in table
df_key_PVT = pd.DataFrame([
    [P_a, V_a, T_a],
    [P_b, V_b, T_b],
    [P_c, V_c, T_c],
    [P_d, V_d, T_d],
], index=["a", "b", "c", "d"], columns=["P (Pa)", "V (m^3)", "T (K)"])

# Process variables at key transitions
# a -> b
Delta_U_ab = 0
W_ab = Q_ab
Delta_S_ab = Q_ab / T_H
# b -> c
Q_bc = 0
W_bc = adiabatic_work(gamma, P_b, V_b, P_c, V_c)
Delta_U_bc = - W_bc
Delta_S_bc = 0
# c -> d
Delta_U_cd = 0
W_cd = isothermal_work(n, T_C, V_c, V_d)
Q_cd = W_cd
Q_C = Q_cd
Delta_S_cd = Q_cd / T_C
# d -> a
Q_da = 0
W_da = adiabatic_work(gamma, P_d, V_d, P_a, V_a)
Delta_U_da = - W_da
Delta_S_da = 0
# Total
Q_tot = Q_H + Q_C
W_tot = W_ab + W_bc + W_cd + W_da
Delta_U_tot = Delta_U_ab + Delta_U_bc + Delta_U_cd + Delta_U_da
Delta_S_tot = Delta_S_ab + Delta_S_bc + Delta_S_cd + Delta_S_da
# Put results in table
df_key_processes = pd.DataFrame([
    [Q_ab, W_ab, Delta_U_ab, Delta_S_ab],
    [Q_bc, W_bc, Delta_U_bc, Delta_S_bc],
    [Q_cd, W_cd, Delta_U_cd, Delta_S_cd],
    [Q_da, W_da, Delta_U_da, Delta_S_da],
    [Q_tot, W_tot, Delta_U_tot, Delta_S_tot],
], index=["a->b", "b->c", "c->d", "d->a", "Total"], columns=["Q (J)", "W (J)", "ΔU (J)", "ΔS (J/K)"])

if __name__ == "__main__":
    print(df_key_PVT.to_string(float_format="%.3g"))
    print(df_key_processes.to_string(float_format="%.3g"))