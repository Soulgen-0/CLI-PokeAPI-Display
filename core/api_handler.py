import requests

from core.poke_cache import PokeCache
from core.poke_data import PokeData

ENDPOINTS = {
    "species": "https://pokeapi.co/api/v2/pokemon-species/"
}


class ApiHandler():
    def __init__(self, cache: PokeCache):
        self._cache = cache
    def get_species(self, name: str) -> PokeData | None:
        if self._cache.in_cache(name):
            return self._cache.get(name)
        try:
            result = requests.get(ENDPOINTS["species"] + f"{name}/")
            if result.status_code != 200:
                raise Exception("Bad Request")
            data = result.json()
            #print(data)
            poke_data = PokeData(data)
            self._cache.add(poke_data)
            return poke_data
        except Exception as e:
            raise e
