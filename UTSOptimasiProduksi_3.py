import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi performa P dan gradiennya
def P(x1, x2):
    return - (x1 - 10)**2 - (x2 - 5)**2 + 50  # Fungsi performa yang diberikan

def gradient(x1, x2):
    grad_x1 = -2 * (x1 - 10)  # Turunan terhadap x1
    grad_x2 = -2 * (x2 - 5)   # Turunan terhadap x2
    return np.array([grad_x1, grad_x2])

# Metode Gradient Descent
def gradient_descent(initial_x, learning_rate, tolerance):
    x = np.array(initial_x)
    history = [P(x[0], x[1])]  # Menyimpan nilai performa
    
    error = float('inf')
    
    while error > tolerance:
        grad = gradient(x[0], x[1])
        x_new = x - learning_rate * grad
        error = np.linalg.norm(x_new - x)  # Menghitung error
        x = x_new
        history.append(P(x[0], x[1]))  # Menyimpan nilai performa
    
    return x, history

# Parameter
initial_x = [8, 4]
learning_rate = 0.1
tolerance = 0.001

# Mencari nilai optimal dari x1 dan x2
optimal_values, history = gradient_descent(initial_x, learning_rate, tolerance)
print(f'Optimal Length of Wing (x1): {optimal_values[0]:.2f}')
print(f'Optimal Angle of Attack (x2): {optimal_values[1]:.2f}')

# Plotting performa seiring iterasi
plt.figure(figsize=(12, 7))
plt.plot(history, linestyle='--', marker='s', color='orange', markersize=8, linewidth=2)
plt.title('Performa Aerodinamis vs Iterasi', fontsize=16)
plt.xlabel('Iterasi', fontsize=14)
plt.ylabel('Performa P(x1, x2)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.axhline(y=history[0], color='red', linestyle='--', label='Initial Performance')
plt.axhline(y=history[-1], color='green', linestyle='--', label='Optimal Performance')
plt.legend()
plt.tight_layout()
plt.show()
