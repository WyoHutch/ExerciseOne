import operator

num_decks = 4;

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
    card_val = cards[0][0];
    val_cnt = 0;
    ones_cnt = 0;
    tens_cnt = 0;
    for i in range(len(cards)):
        card_rank = cards[i][0];
        if card_rank == "1":
            tens_cnt += 1
        if card_rank == "J" or card_rank == "Q" or card_rank == "K":
            tens_cnt += 1
        if card_rank == "A":
            ones_cnt += 1
        if card_rank == card_val:
            val_cnt += 1
        else:
            odds_pct[card_val] = val_cnt/len(cards) * 100;
            card_val = card_rank;
            val_cnt = 1;
        odds_pct[card_val] = val_cnt/len(cards) * 100

    odds_pct.pop("J");
    odds_pct.pop("Q");
    odds_pct.pop("K");
    odds_pct["1"] = odds_pct["A"];
    odds_pct["10"] = tens_cnt/len(cards) * 100;
    odds_pct["11"] = odds_pct["A"];
    odds_pct.pop("A");
    odds_pct_sort = sorted(odds_pct.items(), key = operator.itemgetter(1), reverse = True)
    odds_sort = {}
    for keys in odds_pct_sort:
        odds_sort[keys[0]] = keys[1]
    return odds_sort
