from string import ascii_lowercase

def reacting(polymer):
    lowest = 0
    while True:
        x = 0
        prev_len = len(polymer)
        while True:
            if (polymer[x].islower() and polymer[x + 1].isupper()) or (polymer[x].isupper() and polymer[x + 1].islower()):
                if polymer[x].lower() == polymer[x + 1].lower():
                    # print('removing {} {}'.format(polymer[x], polymer[x+1]))
                    del polymer[x:x + 2]
                    break
                else:
                    x = x + 1
            else:
                x = x + 1
            if x == prev_len - 1:
                lowest = x
                break

        if len(polymer) == prev_len:
            break
    return lowest

with open('input') as file:
    poly = list(file.readline())

print('lowest unit in polymer: {}'.format(reacting(poly)))


for letter in ascii_lowercase:
    polym = [x for x in poly if x.lower() != letter]
    print('Removing {} and reacting gives: {}'.format(letter, reacting(polym)))
