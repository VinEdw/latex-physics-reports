import math

# Given
P_1 = 2.00e5
V_1 = 2.50E-3
T_1 = 300
Q_H = 500
Q_2_3 = Q_H
V_2 = V_1 / 8
R = 8.31
C_V = 5/2 * R
C_P = 7/2 * R
gamma = 1.40

# Moles
n = P_1 * V_1 / (R * T_1)

# P, V, and T
# Point 2
P_2 = P_1 * (V_1 / V_2)**gamma
T_2 = P_2 * V_2 / (n * R)
# Point 3
P_3 = P_2
T_3 = Q_2_3 / (n * C_P) + T_2
V_3 = n * R * T_3 / P_3
# Point 4
V_4 = V_1
P_4 = P_3 * (V_3 / V_4)**gamma
T_4 = P_4 * V_4 / (n * R)

# Process Variables
# 1 -> 2
Q_1_2 = 0
Delta_U_1_2 = n * C_V * (T_2 - T_1)
W_1_2 = -Delta_U_1_2
Delta_S_1_2 = 0
# 2 -> 3
Delta_U_2_3 = n * C_V * (T_3 - T_2)
W_2_3 = P_2 * (V_3 - V_2)
Delta_S_2_3 = n * C_P * math.log(T_3 / T_2)
# 3 -> 4
Q_3_4 = 0
Delta_U_3_4 = n * C_V * (T_4 - T_3)
W_3_4 = -Delta_U_3_4
Delta_S_3_4 = 0
# 4 -> 1
W_4_1 = 0
Delta_U_4_1 = n * C_V * (T_1 - T_4)
Q_4_1 = Delta_U_4_1
Delta_S_4_1 = n * C_V * math.log(T_1 / T_4)
# Total
Q_tot = Q_1_2 + Q_2_3 + Q_3_4 + Q_4_1
W_tot = W_1_2 + W_2_3 + W_3_4 + W_4_1
Delta_U_tot = Delta_U_1_2 + Delta_U_2_3 + Delta_U_3_4 + Delta_U_4_1
Delta_S_tot = Delta_S_1_2 + Delta_S_2_3 + Delta_S_3_4 + Delta_S_4_1

# Efficiency
e = W_tot / Q_H
