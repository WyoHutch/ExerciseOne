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
    def __init__(self, num_cards=0, num_aces=0, tot_hand=0, arrCard = []):
        self.num_cards = num_cards;
        self.num_aces = num_aces;
        self.tot_hand = tot_hand
    def handtot(self):
        if self.num_aces > 0:
            if self.tot_hand > 21:
                self.tot_hand = self.tot_hand - 10;
                self.num_aces = self.num_aces - 1

def clr_msg():
    global num_plyr
    Player0.num_cards = 0
    Player0.num_aces = 0
    Player0.tot_hand = 0
    Player0.arrCard = []
    Player1.num_cards = 0
    Player1.num_aces = 0
    Player1.tot_hand = 0
    Player1.arrCard = []
    if num_plyr >= 1:
        Player2.num_cards = 0
        Player2.num_aces = 0
        Player2.tot_hand = 0
        Player2.arrCard = []
    if num_plyr >= 2:
        Player3.num_cards = 0
        Player3.num_aces = 0
        Player3.tot_hand = 0
        Player3.arrCard = []
    if num_plyr == 3:
        Player4.num_cards = 0
        Player4.num_aces = 0
        Player4.tot_hand = 0
        Player4.arrCard = []
    dlr_CS1.set("")
    dlr_CS2.set("")
    dlr_CS3.set("")
    dlr_CS4.set("")
    dlr_score.set("")
    user_CS1.set("")
    user_CS2.set("")
    user_CS3.set("")
    user_CS4.set("")
    user_score.set("")
    plA_CS1.set("")
    plA_CS2.set("")
    plA_CS3.set("")
    plA_CS4.set("")
    plA_score.set("")
    plB_CS1.set("")
    plB_CS2.set("")
    plB_CS3.set("")
    plB_CS4.set("")
    plB_score.set("")
    plC_CS1.set("")
    plC_CS2.set("")
    plC_CS3.set("")
    plC_CS4.set("")
    plC_score.set("")

def shuffle():
    global card_deck;
    global card_num;
    clr_msg();
    for i in range(1, 5) :
        globals()['dlr_CS%s' % i].set("")
        globals()['user_CS%s' % i].set("")
        globals()['plA_CS%s' % i].set("")
        globals()['plB_CS%s' % i].set("")
        globals()['plC_CS%s' % i].set("")
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

def chip_amt(amount):
    amt_txt = amt_chips.get();
    # amt_txt = amt_chips;
    amtVal = int(amt_txt[1:]);
    amtNew = amtVal - amount;
    amt_chips.set("$" + str(amtNew));
    # amt_chips -= "$" + str(int(amt_txt[1:]) - 10);


def deal_cards():
    global amt_chips;
    global Player0;
    global Player1;
    global Player2;
    global Player3;
    global Player4;
    global num_plyr;

    clr_msg();
    dlr_CS1.set("XX");
    chip_amt(10);

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
            c_value = CardFuncs.get_cval(card_val)
            Player0.tot_hand = c_value
            Player0.arrCard.append(c_value)
        elif i == 1:
            user_CS1.set(card_val + card_suit);
            # user_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player1.num_aces = num_A;
            c_value = CardFuncs.get_cval(card_val)
            Player1.tot_hand = c_value
            Player1.arrCard.append(c_value)
        elif i == 2:
            user_CS2.set(card_val + card_suit);
            # user_CS2 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player1.num_cards = 2;
            Player1.num_aces += num_A;
            c_value = CardFuncs.get_cval(card_val)
            Player1.tot_hand += c_value
            Player1.arrCard.append(c_value)
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
            c_value = CardFuncs.get_cval(card_val)
            Player2.tot_hand = c_value
            Player2.arrCard.append(c_value)
        elif i == 4:
            plA_CS2.set(card_val + card_suit);
            # plA_CS2 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 2;
            Player2.num_aces += num_A;
            c_value = CardFuncs.get_cval(card_val)
            Player2.tot_hand += c_value
            Player2.arrCard.append(c_value)
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
            c_value = CardFuncs.get_cval(card_val)
            Player3.tot_hand = c_value
            Player3.arrCard.append(c_value)
        elif i == 6:
            plB_CS2.set(card_val + card_suit);
            # plB_CS2 = card_val + card_suit;
            Player3.num_cards = 2;
            Player3.num_aces += num_A;
            c_value = CardFuncs.get_cval(card_val)
            Player3.tot_hand += c_value
            Player3.arrCard.append(c_value)
        if num_plyr == 2:
            continue
        elif i == 7:
            plC_CS1.set(card_val + card_suit);
            # plC_CS1 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player4.num_aces = num_A;
            c_value = CardFuncs.get_cval(card_val)
            Player4.tot_hand = c_value
            Player4.arrCard.append(c_value)
        elif i == 8:
            plC_CS2.set(card_val + card_suit);
            # plC_CS2 = card_val + card_suit;
            Player4.num_cards = 2;
            Player4.num_aces += num_A;
            c_value = CardFuncs.get_cval(card_val)
            Player4.tot_hand += c_value
            Player4.arrCard.append(c_value)

