from CardFuncs import *

import random

card_num = 0;
card_deck = [];
num_plyr = 2
amt_chips = 100

class Player:
    def __init__(self, num_cards=0, num_aces=0, tot_hand=0):
        self.num_cards = num_cards;
        self.num_aces = num_aces;
        self.tot_hand = tot_hand
    def handtot(self):
        if self.num_aces > 0:
            if self.tot_hand > 21:
                self.tot_hand = self.tot_hand - 10;
                self.num_aces = self.num_aces - 1


def shuffle():
    global card_deck;
    global card_num;
    # for i in range(1, 9) :
    #     globals()['dlr_CS%s' % i].set("")
    #     globals()['user_CS%s' % i].set("")
    #     globals()['plA_CS%s' % i].set("")
    #     globals()['plB_CS%s' % i].set("")
    #     # globals()['plC_CS%s' % i].set("")

    card_deck = get_cards(3);
    card_num = 3 * 52

def get_card():
    global card_num;
    global card_deck;
    # card = card_deck.pop(38);
    card = card_deck.pop(random.randint(0, card_num));
    card_num -= 1;
    if len(card) == 3:
        card_val = card[:2]
    else:
        card_val = card[0]
    card_suit = card[-1]
    return card_val, card_suit


def deal_cards():
    global amt_chips;
    num_plyr = 2
    amt_chips -= 10;
    dlr_CS1 = "X";
    dlr_CS2 = "X";
    for i in range(3 + 2 * num_plyr):
        card_val, card_suit = get_card();
        if i == 0:
            dlr_CS3 = card_val;
            dlr_CS4 = card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0 = Player(1, num_A, get_cval(card_val))
        elif i == 1:
            user_CS1 = card_val;
            user_CS2 = card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player1 = Player(1, num_A, get_cval(card_val))
        elif i == 2:
            user_CS3 = card_val;
            user_CS4 = card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player1.num_cards = 2;
            Player1.num_aces += num_A;
            Player1.tot_hand += get_cval(card_val)
        if num_plyr == 0:
            continue
        elif i == 3:
            plA_CS1 = card_val;
            plA_CS2 = card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2 = Player(1, num_A, get_cval(card_val))
        elif i == 4:
            plA_CS3 = card_val;
            plA_CS4 = card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 2;
            Player2.num_aces += num_A;
            Player2.tot_hand += get_cval(card_val)
        if num_plyr == 1:
            continue
        elif i == 5:
            plB_CS1 = card_val;
            plB_CS2 = card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3 = Player(1, num_A, get_cval(card_val))
        elif i == 6:
            plB_CS3 = card_val;
            plB_CS4 = card_suit;
            Player3.num_cards = 2;
            Player3.num_aces += num_A;
            Player3.tot_hand += get_cval(card_val)

def hit():
    card_val, card_suit = get_card()
    if Player1.num_cards == 2:
        user_CS5.set(card_val);
        user_CS6.set(card_suit)
        user.num_cards = 3;
        user.tot_hand += get_cval(card_val)
    if Player1.num_cards == 3:
        user_CS7.set(card_val);
        user_CS8.set(card_suit)
        user.num_cards = 4;
        user.tot_hand += get_cval(card_val)

def plr1_hit():
    while num_plyr >= 1 and Player2.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player2.num_cards == 2:
            plA_CS5 = card_val;
            plA_CS6 = card_suit;
            Player2.num_cards = 3;
            Player2.tot_hand += get_cval(card_val)
        if Player2.num_cards == 3:
            plA_CS7 = card_val;
            plA_CS8 = card_suit
            Player2.num_cards = 4;
            Player2.tot_hand += get_cval(card_val)

def plr2_hit():
    while num_plyr >= 2 and Player3.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player3.num_cards == 2:
            plB_CS5 = card_val;
            plB_CS6 = card_suit;
            Player3.num_cards = 3;
            Player3.tot_hand += get_cval(card_val)
        if Player2.num_cards == 3:
            plB_CS7 = card_val;
            plB_CS8 = card_suit
            Player3.num_cards = 4;
            Player3.tot_hand += get_cval(card_val)

def plr3_hit():
    while num_plyr == 3 and Player4.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player4.num_cards == 2:
            plA_CS5 = card_val;
            plA_CS6 = card_suit;
            Player4.num_cards = 3;
            Player4.tot_hand += get_cval(card_val)
        if Player4.num_cards == 3:
            plA_CS7 = card_val;
            plA_CS8 = card_suit
            Player4.num_cards = 4;
            Player4.tot_hand += get_cval(card_val)

def dlr_play ():
    card_val, card_suit = get_card();
    dlr_CS1 = card_val;
    dlr_CS2 = card_suit;
    if (card_val == "A"):
        num_A = 1
    else:
        num_A = 0
    Player0.num_cards = 2;
    Player0.num_aces += num_A;
    Player0.tot_hand += get_cval(card_val)
    while Player0.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player0.num_cards == 2:
            dlr_CS5 = card_val;
            dlr_CS6 = card_suit;
            Player0.num_cards = 3;
            Player0.tot_hand += get_cval(card_val)
        if Player4.num_cards == 3:
            dlr_CS7 = card_val;
            dlr_CS8 = card_suit
            Player0.num_cards = 4;
            Player0.tot_hand += get_cval(card_val)
    hand_comp = Player0.tot_hand - Player1.tot_hand;
    if hand_comp > 0:
        print("Dealer wins")
    elif hand_comp == 0:
        print("Push from dealer");
        amt_chips += 10;
    else:
        print("Player wins");
        amt_chips += 20




shuffle();
deal_cards();

if num_plyr >= 1:
    plr1_hit();

if num_plyr >= 2:
    plr2_hit();

if num_plyr == 3:
    plr3_hit();

