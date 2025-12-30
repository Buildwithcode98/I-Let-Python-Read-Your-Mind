import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup
num_particles = 500
positions = np.random.rand(num_particles, 2) * 10  # random start
targets = positions.copy()  # will change per structure

fig, ax = plt.subplots()
scat = ax.scatter(positions[:,0], positions[:,1], c='cyan', s=10)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor("black")

# Function to assign targets in a circle
def form_circle(radius=4):
    cx, cy = 5, 5
    angles = np.linspace(0, 2*np.pi, num_particles)
    targets[:,0] = cx + radius * np.cos(angles)
    targets[:,1] = cy + radius * np.sin(angles)

# Function to assign targets in a spiral
def form_spiral():
    cx, cy = 5, 5
    angles = np.linspace(0, 10*np.pi, num_particles)
    r = np.linspace(0.1, 4, num_particles)
    targets[:,0] = cx + r * np.cos(angles)
    targets[:,1] = cy + r * np.sin(angles)

# Function to assign targets in a line
def form_line():
    x = np.linspace(2, 8, num_particles)
    y = np.linspace(2, 8, num_particles)
    targets[:,0] = x
    targets[:,1] = y

# Start with circle
form_circle()

# Update function
def update(frame):
    global positions
    # Smoothly move particles toward targets
    positions += (targets - positions) * 0.05
    scat.set_offsets(positions)
    return scat,

ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)
plt.show()



