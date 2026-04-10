from core.ui_screen import UiScreen, ScreenEnum

class ErrorScreen(UiScreen):
    def __init__(self):
        self.name = ScreenEnum.ERROR_SCREEN
    def handle_input(self, input_string, services, state) -> tuple[bool, str | None]:
        state._error = None
        return (True, state._last_screen)
    def on_enter(self, services, state):
        print(state._error)