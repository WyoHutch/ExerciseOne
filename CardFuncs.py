import operator

def get_cards(num_decks):
    suits = ["C", "D", "H", "S"];
    face_cards = ["B", "J", "Q", "T", "Z"];
    cards = [];
    card_deck = [];

    for i in range(2, 10):
        cards.append(str(i))
    cards.extend(face_cards)

    for i in cards:
        for j in suits:
            card_deck.append(i + j);

    card_list = [];
    for i in range(num_decks):
        card_list.extend(card_deck)

    card_list.sort();

    for i in range(num_decks * 32, num_decks * 36):
        temp = card_list.pop(i)
        card_list.insert(i, temp.replace("B", "10"));
    for i in range(num_decks * 44, num_decks * 48):
        temp = card_list.pop(i)
        card_list.insert(i, temp.replace("T", "K"));
    for i in range(num_decks * 48, num_decks * 52):
        temp = card_list.pop(i)
        card_list.insert(i, temp.replace("Z", "A"));

    return card_list

def get_cval(cardv):
    if cardv == "J" or cardv == "Q" or cardv == "K":
        return 10
    elif cardv == "A":
        return 11
    else:
        return int(cardv)

def get_odds(cards):
    odds_pct = {};
    for i in range(1, 12):
        odds_pct[i] = 0
    print(len(cards))
    for i in range(len(cards)):
        if len(cards[i]) == 3:
            card_val = cards[i][:2]
        else:
            card_val = cards[i][0]
        odds_pct[get_cval(card_val)] += 1
    odds_pct[1] = odds_pct[11]
    return odds_pct

