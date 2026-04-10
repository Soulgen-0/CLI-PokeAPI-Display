VERSION = "version"
FLAVOR_TEXT_ENTRIES = "flavor_text_entries"
LANGUAGE = "language"
FLAVOR_TEXT = "flavor_text"
NAME = "name"

class FlavorText:
    def __init__(self, version: str, flavor_text: str):
        self.version = version
        self.flavor_text = flavor_text
    def __str__(self):
        return self.flavor_text

class PokeData():
    def __init__(self, data: dict):
        self.name: str = data.get(NAME, "MISSING NAME")
        
        flavor_texts = {}
        flavor_text_entries = data.get(FLAVOR_TEXT_ENTRIES, [])
        length = len(flavor_text_entries)
        if length > 0:
            for flavor_text_data in flavor_text_entries:
                language = flavor_text_data[LANGUAGE]["name"]
                version = flavor_text_data[VERSION]["name"]
                if language != "en":
                    continue
                flavor_text = FlavorText(version, flavor_text_data[FLAVOR_TEXT])
                flavor_texts[version] = flavor_text

        self._flavor_texts: list[FlavorText] = flavor_texts
    def _get_flavor_text(self, version: str) -> FlavorText | None:
        return self._flavor_texts.get(version)
    def get_versions(self) -> str:
        return "\n".join([f"{key.capitalize()}" for key in self._flavor_texts.keys()])
    def display_version(self, version: str) -> str | None:
        flavor_text: FlavorText | None = self._get_flavor_text(version)
        if not flavor_text:
            return
        return str(flavor_text)
    def __str__(self) -> str:
        return f"Name: {self.name.capitalize()}\n" + "\n".join([str(entry) for entry in self._flavor_texts])