from sys import path
import pandas as pd

path.append(".../")

from logic.processes.process import Process


class Processes:
    def __init__(self, processes: list | dict = None) -> None:
        self._processes = processes

    def save_processes_to_csv(self, filepath: str) -> None:
        processes_dataframe = pd.DataFrame(columns=["pid", "name", "ui_name", "path", "time", "start_time"])
        processes_dataframe.to_csv(filepath)

    def get_process(self, pid: int = None, name: str = None) -> Process | int:
        if pid:
            for process in self._processes:
                if process.get_pid() == pid:
                    return process
        elif name:
            for process in self._processes:
                if process.get_name() == name:
                    return process
        else:
            return -1

    def get_processes(self) -> list | dict:
        return self._processes

    def add_Process(self, process: Process) -> None:
        self._processes.append(process)

    def update_activity(self) -> None:
        for process in self._processes:
            process.update()
