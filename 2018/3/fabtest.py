import re
with open('xinput') as file:
    claimslist = file.readlines()

claims = {}
for claim in claimslist:
    breakout = re.findall(r'[0-9]+',claim)
    claims[breakout[0]] = {'x': int(breakout[1]),
                           'y': int(breakout[2]),
                           'len': int(breakout[3]),
                           'wid': int(breakout[4])
                           }

# print(claims)

def isclaimed(x, y):

    incount = 0
    for k, v in claims.items():
        xin = False
        yin = False
        if x > v['x'] and x <= v['x'] + v['len']:
            xin = True
        if y > v['y'] and y <= v['y'] + v['wid']:
            yin = True

        # print('x is {}, y is {} xin is {} yin is {}'.format(x, y, xin, yin))
        if xin and yin:
            incount += 1

    return incount

#fabric = [x[:] for x in [[0] * 1001] * 1001]
fabric = [x[:] for x in [[0] * 11] * 11]
total_count = 0

for x_in in range(11):
    for y_in in range(11):
        fabric[x_in][y_in] = isclaimed(x_in, y_in)
        if fabric[x_in][y_in] > 1:
            total_count += 1


for k, v in claims.items():
    sofarsogood = True
    print(v)
    for x in range(11):
        for y in range(11):
            if x > v['x'] and x <= v['x'] + v['len'] and y > v['y'] and y <= v['y'] + v['wid']:
                print('fabric at {} , {} is {}'.format(x, y, fabric[x][y]))
                if fabric[x][y] > 1:
                    sofarsogood = False

    if sofarsogood:
        print(k)

for p in range(10):
    print(fabric[p])

print(total_count)
