pmin = 193651
pmax = 649729

howmanygood = 0

for testpw in range(pmin, pmax):
    tstr = str(testpw)
    prev = ''
    preprev = ''
    double = False
    nodec = True

    for digit in tstr:
        if prev == '':
            prev = digit
            continue

        if prev > digit:
            nodec = False
            break

        if prev == digit:
            double = True

        preprev = prev
        prev = digit

    if double and nodec:
        countdict = { str(x): 0 for x in range (0, 10) }
        for digit in tstr:
            countdict[digit] += 1

        goodone = False
        for k, v in countdict.items():
            if v == 2:
                goodone = True

        if goodone:
            print(testpw)
            howmanygood += 1
            

print('how many good: {}'.format(howmanygood))
