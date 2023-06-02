# predator-prey-simulation
Biological simulation
---

# Stochastic Multi-Species Simulation

This Python program simulates the dynamics of multiple interacting species in an ecosystem over time. It uses a stochastic model, which incorporates random noise to represent the inherent unpredictability of nature. 

## Features

**1. Multi-Species Interaction**: The program allows you to model multiple species in an ecosystem and define how they interact. These interactions can be positive (e.g., symbiosis), negative (e.g., predation), or neutral.

**2. Stochastic Noise**: The simulation includes a stochastic element, modeling the random fluctuations that can occur in real-world ecosystems. This is implemented as a Gaussian noise factor that is applied to the population change of each species at each time step.

**3. Parameter Validation**: The program validates the parameters of the simulation to ensure they make sense. For example, it ensures that the number of simulation steps, the noise strength, and the initial populations of the species are all non-negative.

**4. Population History Tracking**: For each species, the program keeps track of the population at each time step. This allows for the creation of a time-series plot showing the population dynamics over the course of the simulation.

**5. Visualization**: The simulation results are visualized using a matplotlib plot, which shows the population of each species as a function of time.

**6. Data Export**: The population history of each species is saved to a CSV file, allowing for further analysis or plotting in other programs.

---

Remember to replace the filename in the `save_results` function call in the `if __name__ == "__main__"` section with the desired name for your output CSV file. Also, feel free to adjust the species, their initial populations, their relationships, the number of simulation steps, and the noise strength to fit your specific needs.

To run the simulation, simply run the Python file in your preferred environment. Make sure you have numpy, pandas, and matplotlib installed, as these are required for the simulation and its output. 

This project is an excellent example of the use of Python for scientific modeling and data analysis. It is an ongoing project, and further improvements and features are planned for future versions.
