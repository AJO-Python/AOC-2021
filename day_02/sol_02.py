def locate_sub():
    with open("input.txt", "r") as f:
        instructions = []
        horizontal = 0
        depth = 0
        for line in f.readlines():
            line = line[:-1]
            direction, distance = line.split(" ")
            distance = int(distance)
            if direction == "up":
                depth -= distance
            if direction == "down":
                depth += distance
            if direction == "forward":
                horizontal += distance

    print("horizontal: ", horizontal)
    print("depth: ", depth)
    print(horizontal * depth)

def locate_sub_aim():
    with open("input.txt", "r") as f:
        instructions = []
        horizontal = 0
        depth = 0
        aim = 0
        for line in f.readlines():
            line = line[:-1]
            direction, distance = line.split(" ")
            distance = int(distance)
            if direction == "up":
                aim -= distance
            if direction == "down":
                aim += distance
            if direction == "forward":
                horizontal += distance
                depth += (aim * distance)

    print("horizontal: ", horizontal)
    print("depth: ", depth)
    print(horizontal * depth)


locate_sub_aim()

