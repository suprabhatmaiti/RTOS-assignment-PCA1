class Process:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.execution_time = 0

def priority_inversion_schedule(processes):
    # Sort processes based on priority
    processes.sort(key=lambda x: x.priority)

    current_time = 0
    for process in processes:
        if process.deadline < current_time + process.execution_time:
            print(f"Process {process.name} will miss the deadline.")
            return False

        current_time += process.execution_time

    print("All processes will meet their deadlines.")
    return True

def get_processes_from_user():
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        name = input(f"Enter name for process {i+1}: ")
        priority = int(input(f"Enter priority for process {i+1}: "))
        deadline = int(input(f"Enter deadline for process {i+1}: "))

        process = Process(name, priority, deadline)
        processes.append(process)

    return processes

if __name__ == "__main__":
    processes = get_processes_from_user()

    # Assume execution time for each process
    for process in processes:
        process.execution_time = int(input(f"Enter execution time for process {process.name}: "))

    priority_inversion_schedule(processes)
