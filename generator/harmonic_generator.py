import random


class HarmonicGenerator:

    def __init__(self, n: int) -> None:
        super().__init__()
        self.choose_from = range(1, n + 1)
        self.n = n
        self.harmonic_n = self.harmonic(self.n)
        self.weights = [1 / (k * self.harmonic_n) for k in self.choose_from]

    def gen(self, k=1):
        return random.choices(self.choose_from, self.weights, k=k)

    def harmonic(self, n):
        return sum(1 / k for k in range(1, n + 1))
