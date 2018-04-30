import random

from cache.cache import Cache


class RandomCache(Cache):

    def on_request(self, k):
        pass

    def __init__(self, size: int) -> None:
        super().__init__(size)

    # remove random page
    def on_full(self):
        page = random.choice(self.cache)
        self.cache.remove(page)
