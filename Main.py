import CardFuncs

import random

from tkinter import *
from tkinter import ttk

num_cards = 0;
card_deck = [];

class Player:
    def __init__(self, num_cards=0, num_aces=0, tot_hand=0, arrCard = []):
        self.num_cards = num_cards;
        self.num_aces = num_aces;
        self.arrCard = arrCard
    def handtot(self):
        total = 0;
        tot_A = 0;
        for i in self.arrCard:
            if i == 11: tot_A += 1
            total += i
        while total > 21 and tot_A > 0:
            total -= 10
            tot_A -= 1
        return total

def clr_msg():
    global num_plyr
    dlr_score.set("")
    user_score.set("")
    # plA_text.set("")
    # plB_text.set("")
    # plC_text.set("")
    plA_score.set("")
    plB_score.set("")
    plC_score.set("")
    odds_win.set("")
    odds_bust.set("")
    for i in range(1, 5) :
        globals()['dlr_CS%s' % i].set("")
        globals()['user_CS%s' % i].set("")
        globals()['plA_CS%s' % i].set("")
        globals()['plB_CS%s' % i].set("")
        globals()['plC_CS%s' % i].set("")
    for i in range(1, 7) :
        globals()['odds_num%s' % i].set("")
        globals()['odds_per%s' % i].set("")


def shuffle():
    global card_deck;
    global num_cards;
    clr_msg();
    num_plyr = int(num_players.get())
    if num_plyr >= 1: plA_text.set("Player A")
    if num_plyr >= 2: plB_text.set("Player B")
    if num_plyr == 3: plC_text.set("Player C")
    card_deck = CardFuncs.get_cards(int(num_decks.get()));
    num_cards = int(num_decks.get()) * 52

def get_card():
    global num_cards;
    global card_deck;
    card = card_deck.pop(random.randint(0, num_cards));
    num_cards -= 1;
    if len(card) == 3:
        card_val = card[:2]
    else:
        card_val = card[0]
    card_suit = card[-1]
    return card_val, card_suit

def chip_amt(amount):
    amt_txt = amt_chips.get();
    amtVal = int(amt_txt[1:]);
    amtNew = amtVal + amount;
    amt_chips.set("$" + str(amtNew));

def deal_cards():
    global amt_chips;
    global Player0;
    global Player1;
    global Player2;
    global Player3;
    global Player4;
    global num_plyr;
    Player0.num_cards = 0
    Player0.num_aces = 0
    Player0.arrCard = []
    Player1.num_cards = 0
    Player1.num_aces = 0
    Player1.arrCard = []
    if num_plyr >= 1:
        Player2.num_cards = 0
        Player2.num_aces = 0
        Player2.arrCard = []
    if num_plyr >= 2:
        Player3.num_cards = 0
        Player3.num_aces = 0
        Player3.arrCard = []
    if num_plyr == 3:
        Player4.num_cards = 0
        Player4.num_aces = 0
        Player4.arrCard = []

    clr_msg();
    if num_cards < (2 + num_plyr) * 4:
        dlr_score.set("Not enough cards for deal")
        return
    dlr_CS1.set("XX");
    chip_amt(-10);

    for i in range(3 + 2 * num_plyr):
        card_val, card_suit = get_card();
        if i == 0:
            dlr_CS2.set(card_val + card_suit);
            Player0.num_cards = 1;
            Player0.arrCard.append(CardFuncs.get_cval(card_val))
        elif i == 1:
            user_CS1.set(card_val + card_suit);
            Player1.arrCard.append(CardFuncs.get_cval(card_val))
        elif i == 2:
            user_CS2.set(card_val + card_suit);
            Player1.num_cards = 2;
            Player1.arrCard.append(CardFuncs.get_cval(card_val))
        if num_plyr == 0:
            continue
        elif i == 3:
            plA_CS1.set(card_val + card_suit);
            Player2.arrCard.append(CardFuncs.get_cval(card_val))
        elif i == 4:
            plA_CS2.set(card_val + card_suit);
            Player2.num_cards = 2;
            Player2.arrCard.append(CardFuncs.get_cval(card_val))
        if num_plyr == 1:
            continue
        elif i == 5:
            plB_CS1.set(card_val + card_suit);
            Player3.arrCard.append(CardFuncs.get_cval(card_val))
        elif i == 6:
            plB_CS2.set(card_val + card_suit);
            Player3.num_cards = 2;
            Player3.arrCard.append(CardFuncs.get_cval(card_val))
        if num_plyr == 2:
            continue
        elif i == 7:
            plC_CS1.set(card_val + card_suit);
            Player4.arrCard.append(CardFuncs.get_cval(card_val))
        elif i == 8:
            plC_CS2.set(card_val + card_suit);
            Player4.num_cards = 2;
            Player4.arrCard.append(CardFuncs.get_cval(card_val))

