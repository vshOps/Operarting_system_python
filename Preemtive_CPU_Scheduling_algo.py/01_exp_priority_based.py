n = int(input("Enter number of processes: "))

at = []
bt = []
pr = []

for i in range(n):
    at.append(int(input(f"Enter arrival time of P{i+1}: ")))
    bt.append(int(input(f"Enter burst time of P{i+1}: ")))
    pr.append(int(input(f"Enter priority of P{i+1}: ")))

remaining_bt = bt.copy()

ct = [0]*n
tat = [0]*n
wt = [0]*n
rt = [-1]*n

time = 0
completed = 0

while completed < n:
    idx = -1
    highest_priority = -1
    for i in range(n):
        if at[i] <= time and remaining_bt[i] > 0:
            if pr[i] > highest_priority:
                highest_priority = pr[i]
                idx = i

    if idx == -1:
        time += 1
        continue

    if rt[idx] == -1:
        rt[idx] = time - at[idx]
    remaining_bt[idx] -= 1
    time += 1

    if remaining_bt[idx] == 0:
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]
        completed += 1

print("\nP\tAT\tBT\tPR\tCT\tTAT\tWT\tRT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{pr[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\t{rt[i]}")