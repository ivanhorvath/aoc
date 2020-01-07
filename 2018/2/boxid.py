with open('input') as file:
    boxids = file.readlines()


howmany = {'twos': 0, 'threes': 0}

for boxid in boxids:
    letterdict = {}
    for letter in boxid:
        if letter in letterdict:
            letterdict[letter] += 1
        else:
            letterdict[letter] = 1
    
    istheretwo = False
    istherethree = False
    for k, v in letterdict.items():
        if v == 2:
            istheretwo = True
        if v == 3:
            istherethree = True
    
    if istheretwo:
        howmany['twos'] += 1
    if istherethree:
        howmany['threes'] += 1

print(howmany['twos'] * howmany['threes'])


def compare_boxids(bid):
    for boxid in boxids:
        same = 0
        for i in range(len(boxid) - 1):
            if boxid[i] == bid[i]:
                same += 1
        if same == (len(boxid) - 2):
            print('one difference\n{}\n{}'.format(bid, boxid))
            commonletters = []
            for j in range(len(boxid) - 1):
                
                if boxid[j] == bid[j]:
                    commonletters.append(bid[j])
            print('common letters between the two strings:')
            print(''.join(commonletters))

    
for boxid in boxids:
    compare_boxids(boxid)


