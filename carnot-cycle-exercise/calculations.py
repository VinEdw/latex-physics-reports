import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Callable

# Constants
R = 8.31

def print_sf(val: float, sig_figs: int) -> None:
    """
    Print the input value to the specified number of sig figs.
    """
    print(f"{val:.{sig_figs}}")

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

def get_isotherm_func(P_i: float, V_i: float) -> Callable[[float], float]:
    """
    Return a function that takes volume as an input and returns pressure.
    The function will be an isotherm that passes through the inital point.
    """
    return lambda V: P_i * V_i / V

def get_adiabat_func(gamma: float, P_i: float, V_i: float) -> Callable[[float], float]:
    """
    Return a function that takes volume as an input and returns pressure.
    The function will be an adiabat that passes through the inital point.
    """
    return lambda V: P_i * (V_i / V)**gamma

def plot_pv_section(ax: plt.Axes, V_i: float, V_f: float, P_func: Callable[[float], float], label: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Plot a section of the PV diagram on the given ax from V_i to V_f.
    Use the P_func to get pressure values based on volume values.
    Return the N (V, P) points plotted.
    """
    N = 10
    big_N = 1000
    V_arr_big = np.linspace(V_i, V_f, big_N)
    P_arr_big = P_func(V_arr_big)
    ax.plot(V_arr_big, P_arr_big, "0.3", zorder=0)
    V_arr = np.linspace(V_i, V_f, N+2)
    V_arr = V_arr[1:-1]
    P_arr = P_func(V_arr)
    ax.scatter(V_arr, P_arr, label=label)
    return (V_arr, P_arr)

def plot_labeled_point(ax: plt.Axes, x: float, y: float, label: str) -> None:
    """
    Plot a black labeled point on the specified ax.
    """
    ax.plot(x, y, "ko")
    ax.annotate(label, xy=(x, y), xycoords="data", xytext=(2.5, 2.5), textcoords="offset points")

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
# Point a
V_a = V_b * math.exp(-Q_ab / (n * R * T_H))
P_a = n * R * T_a / V_a
# Point d
V_d = V_a * (T_a / T_d)**(1 / (gamma - 1))
P_d = n * R * T_d / V_d
# Print results
df_key_PVT = pd.DataFrame([
    [P_a, V_a, T_a],
    [P_b, V_b, T_b],
    [P_c, V_c, T_c],
    [P_d, V_d, T_d],
], index=["a", "b", "c", "d"], columns=["P (Pa)", "V (m^3)", "T (K)"])
print(df_key_PVT.to_string(float_format="%.3g"))

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
Delta_S_cd = Q_cd / T_C
# d -> a
Q_da = 0
W_da = adiabatic_work(gamma, P_d, V_d, P_a, V_a)
Delta_U_da = - W_da
Delta_S_da = 0
# Print results
df_key_processes = pd.DataFrame([
    [Q_ab, W_ab, Delta_U_ab, Delta_S_ab],
    [Q_bc, W_bc, Delta_U_bc, Delta_S_bc],
    [Q_cd, W_cd, Delta_U_cd, Delta_S_cd],
    [Q_da, W_da, Delta_U_da, Delta_S_da],
], index=["a->b", "b->c", "c->d", "d->a"], columns=["Q (J)", "W (J)", "ΔU (J)", "ΔS (J/K)"])
print(df_key_processes.to_string(float_format="%.3g"))

# 40 additional PV points
# Create the figure
fig, ax = plt.subplots(figsize=(8,6))
# Set the axes labels and title
ax.set_xlabel("$V$ ($\mathrm{m^3}$)")
ax.set_ylabel("$P$ ($\mathrm{Pa}$)")
ax.set_title("Carnot Cycle $PV$ Diagram")
# Remove the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# a -> b
isotherm_ab = get_isotherm_func(P_a, V_a)
V_ab, P_ab = plot_pv_section(ax, V_a, V_b, isotherm_ab, "$a \\to b$")
# b -> c
adiabat_bc = get_adiabat_func(gamma, P_b, V_b)
V_bc, P_bc = plot_pv_section(ax, V_b, V_c, adiabat_bc, "$b \\to c$")
# c -> d
isotherm_cd = get_isotherm_func(P_c, V_c)
V_cd, P_cd = plot_pv_section(ax, V_c, V_d, isotherm_cd, "$c \\to d$")
# d -> a
adiabat_da = get_adiabat_func(gamma, P_d, V_d)
V_da, P_da = plot_pv_section(ax, V_d, V_a, adiabat_da, "$d \\to a$")
# Add the labeled key points
plot_labeled_point(ax, V_a, P_a, "a")
plot_labeled_point(ax, V_b, P_b, "b")
plot_labeled_point(ax, V_c, P_c, "c")
plot_labeled_point(ax, V_d, P_d, "d")
# Turn off scientific notation for the tick marks
ax.ticklabel_format(useOffset=False, style="plain")
# Add a legend
ax.legend()
# Save the figure
fig.savefig("pv-diagram-carnot-cycle.png")

# Print the PV points that were plotted
P_full = np.concatenate([P_a, P_ab, P_b, P_bc, P_c, P_cd, P_d, P_da], axis=None)
V_full = np.concatenate([V_a, V_ab, V_b, V_bc, V_c, V_cd, V_d, V_da], axis=None)
labels = np.concatenate(["$a$", ["$a \\to b$"]*10, "$b$", ["$b \\to c$"]*10, "$c$", ["$c \\to d$"]*10, "$d$", ["$d \\to a$"]*10], axis=None)
df_PV_points = pd.DataFrame({"$P$ (Pa)": P_full, "$V$ (m^3)": V_full}, index=labels)
print(df_PV_points.to_latex(float_format="%.2e", escape=False))