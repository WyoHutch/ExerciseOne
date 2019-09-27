def handtot(arrCard):
    total = 0;
    tot_A = 0;
    for i in arrCard:
        if i == 11: tot_A += 1
        total += i
    while total > 21 and tot_A > 0:
        total -= 10
        tot_A -= 1
    return total

print(handtot([3, 10, 4, 11]))