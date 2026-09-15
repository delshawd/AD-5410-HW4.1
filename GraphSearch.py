################
# original code from:
# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
# accessed on: 02/10/22
# original author: VALERIO VELARDO
# license: none given
################
# CHANGELOG:
# - new main, new graph
# - modified shortest path to return empty list if no path found
# - modified shortest path to return list with start if goal == start
################

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
# end def bfs_connected_component(graph, start):


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return [start]  # "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return []  # "So sorry, but a connecting path doesn't exist :("
# end def bfs_shortest_path(graph, start, goal):


def main():
    # sample graph implemented as a dictionary
    graph = {'1': ['2', '3', '4'],
             '2': ['4', '5'],
             '3': ['6'],
             '4': ['3', '6', '7'],
             '5': ['4', '7'],
             '6': [],
             '7': ['6']}

    # print(bfs_connected_component(graph, '6'))
    print(bfs_shortest_path(graph, '1', '2'))
    print(bfs_shortest_path(graph, '2', '6'))
    print(bfs_shortest_path(graph, '1', '6'))
# end def main():


if __name__ == "__main__":
    main()