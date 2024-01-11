def rms_scheduling(processes):
    time = 0
    missed_deadlines = False

    while processes:
        # Sort processes based on their periods (rates)
        processes.sort(key=lambda x: x[1])

        # Get the process with the shortest period (highest rate)
        current_process = processes[0]

        # Execute the process for one time unit
        current_process[0] -= 1
        time += 1

        # Check for deadline misses
        if time % current_process[1] == 0 and current_process[0] > 0:
            missed_deadlines = True
            break

        # Remove completed processes
        if current_process[0] == 0:
            processes.remove(current_process)

    return not missed_deadlines

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        execution_time = int(input(f"Enter execution time for process {i + 1}: "))
        period = int(input(f"Enter period for process {i + 1}: "))
        processes.append([execution_time, period])

    result = rms_scheduling(processes)

    if result:
        print("All processes will meet their deadlines.")
    else:
        print("At least one process will miss its deadline.")
