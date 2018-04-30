from cache.cache import Cache


class FifoCache(Cache):

    def on_request(self, k):
        pass

    def __init__(self, size: int) -> None:
        super().__init__(size)

    # remove first page
    def on_full(self):
        self.cache.remove(self.cache[0])
