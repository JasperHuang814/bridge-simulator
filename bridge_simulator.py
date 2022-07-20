#!/usr/bin/env python
# coding: utf-8
import random

suit_list = ["S", "H", "D", "C"]
suit_dict = {suit_list[i]: i for i in range(len(suit_list))}
num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
num_dict = {num_list[i]: i for i in range(len(num_list))}

# point_dict = {1: 4, 13: 3, 12: 2, 11: 1}
order_list = ["n", "e", "s", "w"]


class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        return f"{self.suit}{self.num}"

    def __repr__(self):
        return f"{self.suit}{self.num}"


class Player:
    def __init__(self, card_list: list[Card], position: str):
        self.card_list = sort_by_num(sort_by_suit(card_list))
        self.played_card_list = []
        self.position = position

    def play(self, pre_card=None):
        card_return = None
        largest_card = pre_card
        compare = False
        if pre_card is not None:
            for card in self.card_list:
                if card.suit == pre_card.suit and num_dict[card.num] > num_dict[pre_card.num]:
                    card_return = card
                    largest_card = card
                    compare = True
                    break
        else:
            compare = True
            largest_card = self.card_list[0]
        if card_return is None:
            card_return = self.card_list[0]
        self.card_list.remove(card_return)
        self.played_card_list.append(card_return)
        return card_return, largest_card, compare

    def __str__(self):
        return f"Position: {self.position} \nCard List: {self.card_list} \nPlayed Card: {self.played_card_list}"

    def __repr__(self):
        return f"Position: {self.position} \nCard List: {self.card_list} \nPlayed Card: {self.played_card_list}"


def sort_by_suit(card_list):
    card_list.sort(key=lambda card: suit_dict[card.suit], reverse=True)
    return card_list


def sort_by_num(card_list):
    card_list.sort(key=lambda x: num_dict[x.num])
    return card_list


def generate_random_poker_list():
    p_list = []
    for num in range(1, 14):
        p_list.append(Card(num, "S"))
        p_list.append(Card(num, "H"))
        p_list.append(Card(num, "D"))
        p_list.append(Card(num, "C"))
    random.shuffle(p_list)
    return p_list


def deal_card(p_list):
    n = []
    w = []
    s = []
    e = []
    for i in range(0, 52, 4):
        n.append(p_list[i])
        w.append(p_list[i + 1])
        s.append(p_list[i + 2])
        e.append(p_list[i + 3])
    return Player(n, "N"), Player(w, "W"), Player(s, "S"), Player(e, "E")
