import random

from cache.cache import Cache


class RandomMarkingCache(Cache):

    def __init__(self, size: int) -> None:
        super().__init__(size)
        self.marked = {}

    def on_request(self, k):
        if len(self.cache) < self.size:
            self.marked[k] = False
        else:
            self.marked[k] = True

    def on_full(self):
        if not self.__unmarked_page_exists__():
            self.__mark_off_all__()

        unmarked_pages = [(_, marked) for (_, marked) in self.marked.items() if not marked]

        page = random.choice(unmarked_pages)
        # print("Remove {}".format(page[0]))
        self.cache.remove(page[0])
        self.marked.pop(page[0])

    def __mark_off_all__(self):
        for page in self.cache:
            self.marked[page] = False

    def __mark_off_page__(self, k):
        self.marked[k] = False

    def __mark_page__(self, k):
        self.marked[k] = True

    def __unmarked_page_exists__(self):
        return False in self.marked.values()