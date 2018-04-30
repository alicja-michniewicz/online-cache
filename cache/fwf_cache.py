from cache.cache import Cache


class FlushWhenFullCache(Cache):

    def on_request(self, k):
        pass

    def __init__(self, size: int) -> None:
        super().__init__(size)

    # remove all pages
    def on_full(self):
        self.cache.clear()
