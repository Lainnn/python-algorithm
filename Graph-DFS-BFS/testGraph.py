'''
Modified on Sep 19, 2018
@auther: Jingsai
'''
import unittest

import Graph

class Test(unittest.TestCase):

    ga1 = Graph.GraphAlgorithms('graph-1.txt')
    ga2 = Graph.GraphAlgorithms('graph-2.txt')
    ga3 = Graph.GraphAlgorithms('graph-3.txt')
    ga4 = Graph.GraphAlgorithms('graph-4.txt')

    def testDFS_recursive(self):
        self.assertEqual('abefcgdhij', self.ga1.DFS('recursive'))
        # Please add test cases for graph2, graph3, and graph4
        # Your code goes here:



    def testDFS_stack(self):
        self.assertEqual('aijdhcgfbe', self.ga1.DFS('stack'))
        # Please add test cases for graph2, graph3, and graph4
        # Your code goes here:
        


    def testBFS(self):
        self.assertEqual('abcdiefghj', self.ga1.BFS())
        # Please add test cases for graph2, graph3, and graph4
        # Your code goes here:
        


    def testhasCycle(self):
        self.assertTrue(self.ga1.hasCycle())
        # Please add test cases for graph2, graph3, and graph4
        # Your code goes here:
        


    # Uncomment and work on this test for at most 10 extra points
    # def testshortestpath(self):
    #     self.assertEqual(2, self.ga1.shortestpath('a','f'))
    #     # Please add test cases for graph2, graph3, and graph4
    #     # Your code goes here:
        


if __name__ == "__main__":
    unittest.main()