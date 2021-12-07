def get_input(file):
    with open(file, "r") as f:
        pick_list = [int(x) for x in f.readline().split(",")]
        cards = []
        current_card = []
        for line in f.readlines():
            line = line.split()
            if line == []:
                cards.append(current_card)
                current_card = []
            else:
                current_card.append([[int(x), 0] for x in line])

    return pick_list, cards[1:]

def pick_number(pick, cards):
    #print("Checking for: ", pick)
    for c, card in enumerate(cards):
        #print("card: ", card)
        for l, line in enumerate(card):
            #print("line: ", line)
            for n, num in enumerate(line):
                #print("num: ", num)
                if pick == num[0]:
                    cards[c][l][n][1] = 1
                    #print("Picked ", pick)
                    #print(cards[c][l][n])
    return cards


def sum_unpicked_nums(card):
    total = 0
    for line in card:
        for val, pick in line:
            if pick == 0:
                total += val
    return total


def check_winners(cards):
    winning_indices = []
    for i, card in enumerate(cards):
        is_winner = False
        # Check complete rows
        for line in card:
            if all([x[1] for x in line]):
                #print("won with all lines: ", card, line)
                is_winner = True

        # Check complete columns
        for row in range(len(card[0])):
            if all([x[row][1] for x in card]):
                #print("won with row: ", card, row)
                is_winner = True
        if is_winner:
            winning_indices.append(i)

    return winning_indices



pick_list, cards = get_input("input.txt")
for i, pick in enumerate(pick_list):
    print(f"Pick {i}/{len(pick_list)}: {pick}")
    cards = pick_number(pick, cards)
    winning_indices = check_winners(cards)
    if winning_indices:
        print("Winning cards: ", winning_indices)
        for i in winning_indices[::-1]:
            winner = cards[i]
            del cards[i]
        print(len(cards), " cards remaining")
        if len(cards) == 0:
            break
    else:
        print("No winner with ", pick)
    print("------------")

card_totals = sum_unpicked_nums(winner)
print("------------")
print("WINNER\n")
for c in winner:
    print(c)
    print()
print("Score: ", card_totals * pick)
