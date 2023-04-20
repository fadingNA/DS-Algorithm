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
        self.count = 0

    def __str__(self):
        return str(self.root)

    def print(self):
        return self.root.data

    # Consider a binary search tree BT and a value x. Write a method, count_less_than_x, in the class BT that will
    # recursively count the number of nodes in the tree that have a value less than x. Use the in-order traversal
    # approach of visiting the left subtree, then the current node, and then the right subtree.
    def count_less_than_target(self, x):
        self.count = 0
        self.count_helper(self.root, x)
        return self.count

    def find_lowest_common_ancestor(self, value1, value2):
        if self.root is None:
            return None
        return self.ancester_helper(self.root, value1, value2)

    """
    The find ancestor method first checks if the BST is empty or not
    If it is it return None, Otherwise :
    Call helper function method recursively on the root of the binary search tree.
    The helper method caompares the given values " value 1 " and value 2 with the value
    of the current node = (node.data) comepare to detemrine whether to continue searching in the 
    left subtree or right subtree or if the current node is the lowest common ancestor. Once the
    lowest common ancestor is found it is returnde by the method
        """

    def ancester_helper(self, node, value1, value2):
        if node is None:
            return None
        if value1 < node.data and value2 < node.data:
            return self.ancester_helper(node.left, value1, value2)
        if value1 > node.data and value2 > node.data:
            return self.ancester_helper(node.right, value1, value2)
        else:
            return None

    def count_helper(self, node, x):
        if node is None:
            return
        # Inorder -> Left -> Print -> Right
        self.count_helper(node.l, x)
        if node.data < x:
            self.count += 1
        self.count_helper(node.r, x)

    def max_value_preorder(self):
        # Helper function for pre-order traversal to find the maximum value
        def preorder_helper(node):
            if node is None:
                return float('-inf')  # Return negative infinity for comparison
            max_left = preorder_helper(node.l)  # Recursively traverse left subtree
            max_right = preorder_helper(node.r)  # Recursively traverse right subtree
            return max(node.data, max_left, max_right)  # Return maximum value among current node and its subtrees

        return preorder_helper(self.root)

    # In this implementation, the find_second_largest method uses a recursive helper function _in_order_traversal to
    # perform an in-order traversal of the binary search tree in reverse order (right, root, left) and keep track of
    # the count of nodes visited. When the count becomes 2, the method returns the value of the node as the second-
    # largest value in the tree. If the tree has fewer than 2 nodes, the method returns None.
    def find_second_largest(self):
        if self.root is None:
            return None

        def in_order_traversal(node, count):
            if node is None:
                return None

            right_tree = in_order_traversal(node.r, count)
            if right_tree is not None:
                return right_tree

            count[0] += 1
            if count[0] == 2:
                return node.data
            return in_order_traversal(node.r, count)

        count = [0]
        second_largest = in_order_traversal(self.root, count)
        if count[0] < 2:
            return None
        return second_largest

    def is_value_present(self, value):
        return self.helper_is_value(self.root, value)

    def helper_is_value(self, node, value):
        if node is None:
            return False
        if node.data == value:
            return True
        if value < node.data:
            return self.helper_is_value(node.l, value)
        else:
            return self.helper_is_value(node.r, value)

    def is_value_present_inorder(self, value):
        return self.helper_inorder_value(self.root, value)

    def sum_all_node(self):
        return self.sum_helper(self.root, 0)

    def sum_helper(self, node, sum5):
        if node is None:
            return 0
        lef = self.sum_helper(node.l, sum5)
        rig = self.sum_helper(node.r, sum5)
        return node.data + lef + rig

    def helper_inorder_value(self, node, value):
        if not node:
            return False
        if self.helper_inorder_value(node.l, value):
            print(node.data)
            return True
        if node.data == value:
            return True
        return self.helper_inorder_value(node.r, value)

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

    def search(self, data):
        cur = self.root
        while curr:
            if data < cur:
                cur = cur.left
            if data > cur:
                cur = cur.right
            else:
                return cur
        return None

    def search_inorder(self, data):
        if self.root:
            if data == self.search_inorder(self.root.l):
                return True
            if data == self.search_inorder(self.root.r):
                return True

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
        return counะ

    def sum_max_value(self):
        def helper(node):
            if node is None:
                return
            max_value = max(lt, rt)
            left = helper(node.l)
            right = helper(node.r)
            return max_value

        return helper(self.root)

    def find_sum(self, node, sum):
        if node is None:
            return False
        if node.l is None and node.r is None:
            return node.data == sum
        left_sum = self.find_sum(node.l, sum - node.data)
        right_sum = self.find_sum(node.r, sum - node.data)
        return left_sum + right_sum

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
    def height(self):
        if self.root is None:
            return 0
        height = 0
        stack = [self.root]
        while stack:
            level = len(stack)
            for i in range(level):
                node = stack.pop(0)
                if node.l:
                    stack.append(node.l)
                if node.r:
                    stack.append(node.r)
            height += 1
        return height

    def height_recur(self):
        def height_helper(node):
            if node is None:
                return 0
            else:
                hl = height_helper(node.l)
                hr = height_helper(node.r)
                return max(hl, hr) + 1

        return height_helper(self.root)

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
            print("Even Node found: ", node.data)
            c_sum = node.data
        print("traversing left subtree of node with data:", node.data)
        left_sum = self.sum_inOrder(node.l)
        print("traversing right subtree of node with data:", node.data)
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
    def iterative_in_order(self):
        stack = []
        node = self.root
        while True:
            while node is not None:
                stack.append(node)
                node = node.l
            if len(stack) == 0:
                return
            node = stack.pop()
            print(node.data, end=" > ")
            node = node.r

    def print_between(self, min, max):
        print(min, max)
        print("=======")

        def print_between_helper(node, min, max):
            if node is None:
                return
            if min < node.data:
                print_between_helper(node.l, min, max)
            if min < node.data < max:
                print(node.data)
            if max > node.data:
                print_between_helper(node.r, min, max)

        print_between_helper(self.root, min, max)

    def print_leaf_node(self):
        if self.root is None:
            return None

        def inOrder_print(node):
            if node is None:
                return
            inOrder_print(node.l)
            if node.l is None and node.r is None:
                print(node.data, end=" ")
            inOrder_print(node.r)

        inOrder_print(self.root)

    # Write a Python method in a class BST (Binary Search Tree) that takes in a target value as a parameter,
    # and returns the number of nodes in the tree whose value is less than the target value.
    # You must use the search method to first find the node with the target value
    # (if it exists) and then traverse the left subtree of that node to count the number of nodes
    # that are less than the target value.
    def search_less_target(self, node, target):
        count = [0]

        def search_helper(node, target):
            nonlocal count
            if node is None:
                return False
            if node.data < target:
                count[0] += 1
            return search_helper(node.l, target) + search_helper(node.r, target)

        search_helper(self.root, target)
        return count[0]

        def inorderTravelsal(self, root):
            res = []
            stack = []
            curr = root
            while curr or stack:
                while cure:
                    stack.append(curl)
                    curr = curr.left
                curr = stack.pop()
                res.append(cur.val)
                cur = curr.right
            return res

        def incurInOrder(self, rott):
            def inRecur(self, root):
                if not root:
                    return True
                else:
                    inRecur(root.left)
                res.append(root.val)
                inRecur(root.right)

            inOrder(root)
            return res


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
    print("Min dif BST <", root.find_min_diff(8))
    root.print_leaf_node()
    print("\nCounter less than target", root.count_less_than_target(15))
    print("\n Max value of BST <", root.max_value(root.root), ">")
    print("==========INSER AGAIN========")
    root.ins(4)
    root.ins(35)
    root.ins(14)
    print("\n Max value of BST <", root.max_value(root.root), ">")
    print("\n Find second largest value <", root.find_second_largest(), ">")
    root.bfs()
    print("\n Search Less value than target 12 <", root.search_less_target(root.root, 12), ">")
    print("Even Node Sum <", root.sum_inOrder(root.root), ">")
    print("Iterative In-order <", root.iterative_in_order())
    print("\n Find sum 1 and 2, ", root.find_sum2(root.root))
    print("============== CHECK VALUE ================")
    root.bfs()
    print('\n Check value is presented  yet? <', root.is_value_present(7))
    print('\n Check value is presented  yet? <', root.is_value_present_inorder(1))
    print("\n Sum total node value <", root.sum_all_node(), ">")
    print("\n Print between the give value >", root.print_between(7, 15), ">")
    print("\n Height of My tree <", root.height(), ">")
    print("\n Height of My tree <", root.height_recur(), ">")
    print("\n Sum Max Value of all the node<", root.max_value_preorder(), ">")
    print("===========================================")
