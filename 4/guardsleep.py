import re

patt = re.compile(r'^\[[0-9]{4}-[0-9]{2}-[0-9]{2}.?[0-9]{2}:([0-9]{2})')

def processshift(sd):
    shifthour = [0] * 60
    guardinfo = {}
    for i in sd:
        if 'begins' in i:
            guardinfo = re.search(patty, i).groupdict()
        elif 'falls asleep' in i:
            falls = int(re.findall(patt, i)[0])
        elif 'wakes up' in i:
            wakes = int(re.findall(patt, i)[0])
            for j in range(60):
                if j >= falls and j < wakes:
                    shifthour[j] = 1
            falls = 0
            wakes = 0
            # print(shifthour)

    add_to_guard(guardinfo['guardid'], shifthour)
    # return shifthour

def add_to_guard(gid, sh):
    if gid not in guards:
        guards[gid] = [sh]
    else:
        guards[gid].append(sh)


with open('input') as file:
    sleepdata = file.readlines()

patty = re.compile(r'(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}) (?P<time>[0-9]{2}:[0-9]{2})] Guard #(?P<guardid>[0-9]+)(?P<text>.*[^\n])')

guards = {}

sleepdata.sort()

# for i in sleepdata:
    # event = re.search(patt, i).groupdict()
    # cdata[event['guardid']] = cdata[event['guardid']].append(event['date'])


prev_begin = 0
for event in sleepdata:
    if 'begins shift' in event: # or sleepdata.index(event) == len(sleepdata) - 1:
        if sleepdata.index(event) > 0:
            current_index = sleepdata.index(event)
            processshift(sleepdata[prev_begin:current_index])
            prev_begin = current_index
else:
    processshift(sleepdata[prev_begin:])

max_sleep_gid = 0
max_sleep_amount = 0
for k,v in guards.items():
    # print(k)
    # for xx in v:
    #     print(xx)
    asleep = 0
    totalmins = [0] * 60
    for night in v:
        # print('miaturo {}'.format(night))
        # print([x for x in night if x == 1])
        asleep += len([x for x in night if x == 1])
        for min in range(len(night)):
            if night[min] == 1:
                totalmins[min] += 1

    if max_sleep_amount < asleep:
        max_sleep_amount = asleep
        max_sleep_gid = k
    # print('totalmins')
    # print(totalmins)
    maxindex = totalmins.index(max(totalmins))
    maxvalue = max(totalmins)
    print('guard: {} nights: {}, mins asleep: {} mostsleeped: {}, mostinsameminute: {}, weird number: {}'.format(k, len(v), asleep, maxindex, maxvalue, int(k) * int(maxindex)))

print(max_sleep_gid)