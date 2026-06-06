# FCFS CPU Scheduling with Response Time

n = int(input("Enter number of processes: "))

process = []

# Input AT and BT only
for i in range(n):
    at = int(input(f"Enter Arrival Time of P{i+1}: "))
    bt = int(input(f"Enter Burst Time of P{i+1}: "))
    process.append([i+1, at, bt])

# Sort by Arrival Time
process.sort(key=lambda x: x[1])

ct = 0
total_wt = 0
total_tat = 0
total_rt = 0

print("\nPID\tAT\tBT\tCT\tTAT\tWT\tRT")

for i in range(n):
    pid, at, bt = process[i]

    # Start time logic
    if ct < at:
        ct = at
    start_time = ct

    # Completion Time
    ct += bt

    # Calculations
    tat = ct - at
    wt = tat - bt
    rt = start_time - at   # Response Time

    total_tat += tat
    total_wt += wt
    total_rt += rt

    print(f"P{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}\t{rt}")