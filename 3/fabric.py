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

print(claims)

def isclaimed(x, y):
    xin = False
    yin = False

    incount = 0
    for k, v in claims.items():
        if x + 1 > v['x'] and x + 1 <= v['x'] + v['len']:
            xin = True
        if y + 1 > v['y'] and y + 1 <= v['y'] + v['wid']:
            yin = True

        print('x is {}, y is {} xin is {} yin is {}'.format(x, y, xin, yin))
        if xin and yin:
            incount += 1

    return incount

#fabric = [x[:] for x in [[0] * 1000] * 1000]
fabric = [x[:] for x in [[0] * 10] * 10]
total_count = 0

for x_in in range(10):
    for y_in in range(10):
        fabric[x_in][y_in] = isclaimed(x_in, y_in)
        if fabric[x_in][y_in] > 1:
            total_count += 1

for p in range(10):
    print(fabric[p])

print(total_count)
