import numpy as np
import pandas as pd

R_2 = 40

class Circuit:
    def __init__(self, name: str):
        self.name = name
        self.V = {}
        self.I = {}
        self.R = {}
    
    @property
    def keys(self) -> set:
        """
        Return the list of keys that have been set for the circuit elements.
        """
        keys = set()
        keys = keys.union(self.V.keys())
        keys = keys.union(self.R.keys())
        return keys

    @property
    def P(self) -> dict:
        """
        Return the dictionary of power values for each circuit element.
        """
        P = {}
        for key in self.keys:
            V = self.V.get(key, np.nan)
            I = self.I.get(key, np.nan)
            P[key] = abs(V * I)
        return P

    def set_currents_equal(self, initial_key: int|str, new_keys: list) -> None:
        """
        Set the currents in the list of new keys equal to the current for the initial key.
        """
        I_initial = self.I[initial_key]
        for key in new_keys:
            self.I[key] = I_initial
    
    def calculate_resistor_voltages(self) -> None:
        """
        Calculate the voltage across each resistor based on current and resistance.
        """
        for key, R in self.R.items():
            I = self.I.get(key, np.nan)
            self.V[key] = I * R
    
    def describe(self) -> str:
        result_str = f"{self.name}\n"
        df = pd.DataFrame({
            "V": self.V,
            "I": self.I,
            "P": self.P,
        })
        # "E_i" keys are used for the voltage sources; change their print index "Ɛ_i"
        for i in df.index:
            if str(i).startswith("E"):
                df = df.rename(index={i: str(i).replace("E", "Ɛ")})
        # "i" keys are used for the resistors; change their print index to "R_i"
        for i in self.R:
            df = df.rename(index={i: f"R_{i}"})
        # Append the df string with float values rounded to three sig figs
        result_str += df.to_string(float_format="%.3g")
        # Append an extra newline at the end
        result_str += "\n"
        return result_str

# ==================== Circuit 1 ====================
# Givens
cir_1 = Circuit("Circuit 1")
cir_1.R[1] = 110
cir_1.R[2] = R_2
cir_1.R[3] = 45
cir_1.R[4] = 78
cir_1.V["E_1"] = 12

# L_1:
# E_1 - I_1 R_1 - I_1 R_2 - I_1 R_3 - I_1 R_4 = 0
# I_1 = E_1 / (R_1 + R_2 + R_3 + R_4)
cir_1.I[1] = cir_1.V["E_1"] / sum(cir_1.R.values())
cir_1.set_currents_equal(1, [2, 3, 4, "E_1"])
cir_1.calculate_resistor_voltages()
print(cir_1.describe())

# ==================== Circuit 2 ====================
# Givens
cir_2 = Circuit("Circuit 2")
cir_2.R[1] = 85
cir_2.R[2] = R_2
cir_2.R[3] = 125
cir_2.V["E_1"] = 9

# J_1:
# I_E_1 = I_1 + I_2 + I_3
# I_1 + I_2 + I_3 - I_E_1 = 0

# L_1:
# E_1 - I_1 R_1 = 0
# I_1 R_1 = E_1

# L_2:
# E_1 - I_2 R_2 = 0
# I_2 R_2 = E_1

# L_3:
# E_1 - I_3 R_3 = 0
# I_3 R_3 = E_1

cir_2_matrix = np.array([
    [1, 1, 1, -1],
    [cir_2.R[1], 0, 0, 0],
    [0, cir_2.R[2], 0, 0],
    [0, 0, cir_2.R[3], 0],
])
cir_2.I[1], cir_2.I[2], cir_2.I[3], cir_2.I["E_1"] = np.linalg.solve(
    cir_2_matrix,
    [0, cir_2.V["E_1"], cir_2.V["E_1"], cir_2.V["E_1"]]
)
cir_2.calculate_resistor_voltages()
print(cir_2.describe())
