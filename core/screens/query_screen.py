from core.ui_screen import UiScreen, ScreenEnum

class QueryScreen(UiScreen):
    def __init__(self):
        self.name = ScreenEnum.QUERY_SCREEN
    def handle_input(self, input_string, services, state) -> tuple[bool, str | None]:
        if not input_string:
            state._error = "Please specify a species. [Empty string detected!]"
            return (True, ScreenEnum.ERROR_SCREEN)
        try:
            result = services.api_handler.get_species(input_string)
            if result is None:
                state._error = "EMPTY RESULT"
                return (True, ScreenEnum.ERROR_SCREEN)
            state._active_data = result
            return (True, ScreenEnum.VERSION_SCREEN)
        except Exception as e:
            state._error = e
            return (True, ScreenEnum.ERROR_SCREEN)
    def on_enter(self, services, state):
        print("Welcome to the CLI-PokeApi-Display program!\nPlease enter a Pokemon species to query!"
              + "\n(When on any screen, press [ENTER] with no input to go back)"
        )