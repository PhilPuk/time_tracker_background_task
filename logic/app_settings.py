from sys import path
from pathlib import Path

path.append(".../")


class AppSettings:
    def __init__(self,
                 app_settings_path: Path=Path(__file__).parent.parent.parent / "data" / "app_settings.json") -> None:
        self._app_settings_path = app_settings_path
        self._init_app_settings()

    def _init_app_settings(self) -> None:

        pass
