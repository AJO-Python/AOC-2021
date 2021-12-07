
with open("input.txt", "r") as f:
    data = [int(x) for x in f.readline().split(",")]

small = min(data)
big = max(data)
min_fuel = 99999999999
print(small, big)
for i in range(small, big+1):
    fuel = sum([sum(range(0, abs(x-i)+1)) for x in data])
    if fuel < min_fuel:
        min_fuel = fuel
        index = i
        print(min_fuel)
        print(index)
print("FUEL: ", min_fuel)
print("POSITION: ", index)
