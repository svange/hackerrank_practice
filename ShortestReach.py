import unittest
import collections


class MyGraph:
    def __init__(self, adj_list=None):
        if adj_list is None:
            adj_list = {}
        adj_list = collections.defaultdict([], adj_list)

        self._graph = adj_list

    @property
    def nodes(self):
        return self._graph.keys()

    def add_node(self, node):
        pass

    def __str__(self):
        string = ''
        for key in self._graph.keys():
            string += '%s: %s\n' % (str(key), str(self._graph[key]))


class MyGraphTester(unittest.TestCase):
    def test_init(self):
        adj_list = {0: [1, 2], 1: [0], 2: [0]}
        graph = MyGraph(adj_list)
        print(graph)


if __name__ == '__main__':
    unittest.main()
