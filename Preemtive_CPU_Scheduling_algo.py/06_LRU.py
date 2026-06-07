n=int(input("Enter number of pages: "))
pages=list(map(int,input("Enter page reference string: ").split()))
frames=int(input("Enter number of frames: "))
memory=[]
recent=[]
faults=0
for i in range(n):
    if pages[i] not in memory:
        if len(memory)<frames:
            memory.append(pages[i])
        else:
            lru=min(recent,key=recent.get)
            idx=memory.index(lru)
            memory[idx]=pages[i]
            del recent[lru]
        faults+=1
    recent[pages[i]]=i
    print(memory)
print("Total Page Faults:",faults)