def hit():
    global Player1;
    card_val, card_suit = get_card()
    if Player1.num_cards == 3:
        user_CS4.set(card_val + card_suit);
        Player1.num_cards = 4;
        Player1.arrCard.append(CardFuncs.get_cval(card_val))
    if Player1.num_cards == 2:
        user_CS3.set(card_val + card_suit);
        Player1.num_cards = 3;
        Player1.arrCard.append(CardFuncs.get_cval(card_val))
    if Player1.handtot() > 21:
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
    while Player2.handtot() < 16:
        card_val, card_suit = get_card()
        if plyr_cnum == 4:
            plA_CS4.set(card_val + card_suit);
            Player2.num_cards = 4;
            Player2.arrCard.append(CardFuncs.get_cval(card_val))
            return
        if plyr_cnum == 3:
            plA_CS3.set(card_val + card_suit);
            Player2.num_cards = 3;
            Player2.arrCard.append(CardFuncs.get_cval(card_val))
            plyr_cnum = 4;
    if Player2.handtot() > 21:
        plA_score.set("BUST")

def plr2_hit():
    global Player3;
    plyr_cnum = 3;
    while Player3.handtot() < 16:
        card_val, card_suit = get_card()
        if plyr_cnum == 4:
            plB_CS4.set(card_val + card_suit);
            Player3.num_cards = 4;
            Player3.arrCard.append(CardFuncs.get_cval(card_val))
            return
        if plyr_cnum == 3:
            plB_CS3.set(card_val + card_suit);
            Player3.num_cards = 3;
            Player3.arrCard.append(CardFuncs.get_cval(card_val))
            plyr_cnum = 4;
    if Player3.handtot() > 21:
        plB_score.set("BUST")

def plr3_hit():
    global Player4;
    plyr_cnum = 3;
    while Player4.handtot() < 16:
        card_val, card_suit = get_card()
        if plyr_cnum == 4:
            plC_CS4.set(card_val + card_suit);
            Player4.num_cards = 4;
            Player4.arrCard.append(CardFuncs.get_cval(card_val))
            return
        if plyr_cnum == 3:
            plC_CS3.set(card_val + card_suit);
            Player4.num_cards = 3;
            Player4.arrCard.append(CardFuncs.get_cval(card_val))
            plyr_cnum = 4;
    if Player4.handtot() > 21:
        plC_score.set("BUST")

def dlr_play ():
    global Player0;
    card_val, card_suit = get_card();
    dlr_CS1.set(card_val + card_suit);
    Player0.num_cards = 2;
    Player0.arrCard.append(CardFuncs.get_cval(card_val))
    while Player0.handtot() < 16:
        card_val, card_suit = get_card()
        if Player0.num_cards == 3:
            dlr_CS4.set(card_val + card_suit);
            Player0.num_cards = 4;
            Player0.arrCard.append(CardFuncs.get_cval(card_val))
        if Player0.num_cards == 2:
            dlr_CS3.set(card_val + card_suit);
            Player0.num_cards = 3;
            Player0.arrCard.append(CardFuncs.get_cval(card_val))
    hand_comp = Player0.handtot() - Player1.handtot();
    if Player0.handtot() > 21:
        chip_amt(20)
        dlr_score.set("BUST - Player WINS")
    elif hand_comp == 0:
        chip_amt(10)
        dlr_score.set("PUSH")
    elif hand_comp < 0:
        chip_amt(20)
        dlr_score.set("Player WINS")
    else:
        dlr_score.set("Dealer WINS")

