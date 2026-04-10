from core.screens.version_screen import VersionScreen
from core.screens.query_screen import QueryScreen
from core.screens.flavor_text_screen import FlavorTextScreen
from core.screens.error_screen import ErrorScreen

from core.services import Services
from core.state import State

from core.utils.clear_console import clear_console
from core.ui_screen import UiScreen, ScreenEnum

class ScreenManager():
    def __init__(self):
        self._screens: dict[str, UiScreen] = {
            ScreenEnum.VERSION_SCREEN: VersionScreen(),
            ScreenEnum.QUERY_SCREEN: QueryScreen(),
            ScreenEnum.FLAVOR_TEXT_SCREEN: FlavorTextScreen(),
            ScreenEnum.ERROR_SCREEN: ErrorScreen()
        }
        self._current_screen: str = ScreenEnum.QUERY_SCREEN
    def execute(self, input: str, services: Services, state: State):
        screen: UiScreen | None = self._screens[self._current_screen]
        if not screen:
            raise Exception(f"No screen found by name '{self._current_screen}'")
        should_change_screen, next_screen = screen.handle_input(input, services, state)

        if not should_change_screen:
            return
        elif should_change_screen and next_screen is None:
            raise Exception(f"Somehow got told to switch screens with no given screen name.\nActive Screen: {self._current_screen}")
        elif not self._screens.get(next_screen):
            raise Exception(f"Screen '{next_screen}' does not exist. Cannot switch screens.")

        state._last_screen = self._current_screen
        self._current_screen = next_screen
        clear_console()
        self._screens[next_screen].on_enter(services, state)