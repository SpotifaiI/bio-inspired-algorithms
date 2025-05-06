from core.knapsack_problem import Item
from core.solution import evaluate_solution

from strategies.genetic_algorithm import GeneticAlgorithm
from strategies.ant_colony import AntColonyOptimizer
from strategies.particle_swarm_optimization import ParticleSwarmOptimizer
from strategies.cuckoo_search import CuckooSearch  

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    items = [Item(2, 3), Item(3, 4), Item(4, 5), Item(5, 6)]
    capacity = 5

    algorithms = [
        ("Genetic Algorithm", GeneticAlgorithm(population_size=50, generations=3, mutation_rate=0.01)),
        ("Ant Colony Optimization", AntColonyOptimizer(num_ants=3, generations=3)),  
        ("Particle Swarm Optimization", ParticleSwarmOptimizer(items, capacity, num_particles=3, iterations=3)), 
        ("Cuckoo Search", CuckooSearch(num_nests=3, generations=3)), 
    ]

    for name, strategy in algorithms:
        print(f"\n=== {name} ===")
        all_solutions = strategy.solve(items, capacity)

        if all_solutions is None:
            print(f"Erro: 'solve' não retornou soluções para {name}.")
            continue

        for generation, solutions in enumerate(all_solutions):
            print(f"\nGeração {generation + 1}:")
            for i, solution in enumerate(solutions[:3]):
                value = evaluate_solution(solution, items, capacity)
                print(f"  Solução {i + 1}: {solution} | Valor total: {value}")


if __name__ == "__main__":
    main()
