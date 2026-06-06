#priority based
n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    at = int(input(f"Enter arrival time of P{i+1}: "))
    p = int(input(f"Enter priority of P{i+1}: "))
    bt = int(input(f"Enter burst time of P{i+1}: "))
    processes.append([i+1, at, bt, p])

time = 0
completed = 0
ct = [0] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n
done = [False] * n

while completed < n:
    idx = -1
    high_priority = float('inf')
    for i in range(n):
        if processes[i][1] <= time and not done[i]:
            if processes[i][3] < high_priority:
                high_priority = processes[i][3]
                idx = i
    if idx != -1:
        rt[idx] = time - processes[idx][1]
        time += processes[idx][2]
        ct[idx] = time
        tat[idx] = ct[idx] - processes[idx][1]
        wt[idx] = tat[idx] - processes[idx][2]
        done[idx] = True
        completed += 1
    else:
        time += 1

print("\nP\tAT\tBT\tPR\tCT\tTAT\tWT\tRT")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{processes[i][3]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\t{rt[i]}")