import sys

players = int(sys.argv[1])
lastmarb = int(sys.argv[2])
# players = 13
# lastmarb = 7999

playerscore = {}

class Marble(object):
    def __init__(self, num):
        self.cw = None
        self.ccw = None
        self.number = num

def keepscore(playr, addnum):
    if playr in playerscore:
        playerscore[playr] += addnum
    else:
        playerscore[playr] = addnum

def state_of_game(elf):
    here = stateofgamestart
    stog = ''
    for i in range(lastmarb):
        stog = stog + ' ' + str(here.number)
        here = here.cw
    print('[{}] {}'.format(elf, stog))

current = Marble(0)
current.cw = current
current.ccw = current

stateofgamestart = current

marb = 0
while marb < lastmarb + 1:
    for player in range(players):
        player += 1
        # state_of_game(player)
        marb += 1
        if marb > lastmarb:
            break
        newmarble = Marble(marb)
        if marb % 23 == 0:
            keepscore(player, marb)
            before = current.ccw.ccw.ccw.ccw.ccw.ccw.ccw.ccw
            after = current.ccw.ccw.ccw.ccw.ccw.ccw
            keepscore(player, before.cw.number)
            before.cw = after
            after.ccw = before
            current = after
            continue
        next = current.cw
        over = next.cw
        next.cw = newmarble
        newmarble.ccw = next
        over.ccw = newmarble
        newmarble.cw = over
        current = newmarble


# print(playerscore)
scorez = list(playerscore.values())
scorez.sort()
print(scorez)
print(max(playerscore.values()))