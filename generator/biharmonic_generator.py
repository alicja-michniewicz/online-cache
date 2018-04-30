import random


class BiharmonicGenerator:

    def __init__(self, n: int) -> None:
        super().__init__()
        self.choose_from = range(1, n + 1)
        self.n = len(self.choose_from)
        self.biharmonic_n = self.biharmonic(self.n)
        self.weights = [1 / (k ** 2 * self.biharmonic_n) for k in self.choose_from]

    def gen(self, k=1):
        return random.choices(self.choose_from, self.weights, k=k)

    def biharmonic(self, n):
        return sum(1 / k ** 2 for k in range(1, n + 1))
