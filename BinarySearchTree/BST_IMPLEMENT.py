class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = Node(node)
        else:
            self._insert(node, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)

        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree!")
            return value

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)


def binary_sum(str):
    output = f"The space complexity of Average Case is O(n)"
    output2 = f"The space complexity of Worst Case is O(n)"
    output3 = f"The space complexity of Average Case is O(log n)"
    if str == "Space":
        print(output)
        print(output2)
    if str == "Access":
        print(output)
        print(output2)
    if str == "Search":
        print(output3)
        print(output2)
    if str == "Insert":
        print(output)
        print(output2)
    if str == "Delete":
        print(output)
        print(output2)


def fill_tree(tree, num_elemes=100, max_int=1000):
    from random import randint
    for i in range(num_elemes):
        current = randint(0, max_int)
        tree.insert(current)
    return tree


def maisn():
    tree = Tree()
    fill_tree(tree)


if __name__ == "__main__":
    binary_sum("Insert")
    maisn()
