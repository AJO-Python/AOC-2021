def simple_counter():
    with open("input.txt", "r") as f:
        numbers = []
        counter = 0
        for num in f.readlines():
            num = int(num)
            numbers.append(num)

        for i in range(1, len(numbers)):
            if numbers[i] > numbers[i-1]:
                counter += 1
            print(counter)

def rolling_average_counter(window_size: int):
    with open("input.txt", "r") as f:
        numbers = []
        counter = 0
        for num in f.readlines():
            num = int(num)
            numbers.append(num)

        prev_win_sum = sum(numbers[0:window_size])
        for i in range(window_size, len(numbers)):
            cur_win_sum = sum(numbers[i-window_size:i])
            print("------")
            print("prev: ", prev_win_sum)
            print("cur: ", cur_win_sum)
            if cur_win_sum > prev_win_sum:
                print("Increase")
                counter += 1
                print(counter)
            else:
                print("No change or decreased")
            prev_win_sum = cur_win_sum
        print(numbers[-10:])

rolling_average_counter(3)




