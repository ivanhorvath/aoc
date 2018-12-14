import pprint

with open('/home/ihorvath/code/aoc/7/input') as file:
    inst = file.read().splitlines()

# inst.sort()

class Node(object):
    def __init__(self, name):
        self.name = name
        self.prereq = []



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




pprint.pprint(steps)
    