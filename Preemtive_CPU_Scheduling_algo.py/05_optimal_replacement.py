pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = []
size = 3
faults = 0

for i in range(len(pages)):
    page = pages[i]

    if page not in frames:
        faults += 1

        if len(frames) < size:
            frames.append(page)
        else:
            future = pages[i + 1:]
            index = 0
            farthest = -1

            for j in range(len(frames)):
                if frames[j] not in future:
                    index = j
                    break
                pos = future.index(frames[j])
                if pos > farthest:
                    farthest = pos
                    index = j

            frames[index] = page

    print(frames)

print("Page Faults =", faults)