import itertools
import random
import unittest

from approximate_algorithm import find_approximate_schedule
from complete_bust_algorithm import find_optimal_schedule


class TestApproximation(unittest.TestCase):

    def test_for_N_tasks(self):
        all_tasks_num = [3, 4, 5, 6]
        for tasks_num in all_tasks_num:
            tasks_time = [_ for _ in range(1, 1 + tasks_num)]
            tasks_combinations = [tasks_time] * tasks_num
            tasks_times_all_cases = list(itertools.product(*tasks_combinations))
            for task_set in tasks_times_all_cases:
                task_set = list(task_set)
                for machines_num in range(2, tasks_num):
                    optimal_time = find_optimal_schedule(machines_num, task_set)[1]
                    approximate_time = find_approximate_schedule(machines_num, task_set.copy())[1]
                    print("case: ", task_set, "machines: ", machines_num,
                          "optimal:", optimal_time, "approximate: ", approximate_time)
                    self.assertGreaterEqual(4 / 3 * optimal_time, approximate_time)

    def test_many_tasks(self):
        tasks_num = 20
        task_set = [random.randrange(1, 10000) for _ in range(tasks_num)]
        machines_num = 2
        optimal_time = find_optimal_schedule(machines_num, task_set)[1]
        approximate_time = find_approximate_schedule(machines_num, task_set.copy())[1]
        print("case: ", task_set, "machines: ", machines_num,
              "optimal:", optimal_time, "approximate: ", approximate_time)
        self.assertGreaterEqual(4 / 3 * optimal_time, approximate_time)


if __name__ == '__main__':
    unittest.main()
