import CardFuncs

import random

from tkinter import *
from tkinter import ttk

card_num = 0;
card_deck=[];

def shuffle():
    global card_deck;
    global card_num;
    card_deck = CardFuncs.get_cards(int(num_decks.get()));
    card_num = int(num_decks.get()) * 52

def deal_cards(num_plyr):
    global card_num;
    global card_deck;
    for i in range(3 + 2 * num_plyr):
        c_ind = random.randint(0, card_num);
        card = card_deck.pop(c_ind)
        card_num -= 1;
        if len(card) == 3:
            card_val = card[:2]
        else:
            card_val = card[0]
        card_suit = card[-1]
        if i == 0:
            user_CS1.set(card_val);
            user_CS2.set(card_suit);
        elif i == 1:
            user_CS3.set(card_val);
            user_CS4.set(card_suit);
        elif i == 2:
            dlr_CS1.set("X");
            dlr_CS2.set("X");
        elif i == 3:
            dlr_CS3.set(card_val);
            dlr_CS4.set(card_suit);
        if num_plyr == 0:
            continue
        elif i == 4:
            plA_CS1.set(card_val);
            plA_CS2.set(card_suit);
        elif i == 5:
            plA_CS3.set(card_val);
            plA_CS4.set(card_suit);
        if num_plyr == 1:
            continue
        elif i == 6:
            plB_CS1.set(card_val);
            plB_CS2.set(card_suit);
        elif i == 7:
            plB_CS3.set(card_val);
            plB_CS4.set(card_suit);


root = Tk()
root.title("Casino BlackJack Odds")
root.geometry("600x600")

mainframe = ttk.Frame(root, padding="0 0 0 0")
mainframe.grid(columnspan = 1, rowspan = 1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

card_deck = [];

num_decks = StringVar();
ttk.Label(mainframe, width=14, text="Number of card decks to be used").grid(column=0, row=0, sticky=W)
decks = ttk.Entry(mainframe, width=5, justify=RIGHT, textvariable=num_decks)
decks.grid(column=1, row=0, sticky=(W))
decks.insert(0, "2")

num_players = StringVar();
ttk.Label(mainframe, width=13, text="Number of other players").grid(column=5, row=0, sticky=E)
players = ttk.Entry(mainframe, width=5, justify=RIGHT, textvariable=num_players)
players.grid(column=6, row=0, sticky=(E))
players.insert(0, "2")


ttk.Button(mainframe, text="Shuffle", command=shuffle).grid(column=0, row=3, sticky=S)
ttk.Button(mainframe, text="Deal", command=deal_cards).grid(column=0, row=4, sticky=S)
print(card_deck)

dlr_CS1 = StringVar();
dlr_CS2 = StringVar();
dlr_CS3 = StringVar();
dlr_CS4 = StringVar();
dlr_CS5 = StringVar();
dlr_CS6 = StringVar();
dlr_CS7 = StringVar();
dlr_CS8 = StringVar();
ttk.Label(mainframe, width=6, text="Dealer").grid(column=0, row=6, sticky=N)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=dlr_CS1).grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=dlr_CS2).grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=dlr_CS3).grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=dlr_CS4).grid(column=1, row=7, sticky=E)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=dlr_CS5).grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=dlr_CS6).grid(column=1, row=8, sticky=E)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=dlr_CS7).grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=dlr_CS8).grid(column=1, row=9, sticky=E)

user_CS1 = StringVar();
user_CS2 = StringVar();
user_CS3 = StringVar();
user_CS4 = StringVar();
user_CS5 = StringVar();
user_CS6 = StringVar();
user_CS7 = StringVar();
user_CS8 = StringVar();
ttk.Label(mainframe, width=6, text="User").grid(column=5, columnspan=2, row=17, sticky=N)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=user_CS1).grid(column=3, row=16, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=user_CS2).grid(column=3, row=16, sticky=E)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=user_CS3).grid(column=4, row=16, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=user_CS4).grid(column=4, row=16, sticky=E)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=user_CS5).grid(column=5, row=16, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=user_CS6).grid(column=5, row=16, sticky=E)
ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=user_CS7).grid(column=6, row=16, sticky=W)
ttk.Label(mainframe, width=2, justify=LEFT, textvariable=user_CS8).grid(column=6, row=16, sticky=E)

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
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plA_CS1).grid(column=6, row=5, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plA_CS2).grid(column=6, row=5, sticky=E)
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plA_CS3).grid(column=6, row=6, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plA_CS4).grid(column=6, row=6, sticky=E)
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plA_CS5).grid(column=6, row=7, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plA_CS6).grid(column=6, row=7, sticky=E)
    ttk.Label(mainframe, width=2, justify=RIGHT, textvariable=plA_CS7).grid(column=6, row=8, sticky=W)
    ttk.Label(mainframe, width=2, justify=LEFT, textvariable=plA_CS8).grid(column=6, row=8, sticky=E)

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