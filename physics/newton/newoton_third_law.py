# Newton's Third Law of Motion in Python Code
# Description: This script simulates Newton's Third Law, which states that for every action, there is an equal and opposite reaction.
# In other words, if object A exerts a force on object B, then object B exerts an equal force in the opposite direction on object A.
# We will simulate two objects (e.g., two masses on a frictionless surface) pushing against each other with a constant interaction force during a "push" period.
# After the push, no force is applied, showing conservation of momentum as a consequence.
# Each step is described in comments, leading to the conclusion.

# Step 1: Import necessary libraries
# - numpy: For numerical computations and generating time arrays.
# - matplotlib.pyplot: For plotting positions, velocities, and momenta over time to visualize the interaction.
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define initial conditions and parameters
# - Set masses: m1 = 2 kg, m2 = 4 kg (different masses to show inverse proportionality).
# - Set force magnitude F = 10 N. Object 1 exerts +F on object 2 (action), object 2 exerts -F on object 1 (reaction).
# - Thus, acceleration a1 = -F / m1 (negative direction), a2 = +F / m2 (positive direction).
# - Initial positions: x1 = -1 m, x2 = 1 m (separated along a line).
# - Initial velocities: v1 = 0 m/s, v2 = 0 m/s (at rest).
# - Simulation time: total time t_total = 10 s, time step dt = 0.1 s.
# - Push duration: Apply force only for the first 2 seconds (push_time = 2 s), then force = 0.
m1 = 2.0  # Mass of object 1 in kg
m2 = 4.0  # Mass of object 2 in kg
F_mag = 10.0  # Magnitude of the interaction force in Newtons
x1_0 = -1.0  # Initial position of object 1 in meters
x2_0 = 1.0   # Initial position of object 2 in meters
v1_0 = 0.0   # Initial velocity of object 1 in m/s
v2_0 = 0.0   # Initial velocity of object 2 in m/s
t_total = 10.0  # Total simulation time in seconds
dt = 0.1  # Time step in seconds
push_time = 2.0  # Duration to apply the force in seconds

# Step 3: Prepare arrays for simulation data
# - Create a time array from 0 to t_total with steps of dt.
# - Initialize lists to store positions, velocities for both objects, and total momentum.
time_array = np.arange(0, t_total + dt, dt)
positions1 = []  # Positions of object 1
positions2 = []  # Positions of object 2
velocities1 = []  # Velocities of object 1
velocities2 = []  # Velocities of object 2
momenta = []  # Total momentum (m1*v1 + m2*v2)

# Step 4: Simulate the motion step by step
# - Start with current positions x1, x2 and velocities v1, v2.
# - For each time step:
#   - Calculate current force: If t <= push_time, F1 = -F_mag (on object 1), F2 = +F_mag (on object 2); else 0.
#   - Calculate accelerations: a1 = F1 / m1, a2 = F2 / m2.
#   - Append current positions, velocities, and total momentum to lists.
#   - Update velocities: v1 += a1 * dt, v2 += a2 * dt.
#   - Update positions: x1 += v1 * dt, x2 += v2 * dt (using updated velocities for semi-implicit Euler).
current_x1 = x1_0
current_x2 = x2_0
current_v1 = v1_0
current_v2 = v2_0
for t in time_array:
    # Determine current forces based on time
    if t <= push_time:
        F1 = -F_mag  # Force on object 1 (reaction)
        F2 = F_mag   # Force on object 2 (action)
    else:
        F1 = 0.0
        F2 = 0.0
    
    # Calculate accelerations
    a1 = F1 / m1
    a2 = F2 / m2
    
    # Store current states
    positions1.append(current_x1)
    positions2.append(current_x2)
    velocities1.append(current_v1)
    velocities2.append(current_v2)
    momenta.append(m1 * current_v1 + m2 * current_v2)
    
    # Update velocities
    current_v1 += a1 * dt
    current_v2 += a2 * dt
    
    # Update positions
    current_x1 += current_v1 * dt
    current_x2 += current_v2 * dt

# Step 5: Visualize the results
# - Plot positions vs. time for both objects: They should diverge during push and continue linearly after.
# - Plot velocities vs. time: Change linearly during push (due to constant a), then constant.
# - Plot total momentum vs. time: Should remain constant (0), demonstrating conservation as a result of the third law.
plt.figure(figsize=(15, 5))

# Positions plot
plt.subplot(1, 3, 1)
plt.plot(time_array, positions1, label='Position Object 1')
plt.plot(time_array, positions2, label='Position Object 2', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Positions vs. Time')
plt.grid(True)
plt.legend()

# Velocities plot
plt.subplot(1, 3, 2)
plt.plot(time_array, velocities1, label='Velocity Object 1')
plt.plot(time_array, velocities2, label='Velocity Object 2', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocities vs. Time')
plt.grid(True)
plt.legend()

# Momentum plot
plt.subplot(1, 3, 3)
plt.plot(time_array, momenta, label='Total Momentum', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Momentum (kg m/s)')
plt.title('Total Momentum vs. Time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Step 6: Conclusion
# - From the simulation:
#   - During the push (first 2 seconds), forces are equal in magnitude (10 N) but opposite in direction.
#   - Accelerations are a1 = -F/m1 = -5 m/s², a2 = F/m2 = 2.5 m/s² (inverse to masses).
#   - Velocities change accordingly: Object 1 gains negative velocity, Object 2 positive, with magnitudes such that m1*|v1| = m2*|v2|.
#   - After push, velocities remain constant (no force), positions change linearly.
#   - Total momentum remains zero throughout, conserved because internal forces cancel out (action-reaction pairs).
# - This demonstrates Newton's Third Law: The interaction forces are equal and opposite, leading to opposite accelerations proportional to 1/mass.
# - In isolated systems, this results in conservation of momentum.
# - Print final values for verification.
print(f"Final position of Object 1: {positions1[-1]:.2f} m")
print(f"Final position of Object 2: {positions2[-1]:.2f} m")
print(f"Final velocity of Object 1: {velocities1[-1]:.2f} m/s")
print(f"Final velocity of Object 2: {velocities2[-1]:.2f} m/s")
print(f"Final total momentum: {momenta[-1]:.2f} kg m/s (should be ~0)")
print("Conclusion: Action and reaction forces are equal and opposite, confirming Newton's Third Law of Motion and leading to momentum conservation.")