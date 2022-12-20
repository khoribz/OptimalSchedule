import itertools
import sys

from print_distribution import print_tasks_distribution

def find_optimal_schedule(number_of_machines: int, times_of_tasks: list):

    machines = [_ for _ in range(number_of_machines)]
    machines_for_tasks = [machines] * len(times_of_tasks)
    tasks_distribution_all_cases = list(itertools.product(*machines_for_tasks))
    optimal_scheduling_time = sys.maxsize
    optimal_distribution = []
    for case in tasks_distribution_all_cases:
        machines_time = [0] * number_of_machines
        distribution = [""] * number_of_machines
        for task, machine in enumerate(case):
            machines_time[machine] += times_of_tasks[task]
            distribution[machine] += '*' * times_of_tasks[task] + '|'
        if max(machines_time) < optimal_scheduling_time:
            optimal_scheduling_time = max(machines_time)
            optimal_distribution = distribution
    return optimal_distribution, optimal_scheduling_time


