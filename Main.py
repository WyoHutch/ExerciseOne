import CardFuncs

import random

from tkinter import *
from tkinter import ttk

card_num = 0;
card_deck = [];
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
    for i in range(1, 5) :
        globals()['dlr_CS%s' % i].set("")
        globals()['user_CS%s' % i].set("")
        globals()['plA_CS%s' % i].set("")
        globals()['plB_CS%s' % i].set("")
        # globals()['plC_CS%s' % i].set("")
    card_deck = CardFuncs.get_cards(int(num_decks.get()));
    # card_deck = get_cards(num_decks);
    card_num = int(num_decks.get()) * 52
    # card_num = 3 * 52

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

    dlr_CS1 = "XX";
    amt_txt = amt_chips.get();
    # amt_txt = amt_chips;
    amtVal = int(amt_txt[1:]);
    amtNew = amtVal - 10;
    amt_chips.set("$" + str(amtNew));
    # amt_chips -= "$" + str(int(amt_txt[1:]) - 10);
    for i in range(3 + 2 * num_plyr):
        card_val, card_suit = get_card();
        if i == 0:
            dlr_CS2.set(card_val + card_suit);
            # dlr_CS2 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0.num_cards = 1;
            Player0.num_aces = num_A;
            Player0.tot_hand = CardFuncs.get_cval(card_val)
        elif i == 1:
            user_CS1.set(card_val + card_suit);
            # user_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player1.num_aces = num_A;
            Player1.tot_hand = CardFuncs.get_cval(card_val)
        elif i == 2:
            user_CS2.set(card_val + card_suit);
            # user_CS2 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player1.num_cards = 2;
            Player1.num_aces += num_A;
            Player1.tot_hand += CardFuncs.get_cval(card_val)
        if num_plyr == 0:
            continue
        elif i == 3:
            plA_CS1.set(card_val + card_suit);
            # plA_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_aces = num_A;
            Player2.tot_hand = CardFuncs.get_cval(card_val)
        elif i == 4:
            plA_CS2.set(card_val + card_suit);
            # plA_CS2 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 2;
            Player2.num_aces += num_A;
            Player2.tot_hand += CardFuncs.get_cval(card_val)
        if num_plyr == 1:
            continue
        elif i == 5:
            plB_CS1.set(card_val + card_suit);
            # plB_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_aces = num_A;
            Player3.tot_hand = CardFuncs.get_cval(card_val)
        elif i == 6:
            plB_CS2.set(card_val + card_suit);
            # plB_CS2 = card_val + card_suit;
            Player3.num_cards = 2;
            Player3.num_aces += num_A;
            Player3.tot_hand += CardFuncs.get_cval(card_val)

def hit():
    global Player1;
    card_val, card_suit = get_card()
    if Player1.num_cards == 2:
        user_CS3.set(card_val + card_suit);
        # user_CS3 = card_val + card_suit;
        if (card_val == "A"):
            num_A = 1
        else:
            num_A = 0
        Player1.num_cards = 3;
        if num_A ==1: Player1.num_aces += 1
        Player1.tot_hand += CardFuncs.get_cval(card_val)
    if Player1.num_cards == 3:
        user_CS4.set(card_val + card_suit);
        # user_CS4 = card_val + card_suit;
        if (card_val == "A"):
            num_A = 1
        else:
            num_A = 0
        Player1.num_cards = 4;
        if num_A ==1: Player1.num_aces += 1
        Player1.tot_hand += CardFuncs.get_cval(card_val)
    if Player2.tot_hand > 21:
        print("Player A BUSTED")

def plyr_cont():
    

def plr1_hit():
    global Player2;
    while num_plyr >= 1 and Player2.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player2.num_cards == 2:
            plA_CS3.set(card_val + card_suit);
            # plA_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 3;
            if num_A ==1: Player2.num_aces += 1
            Player2.tot_hand += CardFuncs.get_cval(card_val)
        if Player2.num_cards == 3:
            plA_CS4.set(card_val + card_suit);
            # plA_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 4;
            if num_A ==1: Player2.num_aces += 1
            Player2.tot_hand += CardFuncs.get_cval(card_val)
            break;
    if Player2.tot_hand > 21:
        print("Player A BUSTED")

def plr2_hit():
    global Player3;
    while num_plyr >= 2 and Player3.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player3.num_cards == 2:
            plB_CS3.set(card_val + card_suit);
            # plB_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_cards = 3;
            if num_A ==1: Player3.num_aces += 1
            Player3.tot_hand += CardFuncs.get_cval(card_val)
        if Player3.num_cards == 3:
            plB_CS4.set(card_val + card_suit);
            # plB_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_cards = 4;
            if num_A ==1: Player3.num_aces += 1
            Player3.tot_hand += CardFuncs.get_cval(card_val)
            break;
    if Player3.tot_hand > 21:
        print("Player B BUSTED")

