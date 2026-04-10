from abc import ABC, abstractmethod
from core.services import Services
from core.state import State

class ScreenEnum():
    VERSION_SCREEN = "version_screen"
    FLAVOR_TEXT_SCREEN = "flavor_text_screen"
    QUERY_SCREEN = "query_screen"
    ERROR_SCREEN = "error_screen"

class UiScreen(ABC):
    name: str

    @abstractmethod
    def handle_input(self, input_string: str, services: Services, state: State) -> tuple[bool, str | None]:
        pass
    @abstractmethod
    def on_enter(self, services: Services, state: State) -> None:
        pass
