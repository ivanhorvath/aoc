with open('input') as file:
    inst = file.read().splitlines()

steps = {}
for i in inst:
    # Step A must be finished before step N can begin.
    arr = i.split()
    step = arr[7]
    prereq = arr[1]

    if step in steps:
        steps[step].append(prereq)
    else:
        steps[step] = [prereq]

order = []
while True:
    temporder = []
    for k,v in steps.items():
        for letta in v:
            if letta not in steps:
                if letta not in temporder:
                    temporder.append(letta)

    temporder.sort()
    candidate = temporder[0]
    for k,v in steps.items():
        if candidate in v:
            del v[v.index(candidate)]

    order.append(candidate)

    if len(steps) == 1:
        for k,v in steps.items():
            if len(v) == 0 and k not in order:
                order.append(k)

    steps = { k:v  for k,v in steps.items() if len(v) >0}

    if len(steps) == 0:
        break

print(''.join(order))
