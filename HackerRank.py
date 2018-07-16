import networkx as nx
import matplotlib.pyplot as plt
import itertools

def show(g):
    nx.draw(g)
    plt.show()


def nx_solution(n, astronauts):
    g = {}
    for i in range(n):
        g[i] = []
        [g[i].append(e) for e in astronauts if e[0] == i]
    print(str(g))
    # Build graph
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(astronauts)
    # Get connected components
    cc = [c for c in nx.connected_components(graph)]
    print('connected components: ' + str(cc))
    combos = list(itertools.combinations(cc, 2))
    print('combos: ' + str(combos))
    solution = 0
    for c in combos:
        solution += len(c[0]) * len(c[1])
    print('solution: ' + str(solution))
    show(graph)

def custom_solution(n, astronauts):
    pass
    # graph = {}
    # for i in range(n):
    #
    #     graph[i] =
    # print('my graph: ' + str(graph))


if __name__ == "__main__":
    # Gather test data
    n = 6
    astronauts = [[1, 2], [4, 3], [4, 5]]
    custom_solution(n, astronauts)
    # nx_solution(n, astronauts)




