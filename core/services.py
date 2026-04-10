from core.poke_cache import PokeCache
from core.api_handler import ApiHandler

class Services():
    def __init__(self):
        cache = PokeCache()
        api_handler = ApiHandler(cache)

        self.cache = cache
        self.api_handler = api_handler