import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

U = -1 - X**2 + Y
V = 1 + X - Y**2

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

scalar_line = Z[50, :]
axs[0, 0].plot(x, scalar_line, label='Scalar Value along y=0', color='b')
axs[0, 0].set_title('Scalar Field (Line Chart)')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Scalar Value')
axs[0, 0].legend()

axs[0, 1].streamplot(X, Y, U, V, color='r')
axs[0, 1].set_title('Vector Field (Stream Plot)')
axs[0, 1].set_xlabel('X-axis')
axs[0, 1].set_ylabel('Y-axis')

axs[1, 0].hist(Z.flatten(), bins=30, color='g', edgecolor='black')
axs[1, 0].set_title('Histogram of Scalar Values (Z)')
axs[1, 0].set_xlabel('Scalar Value')
axs[1, 0].set_ylabel('Frequency')

axs[1, 1].quiver(X, Y, U, V, color='b')
axs[1, 1].set_title('Vector Field (Quiver Plot)')
axs[1, 1].set_xlabel('X-axis')
axs[1, 1].set_ylabel('Y-axis')

plt.tight_layout()
plt.show()