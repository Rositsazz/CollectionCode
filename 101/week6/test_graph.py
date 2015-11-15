import unittest
from directedGraph import DirectedGraph
from directedGraph import Node


class DirectedClassTest(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()
        self.n1 = Node("A")
        self.n2 = Node("B")

    def test_existing_graph(self):
        self.assertTrue(isinstance(self.graph, DirectedGraph))

    def test_has_no_node_in_graph(self):
        self.assertFalse(self.graph.has_node(self.n1))

    def test_add_node_in_graph(self):
        self.graph.add_node(self.n1)
        self.assertTrue(self.graph.has_node(self.n1))

    def test_no_existing_node(self):
        self.assertFalse(self.graph.has_node(self.n1))

    def test_existing_node(self):
        self.graph.add_node(self.n1)
        self.assertTrue(self.graph.has_node(self.n1))
        self.assertRaises(Exception)

    def test_add_edge_between_nodes(self):
        self.graph.add_edge(self.n1, self.n2)
        self.assertTrue(self.graph.exist_edge(self.n1, self.n2))

    def test_node_neighbours(self):
        self.graph.add_edge(self.n1, self.n2)
        self.assertEqual(self.graph.get_neighbors_for(self.n1), [self.n2])

    def test_path_between_nodes(self):
        self.graph.add_edge(self.n1, self.n2)
        self.assertTrue(self.graph.path_between(self.n1, self.n2))

if __name__ == '__main__':
    unittest.main()
