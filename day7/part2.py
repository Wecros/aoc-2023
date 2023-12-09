#!/usr/bin/env python3

import fileinput
import re
from dataclasses import dataclass


@dataclass
class Hand:
    """A hand with its bid and rank."""

    cards: str
    bid: int
    rank: int = 0

    def calculate_winning(self):
        return self.bid * self.rank

    def __repr__(self):
        return f"{self.cards}:{self.rank}"


def main():
    hands_dict = {
        "fivekind": [],  # AAAAA
        "fourkind": [],  # AAAAB
        "fullhouse": [],  # AAABB
        "threekind": [],  # AAABC
        "twopair": [],  # AABBC
        "onepair": [],  # AABCD
        "highcard": [],  # ABCDE
    }

    for hand in parse_input():
        parse_hand(hand, hands_dict)

    highcards = sort_cards(hands_dict["highcard"])
    onepairs = sort_cards(hands_dict["onepair"])
    twopairs = sort_cards(hands_dict["twopair"])
    threekinds = sort_cards(hands_dict["threekind"])
    fullhouses = sort_cards(hands_dict["fullhouse"])
    fourkinds = sort_cards(hands_dict["fourkind"])
    fivekinds = sort_cards(hands_dict["fivekind"])

    concat_hands = highcards + onepairs + twopairs + threekinds + fullhouses + fourkinds + fivekinds

    curr_rank = 1
    for hand in concat_hands:
        hand.rank = curr_rank
        curr_rank += 1

    total_winnings = sum(hand.calculate_winning() for hand in concat_hands)
    print(total_winnings)


def parse_input():
    for line in fileinput.input():
        cards, strbid = line.strip().split()
        bid = int(strbid)
        yield Hand(cards, bid)


def parse_hand(hand: object, hands_dict):
    """
    Insert the card in the correct category in cards_dict.

    The problem is that "J" card means joker, so it can be any card.
    It will act as the best card for the hand - meaning QQQJ3 is a four of a kind - effectively QQQQ3.
    """
    cards = hand.cards

    # If there is a joker, replace it with the card that appears the most in the hand.
    if "J" in cards:
        card_with_most_occurrences = max(set(cards), key=cards.count)
        if card_with_most_occurrences == "J":
            cards_without_joker = cards.replace("J", "")
            if cards_without_joker:
                second_most_occurrences = max(cards_without_joker, key=cards.count)
                card_with_most_occurrences = second_most_occurrences
        cards = cards.replace("J", card_with_most_occurrences)

    category = "highcard"
    if len(set(cards)) == 1:
        category = "fivekind"
    elif any(cards.count(card) == 4 for card in cards):
        category = "fourkind"
    elif len(set(cards)) == 2:
        category = "fullhouse"
    elif any(cards.count(card) == 3 for card in cards):
        category = "threekind"
    elif len(set(cards)) == 3:
        category = "twopair"
    elif len(set(cards)) == 4:
        category = "onepair"

    hands_dict[category].append(hand)


def sort_cards(hands):
    """
    Sort cards by their first card. If first card is the same, sort by second card and so on.

    Order of cards is A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2.
    """
    order = "AKQT98765432J"
    sorted_hands = sorted(hands, key=lambda hand: [order.index(card) for card in hand.cards], reverse=True)
    return sorted_hands


if __name__ == "__main__":
    main()
