from core.poke_data import PokeData

class PokeCache():
    def __init__(self):
        self._cache = {}
    def add(self, poke_data: PokeData):
        self._cache[poke_data.name] = poke_data
    def in_cache(self, name: str):
        return name in self._cache
    def get(self, name: str):
        return self._cache.get(name)
