def print_tasks_distribution(distribution, distribution_name):
    print(distribution_name)
    for machine in distribution:
        result_for_machine = ""
        for task in machine:
            result_for_machine += task
        print(result_for_machine)