def hit():
    global Player1;
    card_val, card_suit = get_card()
    if Player1.num_cards == 3:
        user_CS4.set(card_val + card_suit);
        # user_CS4 = card_val + card_suit;
        if (card_val == "A"):
            num_A = 1
        else:
            num_A = 0
        Player1.num_cards = 4;
        if num_A ==1: Player1.num_aces += 1
        c_value = CardFuncs.get_cval(card_val)
        Player1.tot_hand += c_value
        Player1.arrCard.append(c_value)
    if Player1.num_cards == 2:
        user_CS3.set(card_val + card_suit);
        # user_CS3 = card_val + card_suit;
        if (card_val == "A"):
            num_A = 1
        else:
            num_A = 0
        Player1.num_cards = 3;
        if num_A ==1: Player1.num_aces += 1
        c_value = CardFuncs.get_cval(card_val)
        Player1.tot_hand += c_value
        Player1.arrCard.append(c_value)
    if Player1.tot_hand > 21:
        user_score.set("BUSTED")

def plyr_cont():
    global num_plyr;
    if num_plyr >= 1:
        plr1_hit()
    if num_plyr >= 2:
        plr2_hit()
    if num_plyr == 3:
        plr3_hit()

def plr1_hit():
    global Player2;
    plyr_cnum = 3;
    while Player2.tot_hand < 16:
        card_val, card_suit = get_card()
        if plyr_cnum == 4:
            plA_CS4.set(card_val + card_suit);
            # plB_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 4;
            if num_A ==1: Player2.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player2.tot_hand += c_value
            Player2.arrCard.append(c_value)
            break;
        if plyr_cnum == 3:
            plA_CS3.set(card_val + card_suit);
            # plB_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player2.num_cards = 3;
            if num_A ==1: Player2.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player2.tot_hand += c_value
            Player2.arrCard.append(c_value)
            plyr_cnum = 4;
    if Player2.tot_hand > 21:
        plA_score.set("BUST")

def plr2_hit():
    global Player3;
    plyr_cnum = 3;
    while Player3.tot_hand < 16:
        card_val, card_suit = get_card()
        if plyr_cnum == 4:
            plB_CS4.set(card_val + card_suit);
            # plB_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_cards = 4;
            if num_A ==1: Player3.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player3.tot_hand += c_value
            Player3.arrCard.append(c_value)
            break;
        if plyr_cnum == 3:
            plB_CS3.set(card_val + card_suit);
            # plB_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player3.num_cards = 3;
            if num_A ==1: Player3.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player3.tot_hand += c_value
            Player3.arrCard.append(c_value)
            plyr_cnum = 4;
    if Player3.tot_hand > 21:
        plB_score.set("BUST")

