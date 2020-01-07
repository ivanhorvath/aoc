with open('input') as file:
    data = file.readline().split()

class Node(object):
    def __init__(self):
        self.childcount = 0
        self.metacount = 0
        self.children = []
        self.metadata = []

    def process(self, stuff):
        self.childcount = int(stuff[0])
        self.metacount = int(stuff[1])
        stuff = stuff[2:]
        if self.childcount > 0:
            for kid in range(self.childcount):
                newkid = Node()
                stuff = newkid.process(stuff)
                self.add_child(newkid)
        self.metadata = stuff[:self.metacount]
        return stuff[self.metacount:]

    def add_child(self, child):
        self.children.append(child)

    def display(self):
        print('kids {} meta {} metaz: {}'.format(self.childcount, self.metacount, self.metadata))
        for x in range(self.childcount):
            self.children[x].display()

    def totalmeta(self):
        total = 0
        for x in self.metadata:
            total += int(x)
        for x in range(self.childcount):
            total += self.children[x].totalmeta()
        
        return total

    def valueof(self):
        total = 0
        for idx in self.metadata:
            iidx = int(idx) - 1
            if self.childcount > 0:
                try:
                    total +=self.children[iidx].valueof()
                except IndexError as ex:
                    pass
            else:
                total += int(idx)
        return total

root = Node()
root.process(data)

root.display()

print(root.totalmeta())

print(root.valueof())
