import math
import numpy as np

def print_sf(val: float, sig_figs: int) -> None:
    """
    Print the input value to the specified number of sig figs.
    """
    print(f"{val:.{sig_figs}}")

# Constants
R = 8.31

# Givens
T_H = 490
T_C = 300
P_c = 1.01E5
V_c = 1.90E-3
Q_ab = 300
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