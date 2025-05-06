from strategies.base_strategy import OptimizationStrategy
from core.solution import evaluate_solution
import random

class AntColonyOptimizer(OptimizationStrategy):
    def __init__(self, num_ants=3, generations=3, alpha=1, beta=2, evaporation_rate=0.1):
        self.num_ants = num_ants 
        self.generations = generations  
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate

    def initialize_pheromone(self, num_items):
        return [1.0 for _ in range(num_items)]

    def construct_solution(self, pheromone, items, capacity):
        solution = []
        for i in range(len(items)):
            prob = pheromone[i]
            solution.append(1 if random.random() < prob else 0)
        return solution

    def solve(self, items, capacity):
        pheromone = self.initialize_pheromone(len(items))
        all_generations = []  

        for generation in range(self.generations): 
            generation_solutions = []  
            for _ in range(self.num_ants):  
                solution = self.construct_solution(pheromone, items, capacity)
                generation_solutions.append(solution)
                
                pheromone = [p * (1 - self.evaporation_rate) + (1 if bit else 0)
                             for p, bit in zip(pheromone, solution)]
            all_generations.append(generation_solutions[:3]) 

        return all_generations
