import CardFuncs

import random

from tkinter import *
from tkinter import ttk

card_num = 0;
card_deck = [];
hit_num = 0;
cards_inhand = {}

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
    for i in range(1, 9) :
        globals()['dlr_CS%s' % i].set("")
        globals()['user_CS%s' % i].set("")
        globals()['plA_CS%s' % i].set("")
        globals()['plB_CS%s' % i].set("")
        # globals()['plC_CS%s' % i].set("")

    card_deck = CardFuncs.get_cards(int(num_decks.get()));
    card_num = int(num_decks.get()) * 52

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

def get_cval(cardv):
    if cardv == "J" or cardv == "Q" or cardv == "K":
        return 10
    elif cardv == "A":
        return 11
    else:
        return int(cardv)


def deal_cards():
    num_plyr = int(num_players.get())
    for i in range(3 + 2 * num_plyr):
        card_val, card_suit = get_card();
        if i == 0:
            user_CS1.set(card_val);
            user_CS2.set(card_suit);
            num_A = 1 if card_val = "A" else num_A = 0
            Player1 = Player(1, num_A, get_cval(card_val))
        elif i == 1:
            user_CS3.set(card_val);
            user_CS4.set(card_suit);
            num_A = 1 if card_val = "A" else num_A = 0
            Player1.num_cards = 2;
            Player1.num_aces += num_A;
            Player1.tot_hand += get_cval(card_val)
        elif i == 2:
            dlr_CS1.set("X");
            dlr_CS2.set("X");
        elif i == 3:
            dlr_CS3.set(card_val);
            dlr_CS4.set(card_suit);
            num_A = 1 if card_val = "A" else num_A = 0
            Player0 = Player(1, num_A, get_cval(card_val))
        if num_plyr == 0:
            continue
        elif i == 4:
            plA_CS1.set(card_val);
            plA_CS2.set(card_suit);
            num_A = 1 if card_val = "A" else num_A = 0
            Player2 = Player(1, num_A, get_cval(card_val))
        elif i == 5:
            plA_CS3.set(card_val);
            plA_CS4.set(card_suit);
            num_A = 1 if card_val = "A" else num_A = 0
            Player2.num_cards = 2;
            Player2.num_aces += num_A;
            Player2.tot_hand += get_cval(card_val)
        if num_plyr == 1:
            continue
        elif i == 6:
            plB_CS1.set(card_val);
            plB_CS2.set(card_suit);
            num_A = 1 if card_val = "A" else num_A = 0
            Player3 = Player(1, num_A, get_cval(card_val))
        elif i == 7:
            plB_CS3.set(card_val);
            plB_CS4.set(card_suit);
            Player3.num_cards = 2;
            Player3.num_aces += num_A;
            Player3.tot_hand += get_cval(card_val)
def hit():
    global hit_num;
    card_val, card_suit = get_card()
    if hit_num == 0:
        user_CS5.set(card_val);
        user_CS6.set(card_suit)
        hit_num += 1;
    if hit_num == 1:
        user_CS7.set(card_val);
        user_CS8.set(card_suit)

def hand_tot(plyr):
    if plyr == 0:
        pl_hand = "dlr_CS";
    elif plyr == 1:
        pl_hand = "user_CS";
    elif plyr == 2:
        pl_hand = "plA_CS";
    elif plyr == 3:
        pl_hand = "plB_CS";
    else:
        pl_hand = "plC_CS";
    

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
ttk.Button(mainframe, text="Get Odds", command=hit).grid(column=9, row=34, sticky=S)

