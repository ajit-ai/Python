# Newton's First Law of Motion in Python Code
# Description: This script simulates Newton's First Law (Law of Inertia), which states that an object at rest remains at rest, 
# and an object in motion continues in uniform motion in a straight line unless acted upon by an external force.
# We will simulate a particle moving in one dimension with constant velocity (no external forces).
# Each step is described in comments, leading to the conclusion.

# Step 1: Import necessary libraries
# - time: Not used here, but could be for real-time simulation.
# - matplotlib.pyplot: For plotting the position over time to visualize the motion.
# - numpy: For efficient numerical computations, like generating time arrays.
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define initial conditions
# - Set initial position (x0) to 0 meters.
# - Set initial velocity (v0) to 5 m/s (positive for rightward motion).
# - Since no force, acceleration (a) is 0 m/s².
# - Define time parameters: simulation duration (t_total) and time step (dt).
x0 = 0.0  # Initial position in meters
v0 = 5.0  # Initial velocity in m/s
a = 0.0   # Acceleration (no force, so 0)
t_total = 10.0  # Total simulation time in seconds
dt = 0.1  # Time step in seconds

# Step 3: Prepare arrays for simulation data
# - Create a time array from 0 to t_total with steps of dt.
# - Initialize lists to store position and velocity at each time step.
time_array = np.arange(0, t_total + dt, dt)
positions = []
velocities = []

# Step 4: Simulate the motion step by step
# - Start with current position = x0, current velocity = v0.
# - For each time step:
#   - Append current position and velocity to their lists.
#   - Update position: x = x + v * dt (since a=0, v remains constant).
#   - Velocity remains constant (no update needed for v).
current_x = x0
current_v = v0
for t in time_array:
    positions.append(current_x)
    velocities.append(current_v)
    # Update position using kinematic equation: Δx = v * Δt (a=0)
    current_x += current_v * dt
    # Velocity unchanged: current_v += a * dt  (but a=0, so no change)

# Step 5: Visualize the results
# - Plot position vs. time: Should be a straight line with slope = velocity.
# - Plot velocity vs. time: Should be a horizontal line (constant velocity).
plt.figure(figsize=(10, 5))

# Position plot
plt.subplot(1, 2, 1)
plt.plot(time_array, positions, label='Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs. Time')
plt.grid(True)
plt.legend()

# Velocity plot
plt.subplot(1, 2, 2)
plt.plot(time_array, velocities, label='Velocity', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs. Time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Step 6: Conclusion
# - From the simulation:
#   - Position increases linearly with time, indicating constant velocity.
#   - Velocity remains constant at 5 m/s throughout, as no external force acts on the object.
# - This demonstrates Newton's First Law: The object continues in uniform motion because acceleration is zero.
# - If we were to add a force (non-zero a), velocity would change, violating the law without external influence.
# - Print the final position and velocity for verification.
print(f"Final position after {t_total} seconds: {positions[-1]:.2f} m")
print(f"Final velocity: {velocities[-1]:.2f} m/s")
print("Conclusion: Velocity is constant, confirming Newton's First Law of Motion.")
