import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_3d_model(depth_map):
    # Normalize depth values for better visualization
    z = depth_map / 255.0

    # Generate meshgrid for X and Y axes
    x = np.linspace(0, 1, depth_map.shape[1])
    y = np.linspace(0, 1, depth_map.shape[0])
    x, y = np.meshgrid(x, y)

    # Plotting 3D surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', antialiased=True)

    # Adding labels and colorbar
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Depth')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # Save the figure
    plt.savefig('static/uploads/3d_model.png')
    plt.close()

    # Calculate dimensions
    x_range = np.ptp(x)
    y_range = np.ptp(y)
    z_range = np.ptp(z)

    return x_range, y_range, z_range
