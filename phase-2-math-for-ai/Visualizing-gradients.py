import numpy as np
import matplotlib.pyplot as plt

# 1. Define the function (e.g., f(x,y) = x^2 + 3y^2)
def f(x, y):
    return x**2 + y**2

# 2. Generate a grid
x_range = np.linspace(-3, 3, 15)
y_range = np.linspace(-3, 3, 15)
X, Y = np.meshgrid(x_range, y_range)

# 3. Calculate the partial derivatives
# ∂f/∂x = 2x
# ∂f/∂y = 6y

# 4. Compute gradient components
U = 2 * X  # x-component of the gradient
V = 6 * Y  # y-component of the gradient

# 5. Plot the gradient field
plt.figure(figsize=(7, 7))
plt.quiver(X, Y, U, V, color='r', angles='xy', scale_units='xy', scale=1.5)

# Optional: Add contour lines of the original function for context
Z = f(X, Y)
plt.contour(X, Y, Z, levels=10, colors='blue', alpha=0.5)

# 6. Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Field of f(x,y) = x² + 3y²')
plt.grid(True)

# 7. Display the plot
plt.show()