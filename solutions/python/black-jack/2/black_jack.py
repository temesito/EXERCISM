"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    value = 0
    if card in {"J", "Q","K"}:
        value = 10
    elif card == "A":
        value = 1
    else:
        card = int(card)
        if card <2 or card >10: 
            raise ValueError("please enter a valid card")
        elif card >=2 or card <=10:
            value = card
    return value

    
def higher_card(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one < value_card_two:
        value_card_two = str(value_card_two)
        return card_two
    elif value_card_one == value_card_two:
        value_card_one = str(value_card_one)
        value_card_two = str(value_card_two)
        return card_one, card_two
    else:
        value_card_one = str(value_card_one)
        return card_one


def value_of_ace(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if (value_card_one + value_card_two + 10) < 21:
        if card_one == "A" or card_two == "A":
            return 1
        else:
            return 11
    else:
        return 1



def is_blackjack(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one == 1 and value_card_two == 10:
        value_card_one = 11
        if (value_card_one + value_card_two) == 21:
            return True
    elif value_card_two == 1 and value_card_one == 10:
        value_card_two = 11
        if (value_card_one + value_card_two) == 21:
            return True
    elif (value_card_one + value_card_two) == 21:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one == value_card_two:
        return True
    else:
        return False

def can_double_down(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if (value_card_one + value_card_two) >= 9 and (value_card_one + value_card_two) <= 11:
        return True
    else:
        return False
