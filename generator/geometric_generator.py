import random


class GeometricGenerator:

    def __init__(self, n: int) -> None:
        super().__init__()

        self.choose_from = range(1, n + 1)
        self.n = n

        self.weights = [1 / (2 ** k) for k in range(1, n)]
        self.weights.append(1 / (2 ** (n - 1)))

    def gen(self, k=1):
        return random.choices(self.choose_from, self.weights, k=k)
