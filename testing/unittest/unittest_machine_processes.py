import unittest
from sys import path
path.append(".../")

from logic.processes.machine_processes import MachineProcesses


class MyTestCase(unittest.TestCase):
    def test_dict_is_not_empty(self):
        machine_processes = MachineProcesses()
        self.assertGreater(len(machine_processes.get_processes()), 0)


if __name__ == '__main__':
    unittest.main()
