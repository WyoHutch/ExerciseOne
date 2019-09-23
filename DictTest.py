import CardFuncs

import random

card_num = 0;
card_deck = [];

def shuffle():
    global card_num
    global card_deck
    card_deck = CardFuncs.get_cards(3)
    card_num = 3 * 52

def deal_cards():
    global card_num
    global card_deck
    num_plyr = 1
    print(card_num)
    for i in range(4 + 2 * num_plyr):
        c_ind = random.randint(0, card_num)
        card = card_deck.pop(c_ind)
        if len(card) == 3:
            card_val = card[:2]
        else:
            card_val = card[0]
        card_suit = card[-1]
        card_num -= 1

        if i == 0:
            user_CS1 = card_val;
            user_CS2 = card_suit;
        elif i == 1:
            user_CS3 = card_val;
            user_CS4 = card_suit;
        elif i == 2:
            dlr_CS1 = card_val;
            dlr_CS2 = card_suit;
        elif i == 3:
            dlr_CS3 = card_val;
            dlr_CS4 = card_suit;
        if num_plyr == 0:
            continue
        elif i == 4:
            plA_CS1 = card_val;
            plA_CS2 = card_suit;
        elif i == 5:
            plA_CS3 = card_val;
            plA_CS4 = card_suit;
        if num_plyr == 1:
            continue
        elif i == 6:
            plB_CS1 = card_val;
            plB_CS2 = card_suit;
        elif i == 7:
            plB_CS3 = card_val;
            plAB_CS4 = card_suit;


shuffle()
deal_cards()
print(card_num)