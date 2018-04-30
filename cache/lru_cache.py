from cache.cache import Cache


class LeastRecentlyUsedCache(Cache):

    def __init__(self, size: int) -> None:
        super().__init__(size)
        self.when_used = {}
        self.request_counter = 0

    def on_request(self, k):
        self.request_counter += 1

        self.when_used[k] = self.request_counter

    def on_full(self):
        # print(self.when_used)
        lru_page = min(self.when_used, key=self.when_used.get)
        # print("LRU PAGE {}".format(lru_page))
        # print("cache {}".format(self.cache))
        self.cache.remove(lru_page)
        self.when_used.pop(lru_page)