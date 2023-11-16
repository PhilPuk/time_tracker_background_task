from sys import path
from matplotlib import pyplot as plt

path.append(".../")

from logic.processes.tracked_processes import TrackedProcesses


def plot(TrackedProcesses):
    tracked_processes = TrackedProcesses()

    times = []

    for process in tracked_processes.get_processes():
        times.append(process.get_time() / 60.)

    fig, ax = plt.subplots()
    rects1 = ax.bar(x=range(len(times)), height=times)

    ax.set_ylim(0, max(times))
    ax.set_ylabel('time in min')
    ax.set_xticks(np.add(range(len(times)), 0.5))
    ax.set_xticklabels([process.get_ui_name() for process in tracked_processes.get_processes()])

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects1)

    plt.show()
