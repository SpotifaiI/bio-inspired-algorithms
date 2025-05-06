from strategies.base_strategy import OptimizationStrategy
from core.solution import evaluate_solution
import random
import math

class ParticleSwarmOptimizer(OptimizationStrategy):
    def __init__(self, items, capacity, num_particles=3, iterations=3, w=0.5, c1=1.5, c2=1.5):
        self.items = items
        self.capacity = capacity
        self.num_particles = num_particles  
        self.iterations = iterations  
        self.w = w
        self.c1 = c1
        self.c2 = c2

    def initialize_particles(self):
        particles = []
        for _ in range(self.num_particles):
            position = [random.randint(0, 1) for _ in self.items]
            velocity = [random.uniform(-1, 1) for _ in self.items]
            particles.append({
                'position': position,
                'velocity': velocity,
                'best_position': position[:],
                'best_value': evaluate_solution(position, self.items, self.capacity)
            })
        return particles

    def solve(self, items, capacity):
        particles = self.initialize_particles()
        global_best = max(particles, key=lambda p: p['best_value'])
        all_iterations = [] 

        for _ in range(self.iterations):
            iteration_solutions = []  
            for particle in particles:
                for i in range(len(particle['position'])):
                    r1, r2 = random.random(), random.random()
                    cognitive = self.c1 * r1 * (particle['best_position'][i] - particle['position'][i])
                    social = self.c2 * r2 * (global_best['best_position'][i] - particle['position'][i])
                    particle['velocity'][i] = self.w * particle['velocity'][i] + cognitive + social

                    sigmoid = 1 / (1 + math.exp(-particle['velocity'][i])) 
                    particle['position'][i] = 1 if random.random() < sigmoid else 0

                value = evaluate_solution(particle['position'], items, capacity)
                if value > particle['best_value']:
                    particle['best_value'] = value
                    particle['best_position'] = particle['position'][:]

                iteration_solutions.append(particle['position'][:])

            global_best = max(particles, key=lambda p: p['best_value'])
            all_iterations.append(iteration_solutions[:3])

        return all_iterations