def get_odds():
    global Player1;
    global card_deck;
    chip_amt(-5)
    odds_dict = CardFuncs.get_odds(card_deck)
    hit_21 = 21 - Player1.handtot()
    if hit_21 > 11:
        user_score.set("No chance to BUST")
        return
    user_score.set(str(hit_21) + " to WIN")
    odds_21 = 100 * odds_dict[hit_21] / num_cards
    bust_tot = 0
    for i in range(hit_21, 11):
        bust_tot += odds_dict[i]
    bust_per = 100 * bust_tot / num_cards
    odds_num1.set("BUST")
    odds_num2.set("21")
    odds_num3.set("20")
    odds_num4.set("19")
    odds_num5.set("18")
    odds_num6.set("17")
    odds_per1.set("{:5.2f}".format(bust_per))
    odds_per2.set("{:5.2f}".format(odds_21))
    if hit_21 > 1: odds_per3.set("{:5.2f}".format(100 * odds_dict[hit_21 - 1] / num_cards))
    if hit_21 > 2: odds_per4.set("{:5.2f}".format(100 * odds_dict[hit_21 - 2] / num_cards))
    if hit_21 > 3: odds_per5.set("{:5.2f}".format(100 * odds_dict[hit_21 - 3] / num_cards))
    if hit_21 > 4: odds_per6.set("{:5.2f}".format(100 * odds_dict[hit_21 - 4] / num_cards))
    if odds_bust.get() == "" or odds_win.get() == "": return
    win_odds = float(odds_win.get())
    bust_odds = float(odds_bust.get())
    if abs(bust_odds - bust_per) < 5 and abs(win_odds - odds_21) < 3: chip_amt(5)
    if abs(bust_odds - bust_per) < 3 and abs(win_odds - odds_21) < 2: chip_amt(5)
    if abs(bust_odds - bust_per) < 2 and abs(win_odds - odds_21) < 1: chip_amt(5)


root = Tk()
root.title("Casino BlackJack Odds")
root.geometry("900x640")

