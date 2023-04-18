import random
from a3_partb import *


def generate_maze(number_of_rows, number_of_columns):
    # Create a list to store the vertical walls
    vertical_walls = []
    horizontal_walls = []

    for i in range(number_of_rows):
        for j in range(number_of_columns - 1):
            wall = i * number_of_columns + j
            vertical_walls.append((wall, wall + 1))
    for i in range(number_of_rows -1):
        for j in range(number_of_columns):
            wall = i * number_of_columns + j
            horizontal_walls.append((wall, wall + number_of_columns))

    # Combine the two lists to create the full maze
    maze = vertical_walls + horizontal_walls
    # Create an empty graph with vertices numbered from 0 to (number_of_rows*number_of_columns - 1)
    """
        graph = {i: {} for i in range(
        number_of_rows * number_of_columns)
             }
    """
    graph = [[] for i in range(number_of_rows * number_of_columns)]

    # For each wall in the maze, create two edges in the graph
    for wall in maze:
        cell_1, cell_2 = wall
        weight = random.randint(1, 50)
        graph[cell_1].append((cell_2, weight))
        graph[cell_2].append((cell_1, weight))

    # Find the minimum spanning tree of the graph
    return graph_analysis(graph, maze, number_of_rows, number_of_columns)


def graph_analysis(g, m, r, c):
    m_e = mst_maze(g)
    for e in m_e:
        u, v = e
        if v == u + 1:
            m.remove((u, v))
        else:
            m.remove((u, u + c))
    return m
