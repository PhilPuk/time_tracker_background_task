from sys import path
import os
path.append(".../")

import wmi

#from utility.logger_config import log
from logic.processes.processes import Processes


class MachineProcesses(Processes):
    def __init__(self) -> None:
        super().__init__(self._init_machine_processes_dict())

    @staticmethod
    def _init_machine_processes_dict() -> dict:
        processes_dict = {}
        #c = wmi.WMI()
        print(len("Description                                                    ProcessId"))
        output = os.popen('wmic process get description, processid').read()
        output = output[72:]
        output = output.replace(" ", "")
        print(output)
        for process in output:
            processes_dict[process[0]] = process[1]

        return processes_dict

    def update(self):
        self._processes = self._init_machine_processes_dict()

    def process_exists(self, pid: int) -> bool:
        return pid in self._processes.keys()
