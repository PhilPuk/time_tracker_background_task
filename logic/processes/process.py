from sys import path
from pathlib import Path
path.append(".../")
from PIL import Image


class Process:
    def __init__(self,
                 pid: int = -1,
                 name: str = "",
                 ui_name: str = "",
                 exe_path: str = "",
                 icon: Image = Image.open(str(Path(__file__).parent.parent.parent / "data" / "none.png")),
                 time: float = 0,
                 start_time: float = 0
                 ) -> None:
        self._pid = pid
        self._name = name
        self._ui_name = ui_name
        self._path = exe_path
        self._icon = icon
        self._time = time
        self._start_time = start_time

    def get_pid(self) -> int:
        return self._pid

    def get_name(self) -> str:
        return self._name

    def get_ui_name(self) -> str:
        return self._ui_name

    def get_path(self) -> str:
        return self._path

    def get_icon(self):
        return self._icon

    def get_time(self) -> float:
        return self._time

    def get_start_time(self) -> float:
        return self._start_time

    def set_start_time(self, time: float):
        self._start_time = time

    def set_pid(self, pid: int):
        self._pid = pid

    def add_time(self, time: float):
        self._time += time

    def __str__(self) -> str:
        return f"pid: {self._pid}\n" \
               f"name: {self._name}\n" \
               f"ui_name: {self._ui_name}\n" \
               f"path: {self._path}\n" \
               f"icon: {self._icon}\n" \
               f"time: {self._time}\n" \
               f"start_time: {self._start_time}\n"

