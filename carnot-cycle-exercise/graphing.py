from calculations import *
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

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
    ax.plot(V_arr_big, P_arr_big, zorder=0)
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
    ax.annotate(label, xy=(x, y), xycoords="data", xytext=(2.5, 2.5), textcoords="offset points", fontsize="x-large")

def draw_midline_arrow(ax: plt.Axes, x_i: float, y_i: float, x_f: float, y_f: float):
    """
    Plot an arrow in the middle of the line pointing from the starting point to the ending point.
    """
    scale = 0.01
    x = (x_i + x_f) / 2
    y = (y_i + y_f) / 2
    displacement = complex(x_f - x_i, y_f - y_i)
    direction = displacement / abs(displacement) * scale
    dx = direction.real
    dy = direction.imag
    ax.annotate("", (x+dx, y+dx), (x-dx, y-dy), arrowprops=dict(arrowstyle="-|>"))

# Create the figure
fig, ax = plt.subplots(figsize=(8,6))
# Set the axes labels and title
ax.set_xlabel("$V$ ($\mathrm{m^3}$)", fontsize="x-large")
ax.set_ylabel("$P$ ($\mathrm{Pa}$)", fontsize="x-large")
ax.set_title("Carnot Cycle $PV$-Diagram", fontsize="x-large")
# Remove the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# 40 additional PV points
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
# Include (0, 0)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
# Turn off scientific notation for the tick marks
ax.ticklabel_format(useOffset=False, style="plain")
# Add a legend
ax.legend()
# Save the figure
fig.savefig("pv-diagram-carnot-cycle.eps")

# Print the PV points that were plotted
P_full = np.concatenate([P_a, P_ab, P_b, P_bc, P_c, P_cd, P_d, P_da], axis=None)
V_full = np.concatenate([V_a, V_ab, V_b, V_bc, V_c, V_cd, V_d, V_da], axis=None)
labels = np.concatenate(["$a$", ["$a \\to b$"]*10, "$b$", ["$b \\to c$"]*10, "$c$", ["$c \\to d$"]*10, "$d$", ["$d \\to a$"]*10], axis=None)
df_PV_points = pd.DataFrame({"$P$ (Pa)": P_full, "$V$ (m^3)": V_full}, index=labels)
print(df_PV_points.to_latex(float_format="%.2e", escape=False))

# Create the temperature entropy (TS) diagram
# Assume an initial entropy value
S_a = 0.05
# Calculate the rest of the entropy values
S_b = S_a + Delta_S_ab
S_c = S_b + Delta_S_bc
S_d = S_c + Delta_S_cd
# Plot the TS values
S_arr = np.array([S_a, S_b, S_c, S_d, S_a])
T_arr = np.array([T_a, T_b, T_c, T_d, T_a])
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(S_arr, T_arr)
# Remove the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# Set the axes labels and title
ax.set_xlabel("$S$ (J/K)", fontsize="x-large")
ax.set_ylabel("$T$ (K)", fontsize="x-large")
ax.set_title("Carnot Cycle $TS$-Diagram", fontsize="x-large")
# Include (0, 0)
ax.set_xlim(left=0, right=0.75)
ax.set_ylim(bottom=0, top=650)
# Add the labeled key points
plot_labeled_point(ax, S_a, T_a, "a")
plot_labeled_point(ax, S_b, T_b, "b")
plot_labeled_point(ax, S_c, T_c, "c")
plot_labeled_point(ax, S_d, T_d, "d")
# Add the arrows
draw_midline_arrow(ax, S_a, T_a, S_b, T_b)
draw_midline_arrow(ax, S_b, T_b, S_c, T_c)
draw_midline_arrow(ax, S_c, T_c, S_d, T_d)
draw_midline_arrow(ax, S_d, T_d, S_a, T_a)
# Save the figure
fig.savefig("ts-diagram-carnot-cycle.eps")
