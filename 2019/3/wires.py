import re
import sys
wires = {}

wirecount = 1

with open(sys.argv[1]) as file:
    for route in file.readlines():
        wires[wirecount] = {'route' : route.rstrip().split(',') , 'coords': []}
        wirecount += 1


#print(wires)
        
def whatcoordinates(x, y, route):
    coordz = []
    incx = False
    incy = False
    dirc = 0

 #   print('x {} {} y {} {} dir {}'.format(x, type(x), y, type(y), route))
    
    if route.startswith('U'):
        incy = True
        dirc = 1
    elif route.startswith('D'):
        incy = True
        dirc = -1
    elif route.startswith('L'):
        incx = True
        dirc = -1
    elif route.startswith('R'):
        incx = True
        dirc = 1
    else:
        print('No idea what to do')
        return coordz

#    print('route is {}'.format(route))
    val = int(re.findall(r'[0-9]+', route)[0])
        
    if incx:
        for xs in range(x + (1 * dirc), x + (1 * dirc) + (val * dirc), dirc):
            coordz.append((xs, y))
#            print(xs, y)
            
    if incy:
        for ys in range(y + (1 * dirc), y + (1 * dirc) + (val * dirc), dirc):
            coordz.append((x, ys))
#            print(x, ys)

    return coordz
        
        
#coordinates making
for wire in wires:
    for step in wires[wire]['route']:
        try:
#            print(wires[wire]['coords'])
            lastx = wires[wire]['coords'][-1][0]
            lasty = wires[wire]['coords'][-1][1]
        except IndexError as ex:
            lastx = 0
            lasty = 0
            
        wires[wire]['coords'] += whatcoordinates(lastx, lasty, step)


# find the crossings
print('How many coords in 1: {}'.format(len(wires[1]['coords'])))
print('How many coords in 2: {}'.format(len(wires[2]['coords'])))

intersect = set(wires[1]['coords']) & set (wires[2]['coords'])

manhattan_distance = 100000000000
for coordz in intersect:
    dist = abs(coordz[0]) + abs(coordz[1])
    if dist != 0 and dist < manhattan_distance:
        manhattan_distance = dist


#print(intersect)
steps1 = 100000000000
steps2 = 100000000000
togethersteps = 1000000000000
for coordz in intersect:
    idx1 = wires[1]['coords'].index(coordz) + 1
    idx2 = wires[2]['coords'].index(coordz) + 1
    if idx1 + idx2 < togethersteps:
        togethersteps = idx1 + idx2

    print('steps1 {}'.format(idx1))
    print('steps2 {}'.format(idx2))

print('lowest steps: {}'.format(togethersteps))

# holy shit this is slow as fuck, the set intersection above is sooooo much faster
# manhattan_distance = 100000000000
# for coord1 in wires[1]['coords']:
#     for coord2 in wires[2]['coords']:
#         if coord1 == coord2:
#             dist = abs(coord1[0]) + abs(coord1[1])
#             if dist != 0 and dist < manhattan_distance:
#                 manhattan_distance = dist
#             print('{} equals {}'.format(coord1, coord2))


print('shortest distance is {}'.format(manhattan_distance))
#print(wires)
