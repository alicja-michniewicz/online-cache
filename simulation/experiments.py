from cache.cache import Cache
from cache.fifo_cache import FifoCache
from cache.fwf_cache import FlushWhenFullCache
from cache.lft_cache import LeastFrequentlyUsedCache
from cache.lru_cache import LeastRecentlyUsedCache
from cache.random_cache import RandomCache
from cache.random_marking_cache import RandomMarkingCache
from generator.biharmonic_generator import BiharmonicGenerator
from generator.geometric_generator import GeometricGenerator
from generator.harmonic_generator import HarmonicGenerator
from generator.uniform_generator import UniformGenerator
import numpy as np

trials = 100


def simulate_requests(sequence: [int], cache: Cache):
    # print("Pages {}".format(sequence))

    for page in sequence:
        cache.request(page)

    # print("Costs {}".format(cache.costs))
    return sum(cache.costs) / len(sequence)


def experiment_series(caches, ns, gens):
    for gen in gens:
        print(gen.__name__)

        for cache in caches:
            print(cache.__name__)
            for n in ns:
                k_avg_results = []
                current_gen = gen(n)
                n_results = []

                for k in range(int(n / 10), int(n / 5) + 1):
                    k_results = []
                    for _ in range(trials):
                        # print("Cache {}, {} / {}".format(cache.__name__, k, n))
                        current_cache = cache(k)
                        sequence = current_gen.gen(n)

                        k_results.append(simulate_requests(sequence, current_cache))

                    mean = np.array(k_results).mean()
                    k_avg_results.append(mean)

                n_results.append(k_avg_results)
                print(n_results)


cache_types = [FifoCache, RandomCache, FlushWhenFullCache, LeastFrequentlyUsedCache, LeastRecentlyUsedCache,
               RandomMarkingCache]
gens = [UniformGenerator, GeometricGenerator, HarmonicGenerator, BiharmonicGenerator]
ns = [20, 30, 40, 50, 60, 70, 80, 90, 100]

experiment_series(cache_types, ns, gens)