dlr_CS1 = StringVar();
dlr_CS2 = StringVar();
dlr_CS3 = StringVar();
dlr_CS4 = StringVar();
dlr_CS5 = StringVar();
dlr_CS6 = StringVar();
dlr_CS7 = StringVar();
dlr_CS8 = StringVar();
ttk.Label(mainframe, width=6, text="Dealer").grid(column=0, row=6, sticky=N)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=dlr_CS1).grid(column=1, row=6, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=dlr_CS2).grid(column=2, row=6, padx=0, sticky=W)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=dlr_CS3).grid(column=1, row=7, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=dlr_CS4).grid(column=2, row=7, padx=0, sticky=W)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=dlr_CS5).grid(column=1, row=8, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=dlr_CS6).grid(column=2, row=8, padx=0, sticky=W)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=dlr_CS7).grid(column=1, row=9, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=dlr_CS8).grid(column=2, row=9, padx=0, sticky=W)

user_CS1 = StringVar();
user_CS2 = StringVar();
user_CS3 = StringVar();
user_CS4 = StringVar();
user_CS5 = StringVar();
user_CS6 = StringVar();
user_CS7 = StringVar();
user_CS8 = StringVar();
ttk.Label(mainframe, width=6, text="User").grid(column=5, columnspan=2, row=30, sticky=N)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=user_CS1).grid(column=3, row=28, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=user_CS2).grid(column=4, row=28, padx=0, sticky=W)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=user_CS3).grid(column=5, row=28, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=user_CS4).grid(column=6, row=28, padx=0, sticky=W)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=user_CS5).grid(column=7, row=28, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=user_CS6).grid(column=8, row=28, padx=0, sticky=W)
ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=user_CS7).grid(column=9, row=28, padx=0, sticky=E)
ttk.Label(mainframe, width=3, justify=LEFT, textvariable=user_CS8).grid(column=10, row=28, padx=0, sticky=W)

if int(num_players.get()) > 0:
    plA_CS1 = StringVar();
    plA_CS2 = StringVar();
    plA_CS3 = StringVar();
    plA_CS4 = StringVar();
    plA_CS5 = StringVar();
    plA_CS6 = StringVar();
    plA_CS7 = StringVar();
    plA_CS8 = StringVar();
    ttk.Label(mainframe, text="Player A").grid(column=6, columnspan=2,  row=4, sticky=N)
    ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=plA_CS1).grid(column=6, row=5, sticky=W)
    ttk.Label(mainframe, width=3, justify=LEFT, textvariable=plA_CS2).grid(column=6, row=5, sticky=E)
    ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=plA_CS3).grid(column=6, row=6, sticky=W)
    ttk.Label(mainframe, width=3, justify=LEFT, textvariable=plA_CS4).grid(column=6, row=6, sticky=E)
    ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=plA_CS5).grid(column=6, row=7, sticky=W)
    ttk.Label(mainframe, width=3, justify=LEFT, textvariable=plA_CS6).grid(column=6, row=7, sticky=E)
    ttk.Label(mainframe, width=3, justify=RIGHT, textvariable=plA_CS7).grid(column=6, row=8, sticky=W)
    ttk.Label(mainframe, width=3, justify=LEFT, textvariable=plA_CS8).grid(column=6, row=8, sticky=E)

if int(num_players.get()) > 1:
    plB_CS1 = StringVar();
    plB_CS2 = StringVar();
    plB_CS3 = StringVar();
    plB_CS4 = StringVar();
    plB_CS5 = StringVar();
    plB_CS6 = StringVar();
    plB_CS7 = StringVar();
    plB_CS8 = StringVar();
    ttk.Label(mainframe, text="Player B").grid(column=9, columnspan=2,  row=4, sticky=N)
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plB_CS1).grid(column=8, row=5, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plB_CS2).grid(column=8, row=5, sticky=E)
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plB_CS3).grid(column=8, row=6, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plB_CS4).grid(column=8, row=6, sticky=E)
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plB_CS5).grid(column=8, row=7, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plB_CS6).grid(column=8, row=7, sticky=E)
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plB_CS7).grid(column=8, row=8, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plB_CS8).grid(column=8, row=8, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=5)

decks.focus()
# root.bind('<Return>', calculate)

root.mainloop()