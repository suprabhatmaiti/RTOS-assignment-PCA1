from collections import defaultdict

def hlp_scheduling(processes):
    time = 0
    missed_deadlines = False

    # Create a dictionary to store tasks in each layer
    layers = defaultdict(list)

    while processes:
        # Assign tasks to layers based on deadlines
        for task in processes:
            layers[task[1]].append(task)

        # Iterate through layers and schedule tasks in Round Robin manner
        for layer, tasks in layers.items():
            while tasks:
                current_task = tasks.pop(0)

                # Execute the process for one time unit
                current_task[0] -= 1
                time += 1

                # Check for deadline misses
                if time > current_task[2]:
                    missed_deadlines = True
                    break

                # Remove completed processes
                if current_task[0] == 0:
                    processes.remove(current_task)

                # Move the task to the next layer if it's not completed
                elif time % current_task[1] == 0:
                    layers[current_task[1] * 2].append(current_task)

                # Move the task to the back of the queue
                else:
                    tasks.append(current_task)

            if missed_deadlines:
                break

    return not missed_deadlines

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        execution_time = int(input(f"Enter execution time for process {i + 1}: "))
        period = int(input(f"Enter period for process {i + 1}: "))
        deadline = int(input(f"Enter deadline for process {i + 1}: "))
        processes.append([execution_time, period, deadline])

    result = hlp_scheduling(processes)

    if result:
        print("All processes will meet their deadlines.")
    else:
        print("At least one process will miss its deadline.")
