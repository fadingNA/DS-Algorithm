class SetList:
    class Node:
        # Constructor of Node inside the container name SetList
        def __init__(self, data, set_list=None, next_node=None, prev_node=None):
            self.data = data
            self.next_node = next_node
            self.prev_node = prev_node
            self.set_list = set_list

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def get_previous(self):
            return self.prev_node

        def get_set(self):
            return self.set_list

    def __init__(self):
        self.front = None
        self.back = None

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    """
    The make_set function 
    1. check the very front of the setlist is available or not 
    1.1 if yes we create new Set with data provided
    1.1.1  Then we point front and back of SetList to the new_node
    1.2 if no this function do nothing
    """
    def make_set(self, data):
        if self.front is None:
            new_node = SetList.Node(data, self)
            self.front = new_node
            self.back = new_node
            # print(self.front.data)
            return self.front
        else:
            return None
    """
    This function loop through the entire of Setlist and check how many node contains in the List
    Continue loop by using next_node until the tempory node is None
    Note: each time node loop we assign cou += 1
    """
    def __len__(self):
        tmp = self.front
        cou = 0
        while tmp is not None:
            cou += 1
            tmp = tmp.next_node
        return cou

    """
    The function updates the "prev_node" and "next_node" pointers of each node 
    and also updates the "set_list" pointer of each node to point back to the current set.
    
    """

    def union_set(self, other_set):
        count = 0
        cur_n = other_set.front
        while cur_n:
            """
            store the next and previous pointer of other_set
            for looping and pointing, 
            next step set other.set.next point to self.front of set new setlist
            """
            nxt = cur_n.next_node
            prv = cur_n.prev_node
            cur_n.next_node = self.front
            if self.front:
                # self.front.prev node -> point to new setList
                self.front.prev_node = cur_n
            #set front node of the list to front node of other setList
            self.front = cur_n
            cur_n.set_list = self
            count += 1
            cur_n = nxt
            # if curr is the back_node, modify to link the backList
            if cur_n == self.back:
                self.back = prv
                self.back.next_node =None
        if self.back:
            self.back.prev_node = self.front
        other_set.front, other_set.back = None, None
        other_set.set_list = None
        return count


    """
    Find_data just iterate over the node inthe setList and check each node that match the 
    data provided from parameter or no if yes return the node that contain the data we are looking for
    """
    def find_data(self, data):
        current = self.front
        #print(current.data)
        while current:                  # As ususal use self.front to iteration over the setList
            if current.data == data:
                return current
            current = current.next_node # If not found set to the next node.
        return None


    """
    This function returns the representative node of the setList.
    If the front node is not NOne, is is the representative.
    """
    def representative_node(self,node=None):

        if self.front is not None:
            return self.front
        # if a node is provided, it is the representative
        elif node is not None:
            return node
        # Otherwise, no representative.
        else:
            return None
    """
    This function returns the representative of the set.
    If a node is provided, it is the representative.
    """
    def representative(self,node=None):

        if node is not None:
            #print(node)
            return node
        # If the front node is not None, its data is the representative
        if self.front is not None:
            return self.front.data
        else:
            return None