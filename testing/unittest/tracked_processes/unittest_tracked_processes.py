import unittest
from sys import path
from pathlib import Path


path.append(".../")

from logic.processes.tracked_processes import TrackedProcesses
from logic.processes.process import Process

awaited_tracked_processes = [
    Process(pid=20772,
            name="LeagueClientUx.exe",
            ui_name="League of Legends",
            exe_path="C:\\Riot Games\\League of Legends\\LeagueClient.exe",
            time=1378.0,
            start_time=1699371296.0),

    Process(pid=16796,
            name="opera.exe",
            ui_name="OperaGX",
            exe_path="D:\\Programme (x86)\\Opera GX\\launcher.exe",
            time=1425.0,
            start_time=1699371296.0),

    Process(pid=19460,
            name="Spotify.exe",
            ui_name="Spotify",
            exe_path="C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.222.982.0_x64__zpdnekdrzrea0\\Spotify.exe",
            time=922.0,
            start_time=1699371296.0),

    Process(pid=19396,
            name="Discord.exe",
            ui_name="Discord",
            exe_path="C:\\Users\\Phil\\AppData\\Local\\Discord\\app-1.0.9021",
            time=1378.0,
            start_time=1699371296.0)
]
tracked_processes = TrackedProcesses(Path(__file__).parent / "tracked_processes.json")


class MyTestCase(unittest.TestCase):

    def test_loaded_correctly(self):
        self.assertEqual(len(tracked_processes.get_processes()), len(awaited_tracked_processes))

    def test_process_loaded_correctly(self):
        for i in range(len(tracked_processes.get_processes())):
            self.assertEqual(tracked_processes.get_processes()[i].get_name(), awaited_tracked_processes[i].get_name())

        for i in range(len(tracked_processes.get_processes())):
            self.assertEqual(tracked_processes.get_processes()[i].get_ui_name(),
                             awaited_tracked_processes[i].get_ui_name())

        for i in range(len(tracked_processes.get_processes())):
            self.assertEqual(tracked_processes.get_processes()[i].get_path(), awaited_tracked_processes[i].get_path())

        for i in range(len(tracked_processes.get_processes())):
            self.assertEqual(tracked_processes.get_processes()[i].get_time(), awaited_tracked_processes[i].get_time())

        for i in range(len(tracked_processes.get_processes())):
            self.assertEqual(tracked_processes.get_processes()[i].get_start_time(),
                             awaited_tracked_processes[i].get_start_time())

if __name__ == '__main__':
    unittest.main()
