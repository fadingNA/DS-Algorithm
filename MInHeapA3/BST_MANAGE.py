from BST import BST

if __name__ == "__main__":
    print("========== START ALGORITHM ==========")

    # Initial Array of 15 value
    arr = [4, 5, 62, 435, 6, 7, 9, 14, 69, 23, 42, 65, 43, 21, 1, 2, 47]
    tree = BST()
    for i in range(len(arr) - 1):
        tree.ins(arr[i])

    print(tree.print_leaf_node())

    # Sure! Here are some application-based use cases for your BST implementation:

    # Data Sorting: You can use your BST implementation to sort a collection of data items. By inserting the data
    # items into the BST and then performing an in-order traversal, you can obtain the sorted order of the data
    # items. This can be useful in applications where you need to sort and retrieve data efficiently, such as sorting
    # a list of names or numbers.
    #
    # Counting Nodes with Values Less Than a Target Value: Your BST implementation can be used to count the number of
    # nodes in the tree that have values less than a given target value. This can be useful in applications where you
    # need to perform statistical analysis or gather information based on certain criteria, such as counting the
    # number of students who scored less than a certain threshold in an exam.
    #
    # Finding the Second Largest Value: Your BST implementation can be used to find the second largest value in the
    # tree, which can be useful in applications where you need to retrieve the second highest element from a
    # collection of data, such as finding the second highest salary in a list of employees or the second highest
    # score in a leaderboard.
    #
    # Checking for the Presence of a Value: Your BST implementation can be used to check whether a particular value exists in the tree or not. This can be useful in applications where you need to validate user input or search for a specific item in a collection of data, such as checking whether a certain product is available in an e-commerce inventory or whether a word exists in a dictionary.
    #
    # Computing the Sum of All Nodes: Your BST implementation can be used to compute the sum of all the nodes in the tree. This can be useful in applications where you need to calculate the total of a particular attribute or value associated with each node, such as calculating the total cost of all items in a shopping cart or the total revenue from a list of sales transactions.
    #
    # Counting Leaf Nodes: Your BST implementation can be used to count the number of leaf nodes in the tree, which are the nodes that do not have any children. This can be useful in applications where you need to perform analysis or calculations based on the structure of the tree, such as counting the number of endpoints in a network graph or the number of terminal nodes in a decision tree.
    #
    # Finding the Maximum Value: Your BST implementation can be used to find the maximum value in the tree, which can be useful in applications where you need to retrieve the highest element from a collection of data, such as finding the highest score in a list of test results or the highest price in a list of products.
    #
    # Inserting and Deleting Nodes: Your BST implementation allows for inserting new nodes with specified values into the tree, as well as deleting nodes with specified values from the tree. This can be useful in applications where you need to dynamically add or remove data items from a collection of data, such as managing a database or maintaining a dynamic data structure.
    #
    # These are just a few examples of how your BST implementation can be used in various applications. Depending on your specific use case, you may need to modify or extend your BST implementation to suit the requirements of your application.

    print("========== END ALGORITHM   ==========")
