from core.ui_screen import UiScreen, ScreenEnum

class FlavorTextScreen(UiScreen):
    def __init__(self):
        self.name = ScreenEnum.FLAVOR_TEXT_SCREEN
    def handle_input(self, input_string, services, state) -> tuple[bool, str | None]:
        return (True, ScreenEnum.VERSION_SCREEN)
    def on_enter(self, services, state):
        print(f"===== [{state._version.capitalize()}]: {state._active_data.name.capitalize()} =====" 
              + "\n"
              + state._active_data.display_version(state._version)
        )