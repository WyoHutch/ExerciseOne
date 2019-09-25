from CardFuncs import *

import random

num_decks = 3;
num_plyr = 2;
amt_chips = "$100";
card_num = 0;
card_deck = [];

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
        # globals()['dlr_CS%s' % i].set("")
        # globals()['user_CS%s' % i].set("")
        # globals()['plA_CS%s' % i].set("")
        # globals()['plB_CS%s' % i].set("")
        # globals()['plC_CS%s' % i].set("")
    # card_deck = CardFuncs.get_cards(int(num_decks.get()));
    card_deck = get_cards(num_decks);
    # card_num = int(num_decks.get()) * 52
    card_num = 3 * 52

def get_card():
    global card_num;
    global card_deck;
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
    global Player0;
    global Player1;
    global Player2;
    global Player3;
    global Player4;
    global num_plyr;

    # num_plyr = int(num_players.get())
    dlr_CS1 = "XX";
    # amt_txt = amt_chips.get();
    amt_txt = amt_chips;
    amtVal = int(amt_txt[1:]);
    amtNew = amtVal - 10;
    amt_chips = "$" + str(amtNew);
    # amt_chips -= "$" + str(int(amt_txt[1:]) - 10);
    for i in range(3 + 2 * num_plyr):
        card_val, card_suit = get_card();
        if i == 0:
            # dlr_CS2.set(card_val + card_suit);
            dlr_CS2 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0.num_cards = 1;
            Player0.num_aces = num_A;
            Player0.tot_hand = get_cval(card_val)
        elif i == 1:
            # user_CS1.set(card_val + card_suit);
            user_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            # Player1 = Player(1, num_A, CardFuncs.get_cval(card_val))
            Player1.num_aces = num_A;
            Player1.tot_hand = get_cval(card_val)
        elif i == 2:
            # user_CS2.set(card_val + card_suit);
            user_CS2 = card_val + card_suit;
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
            # plA_CS1.set(card_val + card_suit);
            plA_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_aces = num_A;
            Player2.tot_hand = get_cval(card_val)
        elif i == 4:
            # plA_CS2.set(card_val + card_suit);
            plA_CS2 = card_val + card_suit;
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
            # plB_CS1.set(card_val + card_suit);
            plB_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_aces = num_A;
            Player3.tot_hand = get_cval(card_val)
        elif i == 6:
            # plB_CS2.set(card_val + card_suit);
            plB_CS2 = card_val + card_suit;
            Player3.num_cards = 2;
            Player3.num_aces += num_A;
            Player3.tot_hand += get_cval(card_val)

def hit():
    global Player1;
    card_val, card_suit = get_card()
    if Player1.num_cards == 2:
        # user_CS3.set(card_val + card_suit);
        user_CS3 = card_val + card_suit;
        if (card_val == "A"):
            num_A = 1
        else:
            num_A = 0
        Player1.num_cards = 3;
        if num_A ==1: Player1.num_aces += 1
        # Player1.tot_hand += CardFuncs.get_cval(card_val)
        Player1.tot_hand += get_cval(card_val)
    if Player1.num_cards == 3:
        # user_CS4.set(card_val + card_suit);
        user_CS4 = card_val + card_suit;
        if (card_val == "A"):
            num_A = 1
        else:
            num_A = 0
        Player1.num_cards = 4;
        if num_A ==1: Player1.num_aces += 1
        # Player1.tot_hand += CardFuncs.get_cval(card_val)
        Player1.tot_hand += get_cval(card_val)
    if Player2.tot_hand > 21:
        print("Player A BUSTED")


def plr1_hit():
    global Player2;
    while num_plyr >= 1 and Player2.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player2.num_cards == 2:
            # plA_CS3.set(card_val + card_suit);
            plA_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 3;
            if num_A ==1: Player2.num_aces += 1
            # Player2.tot_hand += CardFuncs.get_cval(card_val)
            Player2.tot_hand += get_cval(card_val)
        if Player2.num_cards == 3:
            # plA_CS4.set(card_val + card_suit);
            plA_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 4;
            if num_A ==1: Player2.num_aces += 1
            # Player2.tot_hand += CardFuncs.get_cval(card_val)
            Player2.tot_hand += get_cval(card_val)
            break;
    if Player2.tot_hand > 21:
        print("Player A BUSTED")

def plr2_hit():
    global Player3;
    while num_plyr >= 2 and Player3.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player3.num_cards == 2:
            # plB_CS3.set(card_val + card_suit);
            plB_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_cards = 3;
            if num_A ==1: Player3.num_aces += 1
            # Player3.tot_hand += CardFuncs.get_cval(card_val)
            Player3.tot_hand += get_cval(card_val)
        if Player3.num_cards == 3:
            # plB_CS4.set(card_val + card_suit);
            plB_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_cards = 4;
            if num_A ==1: Player3.num_aces += 1
            # Player3.tot_hand += CardFuncs.get_cval(card_val)
            Player3.tot_hand += get_cval(card_val)
            break;
    if Player3.tot_hand > 21:
        print("Player B BUSTED")

def plr3_hit():
    global Player4;
    while num_plyr == 3 and Player4.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player4.num_cards == 2:
            # plC_CS3.set(card_val + card_suit);
            plC_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player4.num_cards = 3;
            if num_A ==1: Player4.num_aces += 1
            # Player4.tot_hand += CardFuncs.get_cval(card_val)
            Player4.tot_hand += get_cval(card_val)
        if Player4.num_cards == 3:
            # plC_CS4.set(card_val + card_suit);
            plC_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player4.num_cards = 4;
            if num_A ==1: Player4.num_aces += 1
            # Player4.tot_hand += CardFuncs.get_cval(card_val)
            Player4.tot_hand += get_cval(card_val)
            break;
    if Player4.tot_hand > 21:
        print("Player C BUSTED")

def dlr_play ():
    global Player0;
    card_val, card_suit = get_card();
    dlr_CS1 = card_val + card_suit;
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
            dlr_CS3.set(card_val + card_suit);
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0.num_cards = 3;
            if num_A ==1: Player0.num_aces += 1
            Player0.tot_hand += get_cval(card_val)
        if Player4.num_cards == 3:
            dlr_CS4.set(card_val + card_suit);
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0.num_cards = 4;
            if num_A ==1: Player0.num_aces += 1
            Player0.tot_hand += get_cval(card_val)
    hand_comp = Player0.tot_hand - Player1.tot_hand;
    if hand_comp > 0:
        print("Dealer wins")
    elif hand_comp == 0:
        print("Push from dealer");
        amt_txt = amt_chips.get();
        amt_chips -= "$" + str(int(amt_txt[1:]) + 10);
    else:
        print("Player wins");
        amt_txt = amt_chips.get();
        amt_chips -= "$" + str(int(amt_txt[1:]) + 20);


Player0 = Player();
Player1 = Player();
if num_plyr >= 1:
    Player2 = Player()
if num_plyr >= 2:
    Player3 = Player()
if num_plyr == 3:
    Player4 = Player()

shuffle();
deal_cards();

if num_plyr >= 1:
    plr1_hit();

if num_plyr >= 2:
    plr2_hit();

# if num_plyr == 3:
#     plr3_hit();

