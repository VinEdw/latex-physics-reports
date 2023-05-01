import math

emf = 15
R_1 = 10
R_2 = 20
R_3 = 30
C = 4

def V(t):
    C_eq = C
    R_eq = R_3 + (R_1**-1 + R_2**-1)**-1
    tau = R_eq * C_eq
    Q_max = C * (emf / (R_1 + R_2) * R_2)
    q = Q_max * (1 - math.exp(-t / tau))
    return q / C

time = float(input("Input a t value in seconds\n>>> ").strip())
print(f"V = {V(time)} V")
