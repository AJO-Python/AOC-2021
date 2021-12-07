import numpy as np
class Fish:
    def __init__(self, timer):
        self.timer = timer
        self.first_cycle = True

    def new_day(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6


class Schoal:
    day = 0

    def __init__(self, fishes):
        self.fishes = fishes

    def new_day(self):
        for i in range(len(self.fishes)):
            self.fishes[i] -= 1
            if self.fishes[i] < 0:
                self.fishes[i] = 6
                self.fishes.append(8)
        Schoal.day += 1

init_fish = [3,1,4,2,1,1,1,1,1,1,1,4,1,4,1,2,1,1,2,1,3,4,5,1,1,4,1,3,3,1,1,1,1,3,3,1,3,3,1,5,5,1,1,3,1,1,2,1,1,1,3,1,4,3,2,1,4,3,3,1,1,1,1,5,1,4,1,1,1,4,1,4,4,1,5,1,1,4,5,1,1,2,1,1,1,4,1,2,1,1,1,1,1,1,5,1,3,1,1,4,4,1,1,5,1,2,1,1,1,1,5,1,3,1,1,1,2,2,1,4,1,3,1,4,1,2,1,1,1,1,1,3,2,5,4,4,1,3,2,1,4,1,3,1,1,1,2,1,1,5,1,2,1,1,1,2,1,4,3,1,1,1,4,1,1,1,1,1,2,2,1,1,5,1,1,3,1,2,5,5,1,4,1,1,1,1,1,2,1,1,1,1,4,5,1,1,1,1,1,1,1,1,1,3,4,4,1,1,4,1,3,4,1,5,4,2,5,1,2,1,1,1,1,1,1,4,3,2,1,1,3,2,5,2,5,5,1,3,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,3,1,4,1,4,2,1,3,4,1,1,1,2,3,1,1,1,4,1,2,5,1,2,1,5,1,1,2,1,2,1,1,1,1,4,3,4,1,5,5,4,1,1,5,2,1,3]
fish = [0 for _ in range(9)]
print(fish)
for f in init_fish:
    fish[f] += 1
print(fish)

for i in range(256):
    spawn_fish = fish[0]
    for f in range(1, len(fish)):
        fish[f-1] = fish[f]
    fish[6] += spawn_fish
    fish[-1] = spawn_fish
    print(fish)
print(sum(fish))


# unique_starting = np.unique(init_fish)
# print(unique_starting)
# school = Schoal(init_fish)
# for i in unique_starting:
#     school = Schoal([i])
#     for day in range(256):
#         school.new_day()
#         print(day)
#     print(f"Start age: {i}")
#     print(f"Total num of fish: {len(school.fishes)}")
#
# # for i in range(256):
# #     school.new_day()
# #     print(i)
# print(len(school.fishes))