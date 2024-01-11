def edf_scheduling(processes):
    time = 0
    missed_deadlines = False

    while processes:
        # Sort processes based on their deadlines
        processes.sort(key=lambda x: x[1])

        # Get the process with the earliest deadline
        current_process = processes[0]

        # Execute the process for one time unit
        current_process[0] -= 1
        time += 1

        # Remove completed processes
        if current_process[0] == 0:
            processes.remove(current_process)

        # Check for deadline misses
        if time > current_process[1]:
            missed_deadlines = True
            break

    return not missed_deadlines

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        execution_time = int(input(f"Enter execution time for process {i + 1}: "))
        deadline = int(input(f"Enter deadline for process {i + 1}: "))
        processes.append([execution_time, deadline])

    result = edf_scheduling(processes)

    if result:
        print("All processes will meet their deadlines.")
    else:
        print("At least one process will miss its deadline.")
