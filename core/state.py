from core.poke_data import PokeData

class State():
    def __init__(self):
        self._active_data: PokeData | None = None
        self._version: str | None = None
        self._last_screen: str | None = None
        self._error: any | None = None
    def set_active_data(self, data: PokeData | None):
        self._active_data = data