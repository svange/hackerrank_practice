import itertools


class MyGraph:

    def __init__(self, adjMatrix=None):
        if adjMatrix is None:
            adjMatrix = {}

        self._graph = adjMatrix
        self._visited = {}
        self._cc = {}
        for vertex in self._graph.keys():
            self._visited[vertex] = False
            self._cc[vertex] = None


    @property
    def vertices(self):
        return list(self._graph.keys())

    def edges(self, vertex=None):
        if vertex is None:
            edges = []
            for start in self._graph.keys():
                for end in self._graph(start):
                    edges.append((start, end))
            return edges
        else:
            return [(vertex, end) for end in self._graph[vertex]]

    def add_vertex(self, vertex):
        self._graph[vertex] = []
        self._visited[vertex] = False

    def add_edge(self, edge):
        edge = tuple(edge)
        if edge[0] not in self._graph.keys():
            self.add_vertex(edge[0])
        if edge[1] not in self._graph.keys():
            self.add_vertex(edge[1])

        self._graph[edge[0]].append(edge[1])
        self._graph[edge[1]].append(edge[0])

    def clear_visited(self):
        for vertex in self._visited.keys():
            self._visited[vertex] = False

    def visited(self, vertex):
        self._visited[vertex] = True

    def connected_components(self):
        ''' returns a list of vertices for each components in graph:\
            For example: [[1, 2], [3, 4, 5, 6]]
        '''
        cc = 0
        for v in self.vertices:
            self._explore(v, cc)
            cc += 1
        cc_table = []
        for v in self._cc.keys():
            cc_table.append(self._cc[v])
        return cc_table

    def _explore(self, v, cc):
        if self.visited(v):
            return
        else:
            self.visited(v)
            self._cc[v] = cc
            cc += 1
            for n in self._graph.get(v):
                self._explore(n, cc)


if __name__ == "__main__":
    # Gather test data
    n = 6
    astronauts = [[1, 2], [4, 3], [4, 5]]
    g = {}
    graph = MyGraph()
    for i in range(n)[1::]:
        g[i] = []
        [g[i].append(e) for e in astronauts if e[0] == i]
        graph.add_vertex(i)
    for edge in astronauts:
        graph.add_edge(edge)

    # Get connected components
    cc = graph.connected_components()
    print('connected components: ' + str(cc))
    combos = list(itertools.combinations(cc, 2))
    print('combos: ' + str(combos))
    solution = 0
    for c in combos:
        solution += len(c[0]) * len(c[1])
    print('solution: ' + str(solution))
