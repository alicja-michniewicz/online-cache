from abc import ABC, abstractmethod


class Cache(ABC):

    def __init__(self, size: int) -> None:
        super().__init__()

        self.size = size
        self.costs = []
        self.cache = []

    def request(self, k: int):
        self.on_request(k)
        # print("Requested {} on cache {}".format(k, self.cache))

        if k in self.cache:
            self.costs.append(0)
        else:
            self.costs.append(1)
            self.__insert__(k)


    def __insert__(self, k: int):
        if len(self.cache) >= self.size:
            self.on_full()

        self.cache.append(k)


    @abstractmethod
    def on_full(self):
        pass

    @abstractmethod
    def on_request(self, k):
        pass