mainframe = ttk.Frame(root, padding="4 8 4 8")
mainframe.grid(columnspan = 1, rowspan = 1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

card_deck = [];

num_decks = StringVar();
ttk.Label(mainframe, text="Number of card decks to be used :").grid(column=0, columnspan=3, row=0, sticky=E)
decks = ttk.Entry(mainframe, width=3, justify=RIGHT, textvariable=num_decks)
decks.grid(column=3, row=0, sticky=W)
decks.insert(0, "2")

num_players = StringVar();
ttk.Label(mainframe, text="Number of other players :").grid(column=8, row=0, sticky=W)
players = ttk.Entry(mainframe, width=3, justify=RIGHT, textvariable=num_players)
players.grid(column=9, row=0, sticky=W)
players.insert(0, "2")

ttk.Button(mainframe, text="Shuffle", command=shuffle).grid(column=0, row=3, sticky=S)
ttk.Button(mainframe, text="Deal", command=deal_cards).grid(column=0, row=4, sticky=S)
ttk.Button(mainframe, text="-Hit-", command=hit).grid(column=4, row=32, sticky=S)
ttk.Button(mainframe, text="-Hold-", command=dlr_play).grid(column=6, row=32, sticky=S)
ttk.Button(mainframe, text="Continue Players Hands", command=plyr_cont).grid(column=8, row=25, sticky=S)
ttk.Button(mainframe, text="Get Odds", command=get_odds).grid(column=8, row=32, sticky=S)

dlr_CS1 = StringVar();
dlr_CS2 = StringVar();
dlr_CS3 = StringVar();
dlr_CS4 = StringVar();
dlr_score = StringVar();
ttk.Label(mainframe, text="Dealer", font=('Arial Bold', 14)).grid(column=0, row=6, sticky=N)
ttk.Label(mainframe, textvariable=dlr_CS1, font=('Arial Bold', 12)).grid(column=2, row=6, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS2, font=('Arial Bold', 12)).grid(column=2, row=7, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS3, font=('Arial Bold', 12)).grid(column=2, row=8, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_CS4, font=('Arial Bold', 12)).grid(column=2, row=9, padx=0, sticky=W)
ttk.Label(mainframe, textvariable=dlr_score, font=('Arial Bold', 14)).grid(column=2, columnspan=3, row=10, padx=0, sticky=W)

user_CS1 = StringVar();
user_CS2 = StringVar();
user_CS3 = StringVar();
user_CS4 = StringVar();
user_score = StringVar();
ttk.Label(mainframe, text="User", font=('Arial Bold', 14)).grid(column=5, columnspan=2, row=30, sticky=S)
ttk.Label(mainframe, textvariable=user_CS1, font=('Arial Bold', 12)).grid(column=4, row=28)
ttk.Label(mainframe, textvariable=user_CS2, font=('Arial Bold', 12)).grid(column=5, row=28)
ttk.Label(mainframe, textvariable=user_CS3, font=('Arial Bold', 12)).grid(column=6, row=28)
ttk.Label(mainframe, textvariable=user_CS4, font=('Arial Bold', 12)).grid(column=7, row=28, sticky=W)
ttk.Label(mainframe, textvariable=user_score, font=('Arial Bold', 14)).grid(column=5, columnspan=2, row=25, padx=0, sticky=S)

amt_chips = StringVar();
ttk.Label(mainframe, text="Amount in Player chips:", font=('Arial', 12)).grid(column=0, row=35, sticky=W)
ttk.Label(mainframe, textvariable=amt_chips, font=('Arial Bold', 12)).grid(column=1, row=35, sticky=W)
amt_chips.set("$100")

odds_bust = StringVar();
ttk.Label(mainframe, text="What are the odds of going BUST?").grid(column=5, columnspan=3, row=37, sticky=W)
odds_b = ttk.Entry(mainframe, width=5, justify=RIGHT, textvariable=odds_bust)
odds_b.grid(column=8, row=37, sticky=W)
odds_win = StringVar();
ttk.Label(mainframe, text="What are the odds of hitting 21?").grid(column=5, columnspan=3, row=38, sticky=W)
odds_w = ttk.Entry(mainframe, width=5, justify=RIGHT, textvariable=odds_win)
odds_w.grid(column=8, row=38, sticky=W)


odds_num1 = StringVar();
odds_num2 = StringVar();
odds_num3 = StringVar();
odds_num4 = StringVar();
odds_num5 = StringVar();
odds_num6 = StringVar();
odds_per1 = StringVar();
odds_per2 = StringVar();
odds_per3 = StringVar();
odds_per4 = StringVar();
odds_per5 = StringVar();
odds_per6 = StringVar();
ttk.Label(mainframe, text="Total").grid(column=9, row=35, sticky=S)
ttk.Label(mainframe, text="Odds %").grid(column=10, row=35, sticky=S)
ttk.Label(mainframe, textvariable=odds_num1).grid(column=9, row=36)
ttk.Label(mainframe, textvariable=odds_num2).grid(column=9, row=37)
ttk.Label(mainframe, textvariable=odds_num3).grid(column=9, row=38)
ttk.Label(mainframe, textvariable=odds_num4).grid(column=9, row=39)
ttk.Label(mainframe, textvariable=odds_num5).grid(column=9, row=40)
ttk.Label(mainframe, textvariable=odds_num6).grid(column=9, row=41)
ttk.Label(mainframe, textvariable=odds_per1).grid(column=10, row=36)
ttk.Label(mainframe, textvariable=odds_per2).grid(column=10, row=37)
ttk.Label(mainframe, textvariable=odds_per3).grid(column=10, row=38)
ttk.Label(mainframe, textvariable=odds_per4).grid(column=10, row=39)
ttk.Label(mainframe, textvariable=odds_per5).grid(column=10, row=40)
ttk.Label(mainframe, textvariable=odds_per6).grid(column=10, row=41)


plA_text = StringVar();
plA_CS1 = StringVar();
plA_CS2 = StringVar();
plA_CS3 = StringVar();
plA_CS4 = StringVar();
plA_score = StringVar();
ttk.Label(mainframe, textvariable=plA_text).grid(column=8, row=4, sticky=N)
ttk.Label(mainframe, textvariable=plA_CS1, font=('Arial Bold', 12)).grid(column=8, row=5)
ttk.Label(mainframe, textvariable=plA_CS2, font=('Arial Bold', 12)).grid(column=8, row=6)
ttk.Label(mainframe, textvariable=plA_CS3, font=('Arial Bold', 12)).grid(column=8, row=7)
ttk.Label(mainframe, textvariable=plA_CS4, font=('Arial Bold', 12)).grid(column=8, row=8)
ttk.Label(mainframe, textvariable=plA_score, font=('Arial Bold', 14), foreground='#ff1000').grid(column=8, row=9, sticky=N)

plB_text = StringVar();
plB_CS1 = StringVar();
plB_CS2 = StringVar();
plB_CS3 = StringVar();
plB_CS4 = StringVar();
plB_score = StringVar();
ttk.Label(mainframe, textvariable=plB_text).grid(column=9, row=4, sticky=N)
ttk.Label(mainframe, textvariable=plB_CS1, font=('Arial Bold', 12)).grid(column=9, row=5,)
ttk.Label(mainframe, textvariable=plB_CS2, font=('Arial Bold', 12)).grid(column=9, row=6,)
ttk.Label(mainframe, textvariable=plB_CS3, font=('Arial Bold', 12)).grid(column=9, row=7,)
ttk.Label(mainframe, textvariable=plB_CS4, font=('Arial Bold', 12)).grid(column=9, row=8,)
ttk.Label(mainframe, textvariable=plB_score, font=('Arial Bold', 14), foreground='#ff1000').grid(column=9, row=9, sticky=N)

plC_text = StringVar();
plC_CS1 = StringVar();
plC_CS2 = StringVar();
plC_CS3 = StringVar();
plC_CS4 = StringVar();
plC_score = StringVar();
ttk.Label(mainframe, textvariable=plC_text).grid(column=10, row=4, sticky=N)
ttk.Label(mainframe, textvariable=plC_CS1, font=('Arial Bold', 12)).grid(column=10, row=5,)
ttk.Label(mainframe, textvariable=plC_CS2, font=('Arial Bold', 12)).grid(column=10, row=6,)
ttk.Label(mainframe, textvariable=plC_CS3, font=('Arial Bold', 12)).grid(column=10, row=7,)
ttk.Label(mainframe, textvariable=plC_CS4, font=('Arial Bold', 12)).grid(column=10, row=8,)
ttk.Label(mainframe, textvariable=plC_score, font=('Arial Bold', 14), foreground='#ff1000').grid(column=10, row=9, sticky=N)

ttk.Label(mainframe, text="Rules of the Game").grid(column=1, columnspan=2, row=39, sticky=W)
ttk.Label(mainframe, text="1. Shuffle required when there are less than four cards for every player at the board.").grid(column=0, columnspan=10, row=40, sticky=W)
ttk.Label(mainframe, text="2. Each deal costs the player $10.").grid(column=0, columnspan=10, row=41, sticky=W)
ttk.Label(mainframe, text="3. Dealer and other players play to 16 (HIT on 15 or below, HOLD on 16 or above).").grid(column=0, columnspan=10, row=42, sticky=W)
ttk.Label(mainframe, text="4. Click on 'Continue Players Hands' if you want to play those other hands.").grid(column=0, columnspan=10, row=43, sticky=W)
ttk.Label(mainframe, text="5. Returning the odds for '21' and 'BUST' will cost $5.").grid(column=0, columnspan=10, row=44, sticky=W)
ttk.Label(mainframe, text="6. Guessing witihn 5% for BUST and 3% for '21' will return $5.").grid(column=0, columnspan=10, row=45, sticky=W)
ttk.Label(mainframe, text="7. Guessing witihn 3% for BUST and 2% for '21' will return another $5.").grid(column=0, columnspan=10, row=46, sticky=W)
ttk.Label(mainframe, text="8. Guessing witihn 2% for BUST and 1% for '21' will return another $5.").grid(column=0, columnspan=10, row=47, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=1)

decks.focus()
# root.bind('<Return>', calculate)

num_plyr = int(num_players.get())

Player0 = Player();
Player1 = Player();
Player2 = Player();
Player3 = Player();
Player4 = Player();

root.mainloop()
