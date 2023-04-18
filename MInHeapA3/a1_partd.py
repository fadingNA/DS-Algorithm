def helper(maze, curr_cell, to_cell, path):
    # The base case
    if curr_cell == to_cell:
        return path + [curr_cell]  # if cell is found, append it the path and return

    # Find adjacent neigbours for the current cell, store them in an array
    neighbours = [maze.get_up(curr_cell), maze.get_right(curr_cell), maze.get_down(curr_cell), maze.get_left(curr_cell)]

    # The key for this part is to explore all adjacent cells of the current cell
    for i in neighbours:
        if i != -1 and i not in path:  # if i does not hit the wall or edge AND has not appeared in the path
            # Recursion
            result = helper(maze, i, to_cell, path + [curr_cell])  # record the path
            if result:
                return result
    return None  # return none if the current cell has no new neighbours to explore


def find_path(maze, from_cell, to_cell):
    return helper(maze, from_cell, to_cell, path=[]) or []  # return a valid array of path or an empty path
