from logic.processes.machine_processes import MachineProcesses
from logic.processes.tracked_processes import TrackedProcesses
from utility.logger_config import log
import time
import psutil

def start_find_process(process) -> [bool, int]:
    for pid, process_name in machine_processes.get_processes().items():
        if process.get_name() == process_name:
            return True, pid
    return False, -1


def check_tracked_processes() -> None:
    for process in tracked_processes.get_processes():
        if start_find_process(process):
            print(f"Found: {process.get_ui_name()}")
        else:
            print(f"Did not find: {process.get_ui_name()}")


def start_tracking() -> None:
    for process in tracked_processes.get_processes():
        found, pid = start_find_process(process)
        if found:
            log.info(f"Found process: {process.get_ui_name()} with PID: {pid}")
            process.set_start_time(time.time())
            process.set_pid(pid)
        else:
            continue

def find_process(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def run():
    try:
        start_tracking()

        while True:
            processing_time_start = time.time()
            for process in tracked_processes.get_processes():
                if psutil.pid_exists(process.get_pid()):
                    process.add_time(time.time() - process.get_start_time())
                    process.set_start_time(time.time())
                else:
                    machine_processes.update()
                    found, pid = start_find_process(process)
                    if found:
                        log.info(f"Found process: {process.get_ui_name()} with PID: {pid}")
                        process.set_start_time(time.time())
                        process.set_pid(pid)
                    continue
            tracked_processes.save()
            processing_time = time.time() - processing_time_start
            log.info(f"Processing time: {processing_time}")
            time.sleep(5.0-processing_time if processing_time < 5.0 else 0.1)
    except KeyboardInterrupt:
        log.info(f"Program stopped - running time: {time.time() - start}")
        tracked_processes.save()
        exit(0)


if __name__ == '__main__':
    log.info("Program started")

    start = time.time()
    tracked_processes = TrackedProcesses()
    machine_processes = MachineProcesses()

    run()
    log.info("Program finished")


"""

def run():
    try:
        start_tracking()

        while True:
            for process in tracked_processes.get_processes():
                if machine_processes.process_exists(process.get_pid()):
                    process.add_time(time.time() - process.get_start_time())
                    process.set_start_time(time.time())
                else:
                    found, pid = start_find_process(process)
                    if found:
                        log.info(f"Found process: {process.get_ui_name()} with PID: {pid}")
                        process.set_start_time(time.time())
                        process.set_pid(pid)
                    continue
            processing_time_start = time.time()
            tracked_processes.save()
            machine_processes.update()
            processing_time = time.time() - processing_time_start
            log.info(f"Processing time: {processing_time}")
            time.sleep(5.0-processing_time if processing_time < 5.0 else 0.1)
    except KeyboardInterrupt:
        log.info(f"Program stopped - running time: {time.time() - start}")
        tracked_processes.save()
        exit(0)

"""