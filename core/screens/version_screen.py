from core.ui_screen import UiScreen, ScreenEnum

class VersionScreen(UiScreen):
    def __init__(self):
        self.name = ScreenEnum.VERSION_SCREEN
    def handle_input(self, input_string, services, state) -> tuple[bool, str | None]:
        if not input_string:
            return (True, ScreenEnum.QUERY_SCREEN)
        flavor_text = state._active_data.display_version(input_string)
        if flavor_text is None:
            state._error = f"'{input_string}' is not a valid version!"
            return (True, ScreenEnum.ERROR_SCREEN)
        state._version = input_string
        return (True, ScreenEnum.FLAVOR_TEXT_SCREEN)
    def on_enter(self, services, state):
        print(f"===== {state._active_data.name.capitalize()} =====\n\n" 
              + state._active_data.get_versions()
        )