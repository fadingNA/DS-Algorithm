class SortedTable:
    # packaging they key value pair inot one object
    class Record:
        def __init__(self, keys=None, values=None):
            self.key = keys
            self.value = values

    def __init__(self, cap=32):
        # this initializes a list of ocapapcity length with None
        self.the_table = [None for i in range(cap)]
        self.cap = cap

    def insert(self, key, value):
        if self.search(key) is not None:
            return False

        if len(self) == self.cap:
            new_table = [None for i in range(self.cap * 2)]
            for i in range(self.cap):
                new_table[i] = self.the_table[i]
            self.the_table = new_table
            self.cap *= 2

        self.the_table[len(self)] = self.Record(key, value)
        size = len(self)
        # perform sorted insertion
        for i in range(0, size - 1):
            for j in range(0, size - 1 - i):
                if self.the_table[j].keys > self.the_table[j + 1].keys:
                    tmp = self.the_table[j]
                    self.the_table[j] = self.the_table[j + 1]
                    self.the_table[j + 1] = tmp
        return True

    def modify(self, key, value):
        i = 0
        while i < len(self) and self.the_table[i].keys != key:
            i += 1
        if i == len(self):
            return False
        else:
            self.the_table[i].values = value
            return True
    """
    loop through size of table and check keys is not key we want to remove
    increment i by 1
    if i reach size return false cannot remove
    no check if i increment 1 if above size we assume that this is last key of
    the table set table[i] = nullptr
    
    if not above size
    we switch table till reach the last index
    [1] [2] [3] [4] [5]
    [1] [3] [2] [4] [5]
    [1] [3] [4] [2] [5]
    [1] [3] [4] [5] [2 X remove] 
    """
    def remove(self, key):
        i = 0
        size = len(self)
        while i < size and self.the_table[i].keys is not key:
            i += 1
        if i == size:
            return False
        else:
            while i + 1 < size:
                self.the_table[i] = self.the_table[i + 1]
                i += 1
            self.the_table[i] = None
        return True

    """
    searching function pass parameter by key {key,value}
    loop through the table and check i is not above the len of table
    if i increment equal to size the function return False nothing in the search
    if not =! return table position [i] . value
    """

    def search(self, key):
        i = 0
        size = len(self)
        while i < size and self.the_table[i].keys is not key:
            i += 1
        if i == size:
            return None
        else:
            return self.the_table[i].values

    """
    query function for capacity of table.
    """

    def capacity(self):
        return self.cap

    """
    Create constant for counting iteration
    check condition table position i is not nullptr
    count += 1
    basically check how many key in the table by count 
    and then return count
    """

    def __len__(self):
        i = 0
        count = 0
        while i < len(self.the_table):
            if self.the_table[i] is not None:
                count += 1
            i += 1
        return count


"""
Hash table is uses key of eaach record to determine the location in an array structure.
To do this the key is passed into a hash function which will then return a numberic
value based on the key.

Hash function
A hash function must be designed so that given a certain key it will always reutrn
the same numeric value. Furthermore, the hash function will ideally distribute all possible
keys in the key space uniformly over all possible locations.

For instance, support we wanted to create a table for storing customer information
at store for the key, a customer's telephone number is used. the table can hold up
to 10,000 records and thus valid indexes for an array of that size would be [0 - 9999]
cap = 9999
self.table = [None for i in range(cap)]
"""