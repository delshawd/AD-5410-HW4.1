from GraphSearch import *


def main():
    # sample graph implemented as a dictionary
    graph = {'OMA': ['DAL', 'HOU', 'MDW'],
             'SDF': ['BWI', 'DAL', 'HOU', 'MDW'],
             'BWI': ['SDF', 'PWM', 'SLC', 'BZE', 'DAL', 'HOU', 'MDW'],
             'PWM': ['BWI', 'MDW'],
             'SLC': ['BWI', 'DAL', 'HOU', 'MDW'],
             'BZE': ['BWI', 'HOU'],
             'DAL': ['OMA', 'SDF', 'BWI', 'SLC', 'HOU', 'MDW'],
             'HOU': ['OMA', 'SDF', 'BWI', 'SLC', 'BZE', 'DAL', 'MDW'],
             'MDW': ['OMA', 'SDF', 'BWI', 'PWM', 'SLC', 'DAL', 'HOU']}
    print(bfs_shortest_path(graph, 'OMA', 'SDF'))
    print(bfs_shortest_path(graph, 'BWI', 'SLC'))
    print(bfs_shortest_path(graph, 'SLC', 'PWM'))
    print(bfs_shortest_path(graph, 'BZE', 'PWM'))

# end def main():


if __name__ == "__main__":
    main()