def get_input():
    codes = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            codes.append(line.strip())
    return codes



def bit_criteria(i, codes, gas):
    bit_list = [int(code[i]) for code in codes]  # get relevant bit from codes
    count_1 = sum(bit_list)
    count_0 = len(codes) - count_1
    print(f"Num codes: {len(codes)}")
    print(f"Num 1s: {count_1}")
    print(f"Num 0s: {count_0}")
    if gas == "oxygen":  # Get most common bit
        print("Oxygen->most common bit->'1' wins in tie")
        is_1 = count_1 >= count_0  # if equal, select "1"
    if gas == "carbon":  # Get least common bit
        print("Carbon->least common bit->'0' wins tie")
        is_1 = count_1 < count_0  # if equal select "0"
    
    if is_1:
        bit_val = 1
    else:
        bit_val = 0
    return bit_val

def scrubber(codes, gas):
    result = []
    new_codes = []
    for i in range(len(codes[0])):
        print("------------------")
        print(f"bit: {i}")
        bit_val = bit_criteria(i, codes, gas)
        print("bit_criteria: ", bit_val)
        for code in codes:
            if int(code[i]) == bit_val:
                new_codes.append(code)
        codes = new_codes
        new_codes = []
        if len(codes) == 1:
            return codes
    return codes


codes = get_input()
oxygen_code = scrubber(codes, "oxygen")[0]
carbon_code = scrubber(codes, "carbon")[0]

print()
print("Oxygen binary: ", oxygen_code)
print("Carbon binary: ", carbon_code)
oxygen_dec = int(oxygen_code, 2)
carbon_dec = int(carbon_code, 2)

print("Oxygen decimal: ", oxygen_dec)
print("Carbon decimal: ", carbon_dec)
print("Final answer: ", oxygen_dec * carbon_dec)
