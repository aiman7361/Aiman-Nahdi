import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi C_L dan turunannya
def C_L(AR):
    return AR**2  # Misalkan C_L adalah fungsi kuadrat dari AR

def dC_L(AR):
    return 2 * AR  # Turunan dari C_L

# Metode Newton-Raphson
def newton_raphson(initial_guess, tolerance):
    AR = initial_guess
    error = float('inf')
    
    while error > tolerance:
        f_value = C_L(AR)
        f_derivative = dC_L(AR)
        
        AR_new = AR - f_value / f_derivative
        error = abs(AR_new - AR)
        AR = AR_new
    
    return AR

# Parameter
initial_guess = 5
tolerance = 0.001

# Mencari nilai optimal dari AR
optimal_AR = newton_raphson(initial_guess, tolerance)
print(f'Optimal Aspect Ratio (AR): {optimal_AR}')

# Plotting C_L vs AR
AR_values = np.linspace(0, 10, 100)
C_L_values = C_L(AR_values)

plt.figure(figsize=(10, 6))
plt.plot(AR_values, C_L_values, label='C_L(AR) = AR^2')
plt.axvline(optimal_AR, color='r', linestyle='--', label=f'Optimal AR = {optimal_AR:.2f}')
plt.title('Koefisien Gaya Angkat C_L vs Rasio Aspek Sayap AR')
plt.xlabel('Rasio Aspek Sayap (AR)')
plt.ylabel('Koefisien Gaya Angkat (C_L)')
plt.legend()
plt.grid()
plt.show()