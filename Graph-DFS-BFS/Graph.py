
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang

[Abdullah A&
Lian Xue]
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFSInit()
        if method is 'recursive':
            # print(self.unVisitedVertices)
           

            # print(self.path)
            # print(self.vertices)
            
            self.DFS_recur('a')
            print(self.path)



            return self.path

        elif method is 'stack':

#            self.DFS_stack('a')
#            print(self.path)

            # print(f"\nadjacecy list:  {self.adjacencyList}\n")

            # for (v,d) in (self.adjacencyList.items()):
            #    print(f"{v}: {d}\n")

            for v in self.adjacencyList:
                if v in self.unVisitedVertices:
                    self.DFS_stack(v)
            
            print(self.path)
            
            return self.path
            

    def DFS_recur(self,vertex):

        if vertex in self.unVisitedVertices:
            self.path += vertex
            self.unVisitedVertices.remove(vertex)
            for adjVertex in self.adjacencyList[vertex]:
                self.DFS_recur(adjVertex)
            
            
                
    def DFS_stack(self, vertex):
        stack=[]
        stack.append(vertex)
        self.path = stack[0]
        print(f"stack after append: {stack}\n")
        
        while len(stack) != 0:
            print("stack in while:" + str(stack))
            vertex = stack.pop()
            if vertex in self.unVisitedVertices:
                # print("unvisited vertex: " + vertex)
                self.unVisitedVertices.remove(vertex)
                for v in self.adjacencyList[vertex]:
                    # print(f"adjacent v: {v}")
                    if v in self.unVisitedVertices:
                        stack.append(v)

        





    def BFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""
        

    def BFS(self):
        self.BFSInit()
        queue = []
        # Your code goes here:
 
                


        return self.path


    def hasCycle(self):
        # Your code goes here:
        pass # delete "pass" after writing your own code here 




       
                    
    # Work on this function for at most 10 extra points
    def shortestpath(self, p, q):
        # Your code goes here:
        pass # delete "pass" after writing your own code here 
  
                
        

        

