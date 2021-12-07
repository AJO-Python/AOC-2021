import numpy as np

# Read the data in like this because who is ever gonna read this again and sometimes its fun to watch the world burn
data = [list(map(int, (*pos[0].split(","), *pos[1].split(","))))  for pos in [line.strip().split(" -> ") for line in open("input.txt").readlines()]]
#  data: [[x1, y1, x2 ,y2], ...]
coords = {}
for i, line in enumerate(data):
    print(f"On line {i}/{len(data)}")
    # Use linspace instead of built-in 'range()' to allow for easy negative iteration (eg x2 smaller than x1)
    x_range = np.linspace(line[0], line[2], endpoint=True, num=abs(line[0]-line[2])+1)
    y_range = np.linspace(line[1], line[3], endpoint=True, num=abs(line[1]-line[3])+1)
    if len(x_range) == 1:  # Straight along y axis
        x = x_range[0]
        for y in y_range:
            coords[(x, y)] = coords.get((x, y), 0) + 1
    elif len(y_range) == 1: # Straight along x axis
        y = y_range[0]
        for x in x_range:
            coords[(x, y)] = coords.get((x, y), 0) + 1
    else:  # Diagonal lines
        for x, y in zip(x_range, y_range):
            coords[(x, y)] = coords.get((x, y), 0) + 1


print(sum(1 for val in coords.values() if val >= 2))
