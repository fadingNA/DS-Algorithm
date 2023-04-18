from a1_partb import SetList

class DisjointSet:
    def __init__(self):
        self.disjoin_elements = {}
        self.set_counter = 0

    # If element already exists within the Disjoint set, the function does nothing and returns false.
    def make_set(self, element):
        if element in self.disjoin_elements:
            return False
        else:
            newSetNode = SetList().make_set(element)                    # create a instance by calling the member function 'make_set' from SetList
            self.disjoin_elements.update({element: newSetNode})         # adding the element as key and created node instance as value into dictionary
            self.set_counter += 1                                       # increase counter by 1
            return True

    # Function returns the representative of the set containining element.
    def find_set(self, element):
        if element not in self.disjoin_elements:
            return None
        else:
            # Reference to element's SetList first then returns representative node data
            return self.disjoin_elements[element].get_set().representative()

    # This function returns the number of sets in the DisjointSet
    def get_num_sets(self):
        return self.set_counter

    # This function returns the number of elements in the DisjointSet.
    def __len__(self):
        return len(self.disjoin_elements)

    # This function returns the size of the set containing element
    def get_set_size(self, element):
        representative = self.find_set(element)
        size = 0
        if (representative):
            for i in self.disjoin_elements:
                if self.find_set(i) == representative:
                    size += 1
        return size

    # This function performs a union of the two sets containing element1 and element2 respectively.
    def union_set(self, element1, element2):
        a = self.find_set(element1)             # representative for element 1 set
        b = self.find_set(element2)             # representative for element 2 set
        if a != b:      # if both node contains representative value and doe not match to each other //updated for assignment 3, condition check for None removed

            self.disjoin_elements[b].get_set().union_set(self.disjoin_elements[a].get_set())    # calling the member function 'union_set()' from SetList to union the representatives of both element
            self.set_counter -= 1                                                               # decrease the set counter since it has been unify
            return True
        else:
            return False