import matplotlib.pyplot as plt
import numpy as np

# Define the system parameters
alpha = 1.0  # birth rate of prey
beta = 0.1  # death rate of prey due to predation
gamma = 1.5  # natural death rate of predators
delta = 0.075  # rate at which predators increase due to predation

# Initialize the populations
prey_population = 40
predator_population = 9

# Initialize lists to store population sizes at each time step
prey_populations = [prey_population]
predator_populations = [predator_population]

# Define the number of time steps
num_steps = 1000

# Run the simulation
for _ in range(num_steps):
    new_prey_population = prey_population + (alpha*prey_population - beta*prey_population*predator_population)
    new_predator_population = predator_population + (delta*prey_population*predator_population - gamma*predator_population)

    prey_populations.append(new_prey_population)
    predator_populations.append(new_predator_population)

    prey_population, predator_population = new_prey_population, new_predator_population

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(prey_populations, label='Prey')
plt.plot(predator_populations, label='Predator')
plt.legend(loc='upper right')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Predator-Prey Dynamics')
plt.show()
