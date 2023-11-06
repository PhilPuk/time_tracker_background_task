from sys import path

path.append(".../")

import wmi

from utility.logger_config import log
from logic.processes.processes import Processes


class MachineProcesses(Processes):
    def __init__(self) -> None:
        super().__init__(self._init_machine_processes_dict())

    @staticmethod
    def _init_machine_processes_dict() -> dict:
        processes_dict = {}
        c = wmi.WMI()
        for process in c.Win32_Process():
            processes_dict[process.ProcessId] = process.Name

        return processes_dict

    def update(self):
        self._processes = self._init_machine_processes_dict()

    def process_exists(self, pid: int) -> bool:
        return pid in self._processes.keys()
