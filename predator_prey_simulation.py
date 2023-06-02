import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class StochasticMultiSpeciesSimulation:
    def __init__(self, species, relationships, steps=1000, noise_strength=0.1):
        self.species = species
        self.relationships = relationships
        self.steps = steps
        self.noise_strength = noise_strength
        self.validate_parameters()

    def validate_parameters(self):
        if self.steps < 1:
            raise ValueError("Number of steps must be greater than 0.")
        if self.noise_strength < 0:
            raise ValueError("Noise strength must be non-negative.")
        for species, data in self.species.items():
            if data['population'] < 0:
                raise ValueError(f"Initial population of {species} must be non-negative.")
            for other_species, relationship in self.relationships[species].items():
                if relationship < 0 and other_species != species:
                    raise ValueError(f"Relationship coefficient between {species} and {other_species} must be non-negative.")

    def run(self):
        for _ in range(self.steps):
            for species, data in self.species.items():
                change = 0
                for other_species, relationship in self.relationships[species].items():
                    change += relationship * self.species[other_species]['population']
                noise = np.random.normal(scale=self.noise_strength)
                data['population'] += change + noise
                data['history'].append(data['population'])

    def plot_results(self):
        plt.figure(figsize=(12, 6))
        for species, data in self.species.items():
            plt.plot(data['history'], label=species)
        plt.legend(loc='upper right')
        plt.xlabel('Time')
        plt.ylabel('Population')
        plt.title('Stochastic Multi-Species Dynamics')
        plt.show()

    def save_results(self, filename):
        df = pd.DataFrame(self.species)
        df.to_csv(filename)

if __name__ == "__main__":
    species = {
        'prey': {'population': 40, 'history': [40]},
        'predator': {'population': 9, 'history': [9]}
    }

    relationships = {
        'prey': {'prey': 1.0, 'predator': -0.1},
        'predator': {'prey': 0.075, 'predator': -1.5}
    }

    sim = StochasticMultiSpeciesSimulation(species, relationships, noise_strength=0.2)
    sim.run()
    sim.plot_results()
    sim.save_results('simulation_results.csv')
