# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class LinearProbingTS:
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

    def __init__(self, cap=32):
        self.cap = cap
        self.the_table = [[] for i in range(self.cap)]
        self.length = 0

    def insert(self, key, value):
        """ Inserts a new record with the given key and value """
        idx = hash(key) % self.cap
        for record in self.the_table[idx]:
            if record[0] == key:
                return False
        if (1.0 * self.length / self.cap) > 0.7:
            self._grow()
        self.the_table[idx].append((key, value))
        self.length += 1
        return True

    def modify(self, key, value):
        """ Modifies the value of the record with the given key """
        idx = hash(key) % self.cap
        for num, record in enumerate(self.the_table[idx]):
            if record[0] == key:
                self.the_table[idx][num] = (key, value)
                return True
        return False

    def remove(self, key):
        """ If no matching key exists, return False. Otherwise, return True """
        index = hash(key) % self.cap
        for num, record in enumerate(self.the_table[index]):
            if (record[0] == key):
                del self.the_table[index][num]
                self.length -= 1
                return True

            return False

    def search(self, key):
        """ Returns value of record with matching key. If nothing matching, return None """
        idx = hash(key) % self.cap
        for record in self.the_table[idx]:
            if record[0] == key:
                return record[1]
        return None

    def capacity(self):
        """ Checks for number of available spots in the table """
        return self.cap

    def __len__(self):
        return self.length

    def _grow(self):
        self.cap *= 2
        tmp = self.the_table
        self.the_table = [None] * self.cap
        self.length = 0
        for i in tmp:
            if i is not None:
                index = hash(i.key) % self.cap
                while self.the_table[index] is not None:
                    index = (index + 1) % self.cap
                self.the_table[index] = i
                self.length += 1



class LinearProbingNoTS:
    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.the_table = value

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use linear probing for collision resolution)

    def __init__(self, cap=32):
        self.cap = cap
        self.the_table = [None] * self.cap
        self.length = 0
        self.max_load_factor = 0.70

    def insert(self, key, value):
        """ Adds a new key-value pair to the table. If exists, return False, Othersise adds new key-value and return True. If adding the new record causes the load factor to exceed 0.7,
        you must grow your table by doubling its capacity """
        self.length += 1
        hashed_key = hash(key) % self.cap

        while self.the_table[hashed_key] is not None:
            if self.the_table[hashed_key][0] == key:
                self.length -= 1
                return False

            hashed_key = self._hash(hashed_key)

        if self.length / float(self.cap) >= self.max_load_factor:
            self._grow()
        tuple = (key, value)
        self.the_table[hashed_key] = tuple
        return True

    def modify(self, key, value):
        """ Modifies existing key-value pair into the table. If no matching record, returns False. Otherwise,
        modifies the changes the existing value into the one passed into the function and returns True """
        index = hash(key) % self.cap
        record = index
        while self.the_table[index] is not None and index != record - 1:
            if (self.the_table[index][0] == key and self.the_table[index][0] != None):
                self.the_table[index] = (key, value)
                return True

            index = self._hash(index)
        return False

    def remove(self, key):
        count = 0
        for item in self.the_table:
            if (item is not None):
                if (item[0] == key):
                    self.the_table[count] = None
                    self.length -= 1
                    return True
            count += 1
        return False

    def search(self, key):
        for item in self.the_table:
            if (item is not None):
                if (item[0] == key):
                    return item[1]
        return None

    def capacity(self):
        return self.cap

    def _len_(self):
        if (self.length > self.cap):
            self.length -= 1
        return self.length

    def _grow(self):
        self.cap *= 2
        old_table = self.the_table
        self.length = 0
        for item in old_table:
            if item is not None:
                key, value = item
                index = self.hash(key) % self.cap
                while self.the_table[index] is not None:
                    if self.thhe_table[index][0] == key:
                        break
                    index = (index + 1) % self.cap
        self.the_table[index] = (key, value)
        self.length += 1

    def _hash(self, key):
        return (key + 1) % self.cap
