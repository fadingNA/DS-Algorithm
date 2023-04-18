# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class LinearProbingTS:
    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key=None, value=None, label="Empty"):
            self.key = key
            self.value = value
            """
            Empty - nothing has ever been inserted into this spot
            Used/Occuppied - a record is stored here
            Deleted - something was here but it has been deleted. Note this is NOT exactly the same as empty. You will see why in a moment.
            """
            self.label = label

        # I'm create query string function for return the string value of Record Class
        def __str__(self):
            return f"{self.key} + {self.value} + {self.label}"

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use chaining for collision resolution)

    def __init__(self, cap=32):
        self.arr = [None] * cap
        self.cap = cap
        # initializze length varaible to keep track the length of table.
        self.length = 0
        # make one pointer to ready for delete of the key table.
        self.dummy = self.Record(None, None, "Deleted")

    """
    This function is play important role of hashtable because, this class will determine which index will be the key slot
    by hash(key) modulus capacity of the table size.
    """

    def hashIndex(self, key):
        return hash(key) % self.cap

    """
    Resize function when got called will double size of the capacity by 2 and rotate the previous element 
    to the new table.
    = Note = : We need to allocate new table because we are using array to store the key in the table and array is fixed size
    cannot grow larger than initalize size so we have to allocate new table with a new size.
    """

    def resize(self):
        self.cap *= 2
        tmp = self.arr
        self.arr = [None] * self.cap
        self.length = 0
        for i in tmp:
            if i is not None:
                index = self.hashIndex(i.key)
                while self.arr[index] is not None:
                    index = (index + 1) % self.cap
                self.arr[index] = i
                self.length += 1

    """
    The insert function first start for loop of capacity of the table and the find the index of the hashtable
    First Condition check if table slot is None or Label mark as "USED" or not ?
    if condition are true assign the new Record by key and value (k,v) and mark label as USED
    """

    def insert(self, k, v):
        for i in range(self.cap):
            index = (self.hashIndex(k) + i) % self.cap
            if self.arr[index] is None or self.arr[index].label != "USED":
                self.arr[index] = self.Record(k, v, "USED")
                self.length += 1
                if self.length >= self.cap * 0.7:
                    self.resize()
                return True
            elif self.arr[index].key == k:
                break
        return False

    """
    The Modify function is modify the exist key in the hashtable
    check the key in the table match the parameter query or not
    if matched I assigned the new value into the existing keys in the table.
    """

    def modify(self, keys, values):
        index = self.hashIndex(keys)
        num_iterations = 0
        while num_iterations < self.cap and self.arr[index] is not None:
            if self.arr[index].key == keys:
                self.arr[index].value = values
                return True
            # Iterate over the table find the key that want to modify.
            index = (index + 1) % self.cap
            num_iterations += 1
        return False

    """
        This function removes the key-value 
        pair with the matching key. If no record with matching 
        key exists in the table, the function does nothing and 
        returns False. Otherwise, record with matching 
        key is removed and returns True
     """

    def remove(self, keys):
        index = self.hashIndex(keys)
        itr = 0
        print(self.arr[index])
        while itr < self.cap and self.arr[index] is not None:
            if self.arr[index].key == keys and self.arr[index].label == "USED":
                self.arr[index] = self.dummy
                self.length -= 1
                print(self.arr[index])
                return True
            index = (index + 1) % self.cap
            itr += 1
        return False

    """
        This function returns the value of the record with the matching
        key. If no reocrd with matching key exists in the table, 
        function returns None
    """

    def search(self, keys):
        index = self.hashIndex(keys)
        flag = False  # use flag for easy to exit the function. otherwise can make the function overflow.
        while self.arr[index]:
            if self.arr[index].key == keys:
                # print('Found [', self.arr[index].value, ']')
                flag = True
                break
            # these index use for loop through the table
            index += 1
            index %= self.cap
            if index == self.hashIndex(keys):
                break
        if flag:
            return self.arr[index].value
        else:
            return None

    # query the capacity of the table.
    def capacity(self):
        return self.cap

    # query the length of the table.
    def __len__(self):
        return self.length


class LinearProbingNoTS:
    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use linear probing for collision resolution)

    def __init__(self, cap=32):
        self.cap = cap
        self.arr = [None] * cap
        self.length = 0
        # Same concept as linearprobing with tombstone but now we delete element by set to -1 or None
        self.dummy = self.Record(-1, -1)

    """
    This function is play important role of hashtable because, this class will determine which index will be the key slot
    by hash(key) modulus capacity of the table size.
    """

    def hashIndex(self, k):
        return hash(k) % self.cap

    """
    Another method of re-size or grow table 
    """

    def resize(self):
        self.cap *= 2
        newHash = [None for i in range(self.cap)]
        for i in self.arr:
            if i:
                index = self.hashIndex(i.key)
                while newHash[index]:
                    index = (index + 1) % self.cap
                newHash[index] = i
        self.arr = newHash

    """
    Inserts a new key-value pair into the hash table. 
    It first creates a new Record object containing the key-value pair, 
    and then finds the index where it should be inserted using the hashIndex function. 
    If the key already exists in the table, it updates the corresponding value. 
    If the load factor of the table exceeds 0.7 after the insertion, it resizes the table. 
    Returns True if a new key-value pair was added, False if an existing one was updated.
    """

    def insert(self, k, v):
        tmp = self.Record(k, v)
        i = self.hashIndex(k)
        while self.arr[i]:
            if self.arr[i].key == k:
                self.arr[i].value = v
                return False
            else:
                i = (i + 1) % self.cap
        if self.arr[i] is None:
            self.arr[i] = tmp
            self.length += 1
        if self.length > self.cap * 0.7:
            self.resize()
        return True

    """
    Modifies the value associated with a given key. It finds the index of the key using the hashIndex function and 
    then searches for the key by traversing the table linearly. 
    If the key is found, it updates the corresponding value and returns True. Otherwise, it returns False.
    """

    def modify(self, k, v):
        index = self.hashIndex(k)
        itr = 0
        while self.arr[index] and itr < self.cap:
            if self.arr[index].key == k:
                self.arr[index].value = v
                return True
            index = (index + 1) % self.cap
            itr += 1
        return False

    """
    Removes the key-value pair associated with a given key from the hash table. 
    It finds the index of the key using the hashIndex function 
    and then searches for the key by traversing the table linearly.
    If the key is found, it replaces the Record object with a dummy object,
    decrements the length variable, and returns True. Otherwise, 
    it returns False.
    """

    def remove(self, keys):
        i = self.hashIndex(keys)
        while self.arr[i]:
            if self.arr[i].key == keys:
                self.arr[i] = self.dummy
                self.length -= 1
                return True
            i = (i + 1) % self.cap
        return False

    """
    Searches for the value associated with a given key in the hash table.
    It finds the index of the key using the hashIndex function 
    and then searches for the key by traversing the table linearly. 
    If the key is found, it returns the corresponding value. 
    Otherwise, it returns None.
    """
    def search(self, keys):
        index = self.hashIndex(keys)
        while self.arr[index]:
            if self.arr[index].key == keys:
                return self.arr[index].value
            index = (index + 1) % self.cap
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length
