import math

P = dict()
V = dict()
T = dict()
Delta_U = dict()
Q = dict()
W = dict()
Delta_S = dict()

# Given
P[1] = 1.00E5
P[2] = 8.00E5
V[1] = 1.00E-3
T[1] = 290
T[3] = 1300
R = 8.31
C_V = 5 / 2 * R
C_P = 7 / 2 * R
gamma = 1.40

# Moles
n = P[1] * V[1] / (R * T[1])

# P, V, and T
# Point 2
V[2] = V[1] * (P[1] / P[2])**(1 / gamma)
T[2] = P[2] * V[2] / (n * R)
# Point 3
P[3] = P[2]
V[3] = n * R * T[3] / P[3]
# Point 4
P[4] = P[1]
V[4] = V[3] * (P[3] / P[4])**(1 / gamma)
T[4] = P[4] * V[4] / (n * R)

# Process Variables
# 1 -> 2
Q[1, 2] = 0
Delta_U[1, 2] = n * C_V * (T[2] - T[1])
W[1, 2] = -Delta_U[1, 2]
Delta_S[1, 2] = 0
# 2 -> 3
Delta_U[2, 3] = n * C_V * (T[3] - T[2])
Q[2, 3] = n * C_P * (T[3] - T[2])
W[2, 3] = P[2] * (V[3] - V[2])
Delta_S[2, 3] = n * C_P * math.log(T[3] / T[2])
# 3 -> 4
Q[3, 4] = 0
Delta_U[3, 4] = n * C_V * (T[4] - T[3])
W[3, 4] = -Delta_U[3, 4]
Delta_S[3, 4] = 0
# 4 -> 1
Delta_U[4, 1] = n * C_V * (T[1] - T[4])
Q[4, 1] = n * C_P * (T[1] - T[4])
W[4, 1] = P[4] * (V[1] - V[4])
Delta_S[4, 1] = n * C_P * math.log(T[1] / T[4])

# Totals
Delta_U_tot = sum(Delta_U.values())
Q_tot = sum(Q.values())
W_tot = sum(W.values())
Delta_S_tot = sum(Delta_S.values())

# Efficiency
Q_H = sum(val for val in Q.values() if val > 0)
e = W_tot / Q_H
