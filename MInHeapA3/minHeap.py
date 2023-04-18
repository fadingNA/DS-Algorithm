# A class for a min heap
class MinHeap:
    def __init__(self, arr=[]):
        self.heap = []
        self.length = 0
        for i in arr:
            # calling insert function
            # is automatic heapify the element in the sequence
            self.insert(i)

    # Formula to find node
    # parent node = index // 2
    # left_node = index * 2
    # right_node = index * 2 + 1
    # note when become in the programming part we need to plus 1 index to achieve the result.

    """
    This purpose of this function to generate the identify the parent node;
    by : pass the the index of the current node and - 1 then divide by 2 
    divide by 2 because to go upper level of the child node.
    """
    def parent_node(self, pos):
        return (pos - 1) // 2

    """
    The purpose of this function is almost identical with the parent_node above
    to get the position index of the left_child of the node by multiply by 2 and then plus 1
    plus because will go to the left node
    """
    def left_child(self, pos):
        left_child_pos = 2 * pos + 1
        return left_child_pos if left_child_pos < len(self.heap) else None

    """
    The purpose of this function similar to the left_child function 
    just change the formula to me multiply by 2 and then plus to
    go to the right node.
    """
    def right_child(self, pos):
        right_child_pos = 2 * pos + 2
        return right_child_pos if right_child_pos < len(self.heap) else None

    """
    The swap function is optional for the minHeap to swap the node in the tree
    function perform by current-position node as the first parameter and the second parameter as the
    designation that node will change to.
    
    In addition, the function also check index 1 is exceed the length of min heap of not
    if not the function perform nothing.
    """
    def swap(self, pos1, pos2):
        if pos1 >= len(self.heap) or pos2 >= len(self.heap):
            return None
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    """
    Insert function of the minheap to insert the new_node into the tree and then perform
    heapify in this case we do heapifyUp by the priority_queue of the min value.
    and then after finish heapify, we increase the length of the minheap-tree by 1
    """
    def insert(self, element):
        self.heap.append(element)
        self.heapifyUp(len(self.heap) - 1)
        self.length += 1

    """
    HeapifyUp function as the mentioned above we check the parent node
    of any given node 'i' is located at index i // 2
    The function compare the value at index i with its parent node,
    and if the value is smaller the two nodes are swapped. This
    process is repeated until the heap property is restored. 
    
    The function achieves this by using a loop that continues as long as i is greather than 0
    and then perform the swap with the smaller value.
    """
    def heapifyUp(self, i):
        p_node = self.parent_node(i)
        while i > 0 and self.heap[i] < self.heap[p_node]:
            self.swap(i, p_node)
            # debug
            # print(f"swapped {self.heap[i]} and"
            # f"{self.heap[p_node]} : "
            # f"{self.heap}")
            i = p_node
            p_node = self.parent_node(i)
        # print(f"Final hepifyUp : {self.heap}")

    """
    The function isLeaf is a method of a class take a parameter pos as input
    the function is used to check if a given position in a binary heap 
    data structure is a leaf node or not.
    
    The function returns a boolean value True or False depending on wheter the position pos is a leaf node
    or not. If pos is a leaf node the function return True; otherwise it returns 
    False.
    """
    def isLeaf(self, pos):
        n = len(self.heap)
        return self.left_child(pos) >= n

    """
    The function minHeapfiy is a property state that the value of each node should be less than or equal to the values of its children.
    So the function achieves this by repeatedly comparing the value at position pos that pass by parameter
    and perform swaping by calling swap function.
    
    The fucntion determines the minimum value among the current node at position pos
     and its children b comparing their  values. If the left child index is not None
     and its value is less than the current min, the current min is upadted to be the left child
     index.
     
     Finally, when the loop is completed, the function sets the flag to False to indicate that the
     heap property has been restored.
     
     Return Nothing.
    """
    def minHeapify(self, pos):
        flag = True
        while flag:
            left = self.left_child(pos)
            right = self.right_child(pos)
            min = pos
            if left is not None and self.heap[left] < self.heap[min]:
                min = left
            if right is not None and self.heap[right] < self.heap[min]:
                min = right
            if min != pos:
                self.swap(pos, min)
                pos = min
            else:
                flag = False

    """
    Get minimum value in the binary-heap-tree and at the first index.
    but if lenght of heap-tree is empty we return 0.
    """
    def get_min(self):
        return None if len(self.heap) == 0 else self.heap[0]

    """
    Extract min that  determine the minimum value in the binary-heap-tree and then
    store in the temporary value and swap the swap value into the first value
    if the swap value is not the last node of the tree we set the first index
    of the tree to the remove position and the perform heapify
    to make the node into the correct position
    
    Return Minimum value that store inthe temporary value.
    """
    def extract_min(self):
        if self.is_empty():
            return None
        minVal = self.heap[0]
        lastVal = self.heap.pop()
        self.length -= 1
        if not self.is_empty():
            self.heap[0] = lastVal
            self.minHeapify(0)
        return minVal

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return self.length

    def print_heap(self):
        for i in range(self.length):
            print(self.heap[i], end=" ")
        print()


# Driver Code
if __name__ == "__main__":
    minHeap = MinHeap()

    # create array to test insert
    non = [3, 4, 1, 2, 9, 12, 13, 8, 9]
    for i in range(len(non)):
        minHeap.insert(non[i])

    minHeap.print_heap()
    print(minHeap.get_min())
