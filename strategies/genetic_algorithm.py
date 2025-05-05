from strategies.base_strategy import OptimizationStrategy
from core.solution import evaluate_solution
import random

class GeneticAlgorithm(OptimizationStrategy):
    def __init__(self, population_size=50, generations=100, mutation_rate=0.01):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def initialize_population(self, num_items):
        return [[random.randint(0, 1) for _ in range(num_items)]
                for _ in range(self.population_size)]

    def select_parents(self, population, items, capacity):
        # Seleção por torneio simples
        tournament = random.sample(population, 5)
        tournament.sort(key=lambda ind: evaluate_solution(ind, items, capacity), reverse=True)
        return tournament[0], tournament[1]

    def crossover(self, parent1, parent2):
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:]

    def mutate(self, individual):
        return [1 - gene if random.random() < self.mutation_rate else gene for gene in individual]

    def solve(self, items, capacity):
        population = self.initialize_population(len(items))

        for _ in range(self.generations):
            new_population = []
            for _ in range(self.population_size):
                p1, p2 = self.select_parents(population, items, capacity)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                new_population.append(child)
            population = new_population

        best = max(population, key=lambda ind: evaluate_solution(ind, items, capacity))
        return best
