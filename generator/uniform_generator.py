import random


class UniformGenerator:

    def __init__(self, n: int) -> None:
        super().__init__()
        self.choose_from = range(1, n + 1)
        self.n = n
        self.weights = [1 / n for _ in self.choose_from]

    def gen(self, k=1):
        return random.choices(self.choose_from, self.weights, k=k)
