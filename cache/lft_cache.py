from cache.cache import Cache


class LeastFrequentlyUsedCache(Cache):

    def __init__(self, size: int) -> None:
        super().__init__(size)
        self.frequency = {}

    def on_request(self, k):
        if k in self.frequency.keys() :
            self.frequency[k] += 1
        else:
            self.frequency[k] = 1

    def on_full(self):
        cache_frequency = [(page, frequency) for (page, frequency) in self.frequency.items() if page in self.cache]
        lfu_page_tuple = min(cache_frequency, key = lambda x: x[1])
        self.cache.remove(lfu_page_tuple[0])