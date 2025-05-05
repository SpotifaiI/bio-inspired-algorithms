from abc import ABC, abstractmethod

class OptimizationStrategy(ABC):
    @abstractmethod
    def solve(self, items, capacity):
        pass
