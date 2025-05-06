from strategies.base_strategy import OptimizationStrategy
from core.solution import evaluate_solution
import random

class CuckooSearch(OptimizationStrategy):
    def __init__(self, num_nests=3, generations=3, pa=0.25, alpha=1.0):
        self.num_nests = num_nests  
        self.generations = generations 
        self.pa = pa  
        self.alpha = alpha  

    def initialize_nests(self, num_items):
        return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(self.num_nests)]

    def generate_new_solution(self, nest, best_nest):
        new_solution = []
        for i in range(len(nest)):
            new_value = nest[i] + self.alpha * (random.random() - 0.5)
            new_solution.append(1 if new_value > 0.5 else 0)
        return new_solution

    def solve(self, items, capacity):
        nests = self.initialize_nests(len(items))  
        all_generations = [] 

        for generation in range(self.generations):
            fitness_values = [evaluate_solution(nest, items, capacity) for nest in nests]
            best_nest_index = fitness_values.index(max(fitness_values)) 
            best_nest = nests[best_nest_index]

            generation_solutions = [] 

            for i in range(self.num_nests):
                if random.random() < self.pa:
                    new_solution = self.generate_new_solution(nests[i], best_nest)
                    nests[i] = new_solution

                generation_solutions.append(nests[i])

            all_generations.append(generation_solutions[:3]) 

        return all_generations