def plr3_hit():
    global Player4;
    plyr_cnum = 3;
    while Player4.tot_hand < 16:
        card_val, card_suit = get_card()
        if plyr_cnum == 4:
            plC_CS4.set(card_val + card_suit);
            # plB_CS3 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player4.num_cards = 4;
            if num_A ==1: Player4.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player4.tot_hand += c_value
            Player4.arrCard.append(c_value)
            break;
        if plyr_cnum == 3:
            plC_CS3.set(card_val + card_suit);
            # plB_CS4 = card_val + card_suit;
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player4.num_cards = 3;
            if num_A ==1: Player4.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player4.tot_hand += c_value
            Player4.arrCard.append(c_value)
            plyr_cnum = 4;
    if Player4.tot_hand > 21:
        plC_score.set("BUST")

def dlr_play ():
    global Player0;
    card_val, card_suit = get_card();
    dlr_CS1.set(card_val + card_suit);
    if (card_val == "A"):
        num_A = 1
    else:
        num_A = 0
    Player0.num_cards = 2;
    Player0.num_aces += num_A;
    c_value = CardFuncs.get_cval(card_val)
    Player0.tot_hand += c_value
    Player0.arrCard.append(c_value)
    while Player0.tot_hand < 16:
        card_val, card_suit = get_card()
        if Player0.num_cards == 3:
            dlr_CS4.set(card_val + card_suit);
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0.num_cards = 4;
            if num_A ==1: Player0.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player0.tot_hand += c_value
            Player0.arrCard.append(c_value)
        if Player0.num_cards == 2:
            dlr_CS3.set(card_val + card_suit);
            if (card_val == "A"):
                num_A = 1
            else:
                num_A = 0
            Player0.num_cards = 3;
            if num_A ==1: Player0.num_aces += 1
            c_value = CardFuncs.get_cval(card_val)
            Player0.tot_hand += c_value
            Player0.arrCard.append(c_value)
    if Player0.tot_hand > 21:
        dlr_score.set("BUST - Player WINS")
        # break
    hand_comp = Player0.tot_hand - Player1.tot_hand;
    if hand_comp == 0:
        chip_amt(-10)
        dlr_score.set("PUSH")
    elif hand_comp < 0:
        chip_amt(-20)
        dlr_score.set("Player WINS")
    else:
        dlr_score.set("Dealer WINS")

def get_odds():
    chip_amt(5)


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
ttk.Label(mainframe, text="Number of card decks to be used").grid(column=0, row=0, sticky=W)
decks = ttk.Entry(mainframe, width=3, justify=RIGHT, textvariable=num_decks)
decks.grid(column=5, row=0, sticky=W)
decks.insert(0, "2")

num_players = StringVar();
ttk.Label(mainframe, text="Number of other players").grid(column=8, row=0, sticky=W)
players = ttk.Entry(mainframe, width=3, justify=RIGHT, textvariable=num_players)
players.grid(column=9, row=0, sticky=(E))
players.insert(0, "2")

ttk.Button(mainframe, text="Shuffle", command=shuffle).grid(column=0, row=3, sticky=S)
ttk.Button(mainframe, text="Deal", command=deal_cards).grid(column=0, row=4, sticky=S)
ttk.Button(mainframe, text="-Hit-", command=hit).grid(column=4, row=32, sticky=S)
ttk.Button(mainframe, text="-Hold-", command=dlr_play).grid(column=6, row=32, sticky=S)
ttk.Button(mainframe, text="Continue Players Hands", command=plyr_cont).grid(column=10, row=25, sticky=S)
ttk.Button(mainframe, text="Get Odds", command=get_odds).grid(column=9, row=32, sticky=S)

dlr_CS1 = StringVar();
dlr_CS2 = StringVar();
dlr_CS3 = StringVar();
dlr_CS4 = StringVar();
dlr_score = StringVar();
ttk.Label(mainframe, text="Dealer").grid(column=0, row=6, sticky=N)
ttk.Label(mainframe, textvariable=dlr_CS1).grid(column=2, row=6, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS2).grid(column=2, row=7, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS3).grid(column=2, row=8, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS4).grid(column=2, row=9, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_score).grid(column=2, row=9, padx=0, sticky=W)

