from logic.processes.machine_processes import MachineProcesses
from logic.processes.tracked_processes import TrackedProcesses
from utility.logger_config import log
import time
import psutil


class App:
    def __init__(self):
        log.info("Program started")

        self._start = time.time()

        self.tracked_processes = TrackedProcesses()
        self.machine_processes = MachineProcesses()

    def start_find_process(self, process_name_to_find) -> [bool, int]:
        for pid, process_name in self.machine_processes.get_processes().items():
            if process_name_to_find == process_name:
                return True, pid
        return False, -1

    def check_tracked_processes(self) -> None:
        for process in self.tracked_processes.get_processes():
            if self.start_find_process(process):
                print(f"Found: {process.get_ui_name()}")
            else:
                print(f"Did not find: {process.get_ui_name()}")

    def start_tracking(self) -> None:
        for process in self.tracked_processes.get_processes():
            found, pid = self.start_find_process(process.get_name())
            if found:
                log.info(f"Found process: {process.get_ui_name()} with PID: {pid}")
                process.set_start_time(time.time())
                process.set_pid(pid)
            else:
                continue

    def run(self):
        try:
            self.start_tracking()

            while True:
                processing_time_start = time.time()
                for process in self.tracked_processes.get_processes():
                    if psutil.pid_exists(process.get_pid()):
                        process.add_time(time.time() - process.get_start_time())
                        process.set_start_time(time.time())
                    else:
                        self.machine_processes.update()
                        found, pid = self.start_find_process(process)
                        if found:
                            log.info(f"Found process: {process.get_ui_name()} with PID: {pid}")
                            process.set_start_time(time.time())
                            process.set_pid(pid)
                        continue
                self.tracked_processes.save()
                processing_time = time.time() - processing_time_start
                log.info(f"Processing time: {processing_time}")
                time.sleep(5.0 - processing_time if processing_time < 5.0 else 0.1)
        except KeyboardInterrupt:
            log.info(f"Program stopped - running time: {time.time() - self._start}")
            self.tracked_processes.save()
            exit(0)
