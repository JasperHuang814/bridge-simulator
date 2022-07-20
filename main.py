import random

# Simulator For Bridge

# S stands for Space
# H stands for Heart
# D stands for Diamond
# C stands for Club


class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        return f"{self.suit}{self.num}"

    def __repr__(self):
        return f"{self.suit}{self.num}"

    def __lt__(self, other):
        return compare_card(self, other)


suit_list = ["S", "H", "D", "C"]
num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]


def compare_card(a: Card, b: Card):
    if num_list.index(a.num) < num_list.index(b.num):
        return True
    elif num_list.index(a.num) > num_list.index(b.num):
        return False
    elif suit_list.index(a.suit) > suit_list.index(b.suit):
        return True
    else:
        return False


poker_list = []

for i in range(1, 14):
    poker_list.append(Card(i, "S"))
    poker_list.append(Card(i, "H"))
    poker_list.append(Card(i, "D"))
    poker_list.append(Card(i, "C"))


if __name__ == '__main__':
    random.shuffle(poker_list)
    print([poker for poker in poker_list])
    if poker_list[0] < poker_list[1]:
        print("Smaller")