def plr3_hit():
    global Player4;
    while num_plyr == 3 and Player4.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player4.num_cards == 2:
            plC_CS3.set(card_val + card_suit);
            # plC_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player4.num_cards = 3;
            if num_A ==1: Player4.num_aces += 1
            Player4.tot_hand += CardFuncs.get_cval(card_val)
        if Player4.num_cards == 3:
            plC_CS4.set(card_val + card_suit);
            # plC_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player4.num_cards = 4;
            if num_A ==1: Player4.num_aces += 1
            Player4.tot_hand += CardFuncs.get_cval(card_val)
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
    Player0.tot_hand += CardFuncs.get_cval(card_val)
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
            Player0.tot_hand += CardFuncs.get_cval(card_val)
        if Player4.num_cards == 3:
            dlr_CS4.set(card_val + card_suit);
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0.num_cards = 4;
            if num_A ==1: Player0.num_aces += 1
            Player0.tot_hand += CardFuncs.get_cval(card_val)
    hand_comp = Player0.tot_hand - Player1.tot_hand;
    if hand_comp == 0:
        amt_txt = amt_chips.get();
        amt_chips.set("$" + str(int(amt_txt[1:]) + 10));
    else:
        amt_txt = amt_chips.get();
        amt_chips.set("$" + str(int(amt_txt[1:]) + 20));


root = Tk()
root.title("Casino BlackJack Odds")
root.geometry("800x600")

mainframe = ttk.Frame(root, padding="4 8 4 8")
mainframe.grid(columnspan = 1, rowspan = 1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

card_deck = [];

num_decks = StringVar();
ttk.Label(mainframe, text="Number of card decks to be used").grid(column=0, row=0, columnspan=7, sticky=W)
decks = ttk.Entry(mainframe, width=5, justify=RIGHT, textvariable=num_decks)
decks.grid(column=8, row=0, sticky=(W))
decks.insert(0, "2")

num_players = StringVar();
ttk.Label(mainframe, width=13, text="Number of other players").grid(column=5, row=0, columnspan=6, sticky=E)
players = ttk.Entry(mainframe, width=5, justify=RIGHT, textvariable=num_players)
players.grid(column=15, row=0, sticky=(E))
players.insert(0, "2")

ttk.Button(mainframe, text="Shuffle", command=shuffle).grid(column=0, row=3, sticky=S)
ttk.Button(mainframe, text="Deal", command=deal_cards).grid(column=0, row=4, sticky=S)
ttk.Button(mainframe, text="-Hit-", command=hit).grid(column=7, row=32, sticky=S)
ttk.Button(mainframe, text="Get Odds", command=get_odds).grid(column=9, row=34, sticky=S)
ttk.Button(mainframe, text="Get Odds", command=plyr_cont).grid(column=9, row=34, sticky=S)

dlr_CS1 = StringVar();
dlr_CS2 = StringVar();
dlr_CS3 = StringVar();
dlr_CS4 = StringVar();
ttk.Label(mainframe, width=6, text="Dealer").grid(column=0, row=6, sticky=N)
ttk.Label(mainframe, textvariable=dlr_CS1).grid(column=2, row=6, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS2).grid(column=2, row=7, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS3).grid(column=2, row=8, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS4).grid(column=2, row=9, padx=0, sticky=W)

user_CS1 = StringVar();
user_CS2 = StringVar();
user_CS3 = StringVar();
user_CS4 = StringVar();
ttk.Label(mainframe, width=6, text="User").grid(column=5, columnspan=2, row=30, sticky=N)
ttk.Label(mainframe, textvariable=user_CS1).grid(column=4, row=28, padx=0, sticky=S)
ttk.Label(mainframe, textvariable=user_CS2).grid(column=5, row=28, padx=0, sticky=S)
ttk.Label(mainframe, textvariable=user_CS3).grid(column=6, row=28, padx=0, sticky=S)
ttk.Label(mainframe, textvariable=user_CS4).grid(column=7, row=28, padx=0, sticky=S)

amt_chips = StringVar();
ttk.Label(mainframe, text="Amount in Player chips:").grid(column=0, row=32, sticky=W)
ttk.Label(mainframe, textvariable=amt_chips).grid(column=3, row=32, sticky=W)
amt_chips.set("$100")

plA_text = StringVar();
plA_CS1 = StringVar();
plA_CS2 = StringVar();
plA_CS3 = StringVar();
plA_CS4 = StringVar();
ttk.Label(mainframe, textvariable=plA_text).grid(column=6, columnspan=2,  row=4, sticky=N)
ttk.Label(mainframe, textvariable=plA_CS1).grid(column=6, row=5, sticky=E)
ttk.Label(mainframe, textvariable=plA_CS2).grid(column=6, row=6, sticky=E)
ttk.Label(mainframe, textvariable=plA_CS3).grid(column=6, row=7, sticky=E)
ttk.Label(mainframe, textvariable=plA_CS4).grid(column=6, row=8, sticky=E)

plB_text = StringVar();
plB_CS1 = StringVar();
plB_CS2 = StringVar();
plB_CS3 = StringVar();
plB_CS4 = StringVar();
ttk.Label(mainframe, textvariable=plB_text).grid(column=8, columnspan=2,  row=4, sticky=N)
ttk.Label(mainframe, textvariable=plB_CS1).grid(column=8, row=5, sticky=E)
ttk.Label(mainframe, textvariable=plB_CS2).grid(column=8, row=6, sticky=E)
ttk.Label(mainframe, textvariable=plB_CS3).grid(column=8, row=7, sticky=E)
ttk.Label(mainframe, textvariable=plB_CS4).grid(column=8, row=8, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=5)

decks.focus()
# root.bind('<Return>', calculate)

num_plyr = int(num_players.get())

Player0 = Player();
Player1 = Player();
if num_plyr >= 1:
    plA_text.set("Player A")
    Player2 = Player()
if num_plyr >= 2:
    plB_text.set("Player B")
    Player3 = Player()
# if num_plyr == 3:
    # plC_text.set("Player C")
#     Player4 = Player()

root.mainloop()
