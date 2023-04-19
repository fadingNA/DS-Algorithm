class BST:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)

        insert = True
        curr = self.root
        while insert:
            if data < curr.data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = BST.Node(data)
                    insert = False

            elif data > curr.data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = BST.Node(data)
                    insert = False
            else:
                break

    def print_tree(self):
        def print_helper(node):
            if node is None:
                return
            else:
                print_helper(node.left)
                print(node.data)
                print_helper(node.right)

        print_helper(self.root)


if __name__ == "__main__":
    test_tree = BST()
    test_tree.insert(10)
    test_tree.insert(8)
    test_tree.insert(30)
    test_tree.insert(15)
    test_tree.insert(27)
    test_tree.insert(7)
    test_tree.insert(11)
    test_tree.print_tree()
