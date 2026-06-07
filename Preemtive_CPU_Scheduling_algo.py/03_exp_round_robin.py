n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    at = int(input(f"Enter arrival time of P{i+1}: "))
    bt = int(input(f"Enter burst time of P{i+1}: "))
    processes.append([i+1, at, bt])

tq = int(input("Enter Time Quantum: "))

time = 0
queue = []
rt = [p[2] for p in processes]
ct = [0] * n
tat = [0] * n
wt = [0] * n

visited = [False] * n
completed = 0

while completed < n:
    for i in range(n):
        if processes[i][1] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True
    if not queue:
        time += 1
        continue
    idx = queue.pop(0)
    if rt[idx] > tq:
        time += tq
        rt[idx] -= tq
    else:
        time += rt[idx]
        rt[idx] = 0
        ct[idx] = time
        completed += 1
    for i in range(n):
        if processes[i][1] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True
    if rt[idx] > 0:
        queue.append(idx)
for i in range(n):
    tat[i] = ct[i] - processes[i][1]
    wt[i] = tat[i] - processes[i][2]

print("\nP\tAT\tBT\tCT\tTAT\tWT\tRT")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\t{rt[i]}")