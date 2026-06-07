pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = []
size = 3
faults = 0

for page in pages:
    if page not in frames:
        faults += 1

        if len(frames) < size:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)

    print(frames)

print("Page Faults =", faults)