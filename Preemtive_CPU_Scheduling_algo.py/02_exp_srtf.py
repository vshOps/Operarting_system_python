n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    at = int(input(f"Enter arrival time of P{i+1}: "))
    bt = int(input(f"Enter burst time of P{i+1}: "))
    processes.append([i+1, at, bt])

time = 0
completed = 0

ct = [0] * n
tat = [0] * n
wt = [0] * n
rt = [p[2] for p in processes]

while completed < n:
    idx = -1
    min_rt = float('inf')
    
    for i in range(n):
        if processes[i][1] <= time and rt[i] > 0:
            if rt[i] < min_rt:
                min_rt = rt[i]
                idx = i
    
    if idx != -1:
        rt[idx] -= 1
        time += 1
        
        if rt[idx] == 0:
            completed += 1
            ct[idx] = time
            tat[idx] = ct[idx] - processes[idx][1]
            wt[idx] = tat[idx] - processes[idx][2]
    else:
        time += 1

print("\nP\tAT\tBT\tCT\tTAT\tWT\tRT")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\t{rt[i]}")