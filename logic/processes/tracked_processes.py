from sys import path
import json
from pathlib import Path

path.append(".../")

from logic.processes.processes import Processes
from logic.processes.process import Process


class TrackedProcesses(Processes):
    def __init__(self, tracked_processes_json_path: Path = Path(
        __file__).parent.parent.parent / "data" / "tracked_processes.json") -> None:
        super().__init__([])

        self._tracked_processes_json_path = tracked_processes_json_path
        self._init_tracked_processes()

    def _init_tracked_processes(self) -> None:
        if self._tracked_processes_json_path.exists():
            with open(str(self._tracked_processes_json_path), "r") as f:
                tracked_processes_dict = json.load(f)
            for entry in tracked_processes_dict.values():
                self.get_processes().append(
                    Process(entry["PID"], entry["NAME"], entry["UI_NAME"], entry["PATH"],
                            entry["TIME"], entry["START_TIME"]))

    def save(self):
        tracked_processes_dict = {}
        for process in self.get_processes():
            tracked_processes_dict[process.get_ui_name()] = {
                "PID": process.get_pid(),
                "NAME": process.get_name(),
                "UI_NAME": process.get_ui_name(),
                "PATH": process.get_path(),
                "TIME": process.get_time(),
                "START_TIME": process.get_start_time()
            }
        with open(str(self._tracked_processes_json_path), "w") as f:
            json.dump(tracked_processes_dict, f, indent=4)

    def add_Process(self, process: Process) -> None:
        self._processes.append(process)
        self.save()

    def check_active(self):
        for process in self._processes:
            if process.get_active():
                return True
        return False
