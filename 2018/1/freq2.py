import sys

total_freq = 0
seenit = {}

with open('input') as file:
    freqs = file.readlines()

def checkifseen(num):
    if num in seenit:
        print('Frequency found: {}'.format(num))
        seenit[num] += 1
        sys.exit()
    else:
        seenit[num] = 1

while 1:
    for item in freqs:
        try:
            num = int(item[1:])
            if item[0] == '-':
                total_freq = total_freq - num
            else:
                total_freq = total_freq + num
            checkifseen(total_freq)
        except ValueError as ex:
            print('{} {}'.format(item, ex))


print(total_freq)
#print(seenit)
