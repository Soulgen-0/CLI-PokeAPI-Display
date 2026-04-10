from core.state import State
from core.services import Services
from core.screen_manager import ScreenManager

from core.ui_screen import ScreenEnum

from core.utils.clear_console import clear_console

POKE_API_SPECIES_ENDPOINT = "https://pokeapi.co/api/v2/pokemon-species/"

state = State()
services = Services()
manager = ScreenManager()

clear_console()
manager._screens[ScreenEnum.QUERY_SCREEN].on_enter(services, state)
if __name__ == "__main__":
    while True:
        result = input("\n").lower()
        manager.execute(result, services, state)