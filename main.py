from core.knapsack_problem import Item
from core.solution import evaluate_solution

from strategies.genetic_algorithm import GeneticAlgorithm

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    items = [Item(2, 3), Item(3, 4), Item(4, 5), Item(5, 6)]
    capacity = 5

    algorithms = [
        ("Genetic Algorithm", GeneticAlgorithm()),
    ] # Assim que desenvolver o algoritmo na pasta de strategy, chamar ele nesse array :D

    for name, strategy in algorithms:
        print(f"\n=== {name} ===")
        best_solution = strategy.solve(items, capacity)
        value = evaluate_solution(best_solution, items, capacity)
        print("Melhor solução:", best_solution)
        print("Valor total:", value)

if __name__ == "__main__":
    main()
