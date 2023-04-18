def printInorder(r):
    if r:
        # first recur on left child
        printInorder(r.l)
        print(r.data)
        printInorder(r.r)


class BST:
    class Node:
        def __init__(self, data, r=None, l=None):
            self.data = data
            self.r = r
            self.l = l

    def __init__(self):
        self.root = None

    def ins(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            curr = self.root
            flag = True
            while flag:
                if data < curr.data:
                    if curr.l is not None:
                        curr = curr.l
                    else:
                        curr.l = BST.Node(data)
                        flag = False
                if data > curr.data:
                    if curr.r is not None:
                        curr = curr.r
                    else:
                        curr.r = BST.Node(data)
                        flag = False

        return None

    def postOrder(self, r):
        # O(n)
        # Balance (Log N)
        # not Balance (O N)
        stack = [r]  # all the node
        visited = [False]  # boolean
        res = []
        while stack:
            current, v = stack.pop(), visited.pop()
            if current:
                if v:
                    res.append(current.data)
                else:
                    # Take all tree and add to the stack.
                    stack.append(current)
                    visited.append(True)
                    stack.append(current.right)
                    visited.append(False)
                    stack.append(current.left)

            """
            Add root to the stack first
            and then add right to the stack
            """

    def bfs(self):
        if root is None:
            return
        queue = [self.root]
        stack = []

        while len(queue) > 0:
            cur_node = queue.pop(0)
            print(cur_node.data)
            stack.append(cur_node)
            if cur_node.l is not None:
                queue.append(cur_node.l)
            if cur_node.r is not None:
                queue.append(cur_node.r)

    def count_leaf_node(self):
        if not self.root:
            return 0
        count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            if not node.l and not node.r:
                count += 1
            if node.l:
                stack.append(node.l)
            if node.r:
                stack.append(node.r)
        print(count)
        return count

    def find_sum(self, node, sum):
        if node is None:
            return False
        if node.l is None and node.r is None:
            return node.data == sum
        left_sum = self.find_sum(node.l, sum - node.data)
        right_sum = self.find_sum(node.r, sum - node.data)
        return left_sum and right_sum

    def find_sum2(self, node):
        if node is None:
            return 0
        return node.data + self.find_sum2(node.l) + self.find_sum2(node.r)

    # Write a Python method in class BST that returns the maximum value in the tree using search.
    def max_value(self, n):
        if n is None:
            return None
        elif n.r is None:
            return n.data
        else:
            return self.max_value(n.r)

    # Write a Python method in class BT that returns the sum of all node values in the tree using post-order traversal.
    def post_sums(self, node):
        if node is None:
            return 0
        left_sum = self.post_sums(node.l)
        right_sum = self.post_sums(node.r)
        return node.data + left_sum + right_sum

    # Write a recursive function to count the number of nodes in a binary tree.
    def count_node(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_node(node.l) + self.count_node(node.r)

    # Write a Python method in the class BT that traverses the binary tree and returns the sum of all nodes that have
    # an even value. You must use the pre-order traversal algorithm
    def sum_inOrder(self, node):
        if node is None:
            return 0
        c_sum = 0
        if node.data % 2 == 0:
            print(node.data)
            c_sum = node.data
        left_sum = self.sum_inOrder(node.l)
        r_sum = self.sum_inOrder(node.r)
        return c_sum + left_sum + r_sum

    # Create a method named find_min_diff in class BST that takes a value x as input and returns the minimum
    # difference between that value and any other value in the BST. Your method should use iterative binary search to
    # search the tree for the closest value, and then return the difference between that value and x. Assume that
    # values in the BST are unique.
    def find_min_diff(self, x):
        if self.root is None:
            return False
        min_dif = float('inf')
        cur = self.root
        while cur:
            min_dif = min(min_dif, abs(cur.data - x))
            if x < cur.data:
                cur = cur.l
            elif x > cur.data:
                cur = cur.r
            else:
                return 0
        return min_dif

    # Write an iterative method in the BT class called print_leaf_nodes that prints all the leaf nodes of the binary
    # tree using an in-order traversal. A leaf node is defined as a node without any children. Make sure to include
    # the inner class Node and the constructor in the BT class.
    def print_leaf_node(self):
        if self.root is None:
            return None

        def inOrder_print(node):
            if node is None:
                return
            inOrder_print(node.l)
            # if node.l is None and node.r is None:
            print(node.data, end=" ")
            inOrder_print(node.r)

        inOrder_print(self.root)


"""
Node => Null
"""

if __name__ == "__main__":
    print("===========INSERT=============")
    root = BST()
    root.ins(10)
    root.ins(20)
    root.ins(7)
    root.ins(9)
    root.ins(11)
    # printInorder(root.root)
    root.bfs()
    # root.count_leaf_node()
    print("============================")
    # print(root.find_sum2(root.root))
    print("MAXMIMUM value <", root.max_value(root.root), ">")
    print("SUM VALUE <", root.post_sums(root.root), ">")
    print("COUNT NODE <", root.count_node(root.root), ">")
    print("Even Node Sum <", root.sum_inOrder(root.root), ">")
    print("Min dif BST <", root.find_min_diff(8))
    root.print_leaf_node()
    print("============================")
