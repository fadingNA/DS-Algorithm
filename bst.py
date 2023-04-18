import queue
class BST:
    class Node:
        # node's init function
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insrt(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            # curr points to the variable we are currently looking at
            curr = self.root
            flag = False
            while not flag:
                if data < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = BST.Node(data)
                        flag = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(data)
                        flag = True

    def search(self, data):
        curr = self.root
        while curr:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
        return None

    def bfp(self):
        node = queue.Queue()
        if self.root:
            node.put(self.root)
        while not node.empty():
            curr = node.get()
            if curr.left:
                node.put(curr.left)
            if curr.right:
                node.put(curr.right)
            print(curr.data, end=" ")