user_CS1 = StringVar();
user_CS2 = StringVar();
user_CS3 = StringVar();
user_CS4 = StringVar();
user_score = StringVar();
ttk.Label(mainframe, text="User").grid(column=5, columnspan=2, row=30, sticky=W)
ttk.Label(mainframe, textvariable=user_CS1).grid(column=4, row=28,sticky=S)
ttk.Label(mainframe, textvariable=user_CS2).grid(column=5, row=28,sticky=S)
ttk.Label(mainframe, textvariable=user_CS3).grid(column=6, row=28,sticky=S)
ttk.Label(mainframe, textvariable=user_CS4).grid(column=7, row=28,sticky=S)
ttk.Label(mainframe, textvariable=user_score).grid(column=5, row=26, padx=0, sticky=S)

amt_chips = StringVar();
ttk.Label(mainframe, text="Amount in Player chips:").grid(column=0, row=34, sticky=W)
ttk.Label(mainframe, textvariable=amt_chips).grid(column=2, row=34, sticky=W)
amt_chips.set("$100")

odds_guess = StringVar();
ttk.Label(mainframe, text="Guess odds of going BUST").grid(column=6, row=34, sticky=W)
odds_g = ttk.Entry(mainframe, width=3, justify=RIGHT, textvariable=odds_guess)
odds_g.grid(column=9, row=34, sticky=W)

plA_text = StringVar();
plA_CS1 = StringVar();
plA_CS2 = StringVar();
plA_CS3 = StringVar();
plA_CS4 = StringVar();
plA_score = StringVar();
ttk.Label(mainframe, textvariable=plA_text).grid(column=8, row=4, sticky=N)
ttk.Label(mainframe, textvariable=plA_CS1).grid(column=8, row=5)
ttk.Label(mainframe, textvariable=plA_CS2).grid(column=8, row=6)
ttk.Label(mainframe, textvariable=plA_CS3).grid(column=8, row=7)
ttk.Label(mainframe, textvariable=plA_CS4).grid(column=8, row=8)
ttk.Label(mainframe, textvariable=plA_score).grid(column=8, row=10, sticky=N)

plB_text = StringVar();
plB_CS1 = StringVar();
plB_CS2 = StringVar();
plB_CS3 = StringVar();
plB_CS4 = StringVar();
plB_score = StringVar();
ttk.Label(mainframe, textvariable=plB_text).grid(column=9, row=4, sticky=N)
ttk.Label(mainframe, textvariable=plB_CS1).grid(column=9, row=5,)
ttk.Label(mainframe, textvariable=plB_CS2).grid(column=9, row=6,)
ttk.Label(mainframe, textvariable=plB_CS3).grid(column=9, row=7,)
ttk.Label(mainframe, textvariable=plB_CS4).grid(column=9, row=8,)
ttk.Label(mainframe, textvariable=plB_score).grid(column=9, row=10, sticky=N)

plC_text = StringVar();
plC_CS1 = StringVar();
plC_CS2 = StringVar();
plC_CS3 = StringVar();
plC_CS4 = StringVar();
plC_score = StringVar();
ttk.Label(mainframe, textvariable=plC_text).grid(column=10, row=4, sticky=N)
ttk.Label(mainframe, textvariable=plC_CS1).grid(column=10, row=5,)
ttk.Label(mainframe, textvariable=plC_CS2).grid(column=10, row=6,)
ttk.Label(mainframe, textvariable=plC_CS3).grid(column=10, row=7,)
ttk.Label(mainframe, textvariable=plC_CS4).grid(column=10, row=8,)
ttk.Label(mainframe, textvariable=plC_score).grid(column=10, row=10, sticky=N)

for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=1)

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
