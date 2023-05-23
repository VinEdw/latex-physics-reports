import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_angle_quadrant(angle):
    """
    Determine the quadrant of the input angle in radians.
    Return an integer between 1 and 4 inclusive.
    """
    quadrant_size = np.pi / 2
    quadrant_count = np.floor(angle / quadrant_size)
    quadrant_num = quadrant_count % 4 + 1
    return quadrant_num

def polar_to_cartesian(r, theta):
    """
    Convert the given polar coordinates (r, theta) to Cartesian (x, y).
    """
    return r * np.cos(theta), r * np.sin(theta)

def plot_phasor(ax, length, angle, label, color):
    """
    Plot a phase vector given axes.
    Set the length, angle, and color.
    """
    x, y = polar_to_cartesian(length, angle)
    ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, label=label, color=color)
    lims = np.array((*ax.get_xlim(), *ax.get_ylim(), x, y))
    max_lim = np.max(np.abs(lims))
    ax.set_xlim(left=-max_lim, right=max_lim)
    ax.set_ylim(bottom=-max_lim, top=max_lim)

def create_phasor_diagram(fname, title, offset, V_R, V_L, V_C, E_0):
    """
    Create a phasor diagram plot and save the figure.
    """
    fig, ax = plt.subplots()
    # Set the title
    ax.set_title(title)
    # Initialize the plot limits to that of the resistor voltage
    # Ensures plot is fit to the phasors
    V_R_lims = np.array(polar_to_cartesian(V_R, offset))
    max_lim = np.max(np.abs(V_R_lims))
    ax.set_xlim(left=-max_lim, right=max_lim)
    ax.set_ylim(bottom=-max_lim, top=max_lim)
    # Hide the top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Center the left and bottom spines
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    # Turn off tick marks
    ax.set_xticks([])
    ax.set_yticks([])
    # Fix the aspect ratio as 1:1
    ax.axes.set_aspect("equal")
    # Plot the phasors
    # V_R
    plot_phasor(ax, V_R, offset, "$V_R$", "r")
    # V_L
    plot_phasor(ax, V_L, offset + np.pi / 2, "$V_L$", "b")
    # V_C
    plot_phasor(ax, V_C, offset - np.pi / 2, "$V_C$", "g")
    # E_0
    phi = np.arctan((V_L - V_C) / V_R)
    plot_phasor(ax, E_0, offset + phi, "$\\mathcal{E}_0$", "y")
    # Put the legend in the quadrant opposite the offset angle
    offset_quadrant = get_angle_quadrant(offset)
    section_map = {1: "lower left",
                   2: "lower right",
                   3: "upper right",
                   4: "upper left"}
    section = section_map[offset_quadrant]
    ax.legend(loc=section)
    fig.savefig(fname)
    
# Measured values for the circuit components
# All units in standard SI without any prefixes
R_1 = 150.5 # ohms
R_2_3 = 159.8 # ohms
C = 1.543e-6 # F
L = 12.16e-3 # H
E_0 = 6.46 # V

# Set the measured values for each part
# Part 1
df_1 = pd.DataFrame([[400, 21.37e-3],
                     [800, 32.12e-3],
                     [2000, 38.74e-3],
                     [4000, 20.66e-3],
                     ], columns=["f", "I_0_ex"])
df_1.name = "part_1"
df_1["E_0"] = E_0
df_1["R"] = R_1
df_1["C"] = C
df_1["L"] = 0

# Part 2
df_2 = pd.DataFrame([[400, 39.27e-3],
                     [800, 37.41e-3],
                     [2000, 28.21e-3],
                     [4000, 9.29e-3],
                     ], columns=["f", "I_0_ex"])
df_2.name = "part_2"
df_2["E_0"] = E_0
df_2["R"] = R_2_3
df_2["C"] = 0
df_2["L"] = L

# Part 3
df_3 = pd.DataFrame([[10e-3, 163],
                     [20e-3, 342],
                     [30e-3, 565],
                     [39.81e-3, 1178],
                     [30e-3, 2240],
                     [20e-3, 3045],
                     [10e-3, 3995],
                     ], columns=["I_0_ex", "f"])
df_3.name = "part_3"
df_3["E_0"] = E_0
df_3["R"] = R_2_3
df_3["C"] = C
df_3["L"] = L

# Calculate a bunch of different columns for each dataframe
df_list = (df_1, df_2, df_3)
for df in df_list:
    df["omega"] = 2 * np.pi * df["f"]
    df["X_L"] = df["omega"] * df["L"]
    df["X_C"] = 1/(df["omega"] * df["C"])
    df["X_C"] = df["X_C"].replace(np.inf, 0)
    df["Z"] = np.sqrt(df["R"]**2 + (df["X_L"] - df["X_C"])**2)
    df["I_0_th"] = df["E_0"] / df["Z"]
    df["V_R"] = df["I_0_ex"] * df["R"]
    df["V_L"] = df["I_0_ex"] * df["X_L"]
    df["V_C"] = df["I_0_ex"] * df["X_C"]
    df["fname"] = df.apply(lambda x: f"media/{df.name}_{x['f']:.0f}_hz.png", axis=1)
    df["title"] = df.apply(lambda x: f"{x['f']:.0f} Hz", axis=1)
    # Print the name of the dataframe and the desired columns
    print(df.name)
    desired_colums = ["f", "Z", "I_0_th", "I_0_ex"]
    print(df[desired_colums].to_string(float_format="%#.3g"))

# Create a phasor diagram for each set of measurements
# Save the figures in a media folder
for df in df_list:
    for i, trial in df.iterrows():
        offset = np.pi / 3
        create_phasor_diagram(trial["fname"], trial["title"], offset, trial["V_R"], trial["V_L"], trial["V_C"], trial["E_0"])

# Create a markdown file with all the figures in it and render it with pandoc
doc_str = "# AC Circuits Lab Phasor Diagrams\n\n"
doc_name = "phasor_diagrams"
md_fname = f"{doc_name}.md"
pdf_fname = f"{doc_name}.pdf"
for df in df_list:
    doc_str += f"## {df.name}\n\n"
    for i, trial in df.iterrows():
        fname = trial["fname"]
        fig_str = f"![]({fname})"
        doc_str += f"{fig_str}\n"
    doc_str += "\n"
with open(md_fname, mode="w", encoding="utf-8") as f:
    f.write(doc_str)
cmd = f"pandoc {md_fname} -o {pdf_fname} -V pagestyle=empty"
subprocess.run(cmd.split())
