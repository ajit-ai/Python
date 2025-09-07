# Newton's Second Law of Motion in Python Code
# Description: This script simulates Newton's Second Law, which states that the acceleration of an object is directly proportional 
# to the net force acting on it and inversely proportional to its mass (F = m * a).
# We will simulate a particle in one dimension under a constant force, showing how velocity and position change due to constant acceleration.
# Each step is described in comments, leading to the conclusion.

# Step 1: Import necessary libraries
# - numpy: For numerical computations and generating time arrays.
# - matplotlib.pyplot: For plotting position, velocity, and acceleration over time to visualize the motion.
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define initial conditions and parameters
# - Set mass (m) to 2 kg.
# - Set constant force (F) to 10 N (Newtons), applied in the positive direction.
# - Calculate acceleration (a) using F = m * a, so a = F / m.
# - Initial position (x0) = 0 m, initial velocity (v0) = 0 m/s.
# - Simulation time: total time (t_total) = 10 seconds, time step (dt) = 0.1 seconds.
m = 2.0  # Mass in kg
F = 10.0  # Constant force in Newtons
a = F / m  # Acceleration in m/s² (from F = m * a)
x0 = 0.0  # Initial position in meters
v0 = 0.0  # Initial velocity in m/s
t_total = 10.0  # Total simulation time in seconds
dt = 0.1  # Time step in seconds

# Step 3: Prepare arrays for simulation data
# - Create a time array from 0 to t_total with steps of dt.
# - Initialize lists to store position, velocity, and acceleration at each time step.
time_array = np.arange(0, t_total + dt, dt)
positions = []
velocities = []
accelerations = []

# Step 4: Simulate the motion step by step
# - Start with current position = x0, current velocity = v0, current acceleration = a (constant).
# - For each time step:
#   - Append current position, velocity, and acceleration to their lists.
#   - Update velocity: v = v + a * dt (velocity changes due to acceleration).
#   - Update position: x = x + v * dt (using updated velocity for more accuracy, but simple Euler method here).
current_x = x0
current_v = v0
current_a = a  # Acceleration is constant
for t in time_array:
    positions.append(current_x)
    velocities.append(current_v)
    accelerations.append(current_a)
    # Update velocity using a = dv/dt, so Δv = a * Δt
    current_v += current_a * dt
    # Update position using v = dx/dt, so Δx = v * Δt (using updated v for semi-implicit Euler)
    current_x += current_v * dt

# Step 5: Visualize the results
# - Plot position vs. time: Should be a parabolic curve (x = (1/2) a t² + v0 t + x0).
# - Plot velocity vs. time: Should be a straight line with slope = a (v = a t + v0).
# - Plot acceleration vs. time: Horizontal line at constant a.
plt.figure(figsize=(15, 5))

# Position plot
plt.subplot(1, 3, 1)
plt.plot(time_array, positions, label='Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs. Time')
plt.grid(True)
plt.legend()

# Velocity plot
plt.subplot(1, 3, 2)
plt.plot(time_array, velocities, label='Velocity', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs. Time')
plt.grid(True)
plt.legend()

# Acceleration plot
plt.subplot(1, 3, 3)
plt.plot(time_array, accelerations, label='Acceleration', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Acceleration vs. Time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Step 6: Conclusion
# - From the simulation:
#   - Acceleration is constant at {a:.2f} m/s², as force and mass are constant.
#   - Velocity increases linearly with time, directly due to the constant acceleration (from F = m * a).
#   - Position increases quadratically with time, as it's the integral of velocity.
# - This demonstrates Newton's Second Law: The applied force causes acceleration proportional to F/m.
# - Without force (F=0), it would reduce to the First Law (constant velocity).
# - Print final values for verification.
print(f"Final position after {t_total} seconds: {positions[-1]:.2f} m")
print(f"Final velocity: {velocities[-1]:.2f} m/s")
print(f"Constant acceleration: {a:.2f} m/s²")
print("Conclusion: Acceleration is proportional to force and inverse to mass, confirming Newton's Second Law of Motion.")