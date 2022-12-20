import heapq

from print_distribution import print_tasks_distribution
def find_approximate_schedule(number_of_machines: int, times_of_tasks: list):
    times_of_tasks.sort(reverse=True)
    machines = [[0, machine_num] for machine_num in range(number_of_machines)]
    heapq.heapify(machines)
    optimal_distribution = [[] * _ for _ in range(number_of_machines)]
    for time in times_of_tasks:
        less_busy_machine = heapq.heappop(machines)
        less_busy_machine[0] += time
        optimal_distribution[less_busy_machine[1]].append('*' * time + '|')
        heapq.heappush(machines, less_busy_machine)
    optimal_scheduling_time = max(machines)[0]
    return optimal_distribution, optimal_scheduling_time

