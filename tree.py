# 2-3 Tree
# balanced tree data structure with up to 2 data item per node

class Node:
    def __init__(self, data, par=None):
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + ' : ' + str(self.data)
        return 'Root : ' + str(self.data)

    def __lt__(self, node):
        return self.data[0] < node.data[0]

    # merge new node sub-tree into self-node
    def add(self, data):
        for child in data.data:
            child.parent = self
        self.data.extend(data.data)
        self.data.sort()
        self.child.extend(data.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.data) > 2:
            self._split()

    def insert(self, new_node):
        if self._isLeaf():
            self.add(new_node)
        elif new_node.data[0] > self.data[-1]:
            self.child[-1].insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] < self.data[i]:
                    self.child[i].insert(new_node)
                    break
