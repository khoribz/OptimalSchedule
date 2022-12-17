import heapq


def find_approximate_schedule(number_of_machines: int, times_of_tasks: list):
    times_of_tasks.sort(reverse=True)
    machines = [[0, machine_num] for machine_num in range(number_of_machines)]
    heapq.heapify(machines)
    tasks_distribution = [[] * _ for _ in range(number_of_machines)]
    for time in times_of_tasks:
        less_busy_machine = heapq.heappop(machines)
        less_busy_machine[0] += time
        tasks_distribution[less_busy_machine[1]].append('*' * time + '|')
        heapq.heappush(machines, less_busy_machine)
    for i in tasks_distribution:
        ans = ""
        for j in i:
            ans += j
        print(ans)
    return tasks_distribution, max(machines[0])


# print(find_approximate_schedule(3, [3, 5, 6, 2, 5, 30, 19, 1, 4, 6, 7, 4, 5, 3, 7, 1, 9, 2, 5, 3, 2, 5, 1])[1])