from sys import path
import os
import json
from pathlib import Path
path.append(".../")

#from logic.processes.processes import Processes #local machine
from processes import Processes #school machine

class MachineProcesses(Processes):
    def __init__(self) -> None:
        super().__init__(self._init_machine_processes_dict())

    @staticmethod
    def _init_machine_processes_dict() -> dict:
        processes_dict = {}
        output = os.popen('wmic process get description, processid').read()
        output = output[72:].replace(" ", "").split("\n")
        for process in output:
            try:
                if process == "" or process == '' or process == " " or process.find("exe") == -1:
                    continue
                name = process.split("exe", 1)[0] 
                id = process[len(name)+3:]
                processes_dict[name+"exe"] = id
            except IndexError:
                pass
        return processes_dict

    def update(self):
        self._processes = self._init_machine_processes_dict()

    def process_exists(self, pid: int) -> bool:
        return pid in self._processes.keys()
    
    def save(self, filePath: str=None) -> None:
        filePath = Path(filePath) if filePath is not None else Path(__file__).parent.parent.parent / "data" / "machine_processes.json"
        with open(str(filePath), "w") as f:
            json.dump(self._processes, f, indent=4)

tmp = MachineProcesses()
#print(tmp.get_processes())
tmp.save()