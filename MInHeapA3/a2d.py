# The following class and member functions are implemented in Adjacency matrix method to represent the graph

class Graph:

    # Purpose of this function: A constructor that initializes the graph object
    # Accept arguments of: The self object and the number of vertices that forms the number of rows and columns
    # Restructions: Argument must be greater than 0
    # Return: A graph object
    def __init__(self, number_of_verts):
        if number_of_verts > 0:
            self.num_of_edges = 0  # initialize to 0
            self.num_of_verts = number_of_verts  # initialize by the number of vertices
            self.adj_matrix = [  # create a fixed sized list of fixed sized list (2D array)
                [0 for column in range(number_of_verts)]  # 0 is to indicate there are no edges initially
                for row in range(number_of_verts)
            ]

    # The function to return vertices
    def get_vertices(self):
        vertices = []
        for i in range(self.num_of_verts):
            vertices.append(i)
        return vertices

    # Purpose of this function: Adds a new vertex to the set of vertices by appending a new column and a new row
    # Accept arguments of: The self object, no other argument is needed
    # Restructions: N/A
    # Return: An updated graph object
    def add_vertex(self):
        for row in self.adj_matrix:  # For every row, append a column with value 0
            row.append(0)
        self.adj_matrix.append(
            [0] * (self.num_of_verts + 1))  # Append the new row and initialize each of its node with a value 0
        self.num_of_verts += 1  # increse the number of vertices of the graph by 1

    # Purpose of this function: Creates a directed edge from one vertex to another vertex by setting a weight between them
    # Accept arguments of: self object, start index, end index, and the optional weight (default to 1)
    # Restructions: The argument indexes must be within the range of the existing 2D array
    # Return: If arguments are valid, an edge is created and returns True; If not, return False back to the caller
    def add_edge(self, from_idx, to_idx, weight=1):
        if from_idx >= self.num_of_verts or to_idx >= self.num_of_verts:  # check if the argument indexes are within the arrays' range
            return False
        if self.adj_matrix[from_idx][to_idx] != 0:  # check if the argument edge already exists in the 2D arrays
            return False

        self.adj_matrix[from_idx][to_idx] = weight  # set the weight and edge accroding to the arguments
        self.num_of_edges += 1  # increase the total number of edges by 1
        return True

    # Purpose of this function: Returns the number of recorded edges from the current graph object
    # Accept arguments of: self object
    # Restructions: N/A
    # Return: The number of directed edges
    def num_edges(self):
        return self.num_of_edges

    # Purpose of this function: Returns the number of existing vertices from the current graph object
    # Accept arguments of: self object
    # Restructions: N/A
    # Return: The number of vertices
    def num_verts(self):
        return self.num_of_verts

    # Purpose of this function: Checks if an edge exists between two vertices by checking any valid weight is presented
    # Accept arguments of: self object, start index, end index
    # Restructions: The argument indexes must be within the bound of the graph object
    # Return: Returns True if an edge exists; returns False if arguments are not valid OR no weight can be found between two vertices
    def has_edge(self, from_idx, to_idx):
        if (
                from_idx >= self.num_of_verts or to_idx >= self.num_of_verts):  # check if the argument indexes are within the arrays' range
            return False
        if self.adj_matrix[from_idx][to_idx] > 0:  # check if the argument edge already exists in the 2D arrays
            return True
        return False

    # Purpose of this function: Returns the weight of the edge between two indexes by checking if there is weight exists at the vertex
    # Accept arguments of: self object, start index, end index
    # Restructions: The argument indexes must be within the bound of the graph object AND there is weight at the vertex
    # Return: Returns True if there is weight at the vertex; False if arugments are not valid OR no weight can be found
    def edge_weight(self, from_idx, to_idx):
        if (
                from_idx >= self.num_of_verts or to_idx >= self.num_of_verts):  # check if the argument indexes are within the arrays' range
            return None
        if self.adj_matrix[from_idx][to_idx] == 0:  # if the argument edge does not exist in the graph, return None
            return None
        return self.adj_matrix[from_idx][to_idx]  # return the weight of the argument edge

    # Purpose of this function: Find all the vertices by a given row index, looping through the elements (columns) of the specified row and return all vertices that have weight
    # Accept arguments of: self object and a row index
    # Restructions: The argument index must be within bound of the graph object
    # Return: An array of (index, weight) that contains all the vertices that are connected and have weight
    def get_connected(self, v):
        tuple = []

        if v >= self.num_of_verts:  # check if argument index is within bound, if not, returns an empty array
            return tuple

        for i in range(len(self.adj_matrix[v])):
            if self.adj_matrix[v][
                i]:  # For every vertex, if it has a weight, append the (index, weight) to the tuple variable
                tuple.append((i, self.adj_matrix[v][i]))
        return tuple

    def __len__(self):
        return self.num_of_verts
