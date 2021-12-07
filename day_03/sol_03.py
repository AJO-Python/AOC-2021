
def get_input():
    codes = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            codes.append(line.strip())
    return codes


def calc_gamma(codes):
    gamma = [[0, 0] for _ in codes[0]]
    # get occurence of 0 and 1 in each bit position
    for code in codes:
        for i in range(len(code)):
            if code[i] == "0":
                gamma[i][0] += 1
            else:
                gamma[i][1] += 1
    print(gamma)
    # get final gamma
    final_gamma = ["0" if bit[0] > bit[1] else "1" for bit in gamma]
    return "".join(final_gamma)


def calc_epsilon(gamma):
    epsilon = ["0" if x=="1" else "1" for x in gamma]
    return "".join(epsilon)

def new_calc_epsilon(codes):
    epsilon = [[0, 0] for _ in codes[0]]
    # get occurence of 0 and 1 in each bit position
    for code in codes:
        for i in range(len(code)):
            if code[i] == "0":
                epsilon[i][0] += 1
            else:
                epsilon[i][1] += 1
    final_epsilon = ["0" if bit[0] < bit[1] else "1" for bit in epsilon]
    return "".join(final_epsilon)

codes = get_input()
print(codes[:5])
gamma = calc_gamma(codes)
print(gamma)
epsilon = calc_epsilon(gamma)
# epsilon = new_calc_epsilon(codes)
print(epsilon)
gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(gamma_dec * epsilon_dec)
print("-----------------------------")

def get_oxygen(codes, gamma):
    print("In get_oxygen")
    old_codes = codes
    new_codes = []
    for i, bit in enumerate(gamma):
        print(f"On bit {i}: {bit}")
        for code in old_codes:
            print("On code: ", code)
            if code[i] == bit:
                new_codes.append(code)
                print(f"Added: pos-{i}, val-{bit}, code-{code}")
            else:
                print(f"Code-{code} failed to match the bit")
            if i == len(gamma):
                return new_codes
        old_codes = new_codes
        print(new_codes)
        print(len(new_codes))
        new_codes = [] 
        if len(old_codes) == 1:
            return old_codes

oxygen_bin = get_oxygen(codes, gamma)[0]
c02_bin = get_oxygen(codes, epsilon)[0]
oxygen = int(oxygen_bin, 2)
c02 = int(c02_bin, 2)
print("Oxygen binary: ", oxygen_bin)
print("C02 binary: ", c02_bin)
print("Oxygen: ", oxygen)
print("C02: ", c02)

print("Result: ", c02 * oxygen)


def oxygen(codes):
    for i in range(len(codes[0])):
        print(i)

oxygen(codes)



