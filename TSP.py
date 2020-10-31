from itertools import permutations
import math
import numpy as np

class GraphAlgorithms:

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
            Get the two vertices and the cost
            '''
            (firstVertex, secondVertex, cost) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            # Update self.adjacencyList with a cost from city i to city j
            # Your code goes here:
            if firstVertex not in self.adjacencyList:
                self.adjacencyList.update({firstVertex:[[secondVertex,cost]]})
            else:
                self.adjacencyList[firstVertex].append([secondVertex,cost])

        graphFile.close()

        self.vertices = list(set(self.vertices))
    
    def solve(self):
        min_cost = np.inf # initialize global min_cost as infinity
        min_path = "" # initialize min_path as empty
        
        # Your code goes here:
        all_route = (list(permutations(self.vertices)))
        route_with_start = []
        for route in all_route:
            route_with_start.append(route +(route[0],))
            
        for route in route_with_start:
            cost = 0
            for i in range(len(route)-1):
                for stop in self.adjacencyList[route[i]]:
                    if stop[0] == route[i+1]:
                        cost = cost + int(stop[1])
            min_cost = min(min_cost,cost)
            if cost == min_cost:
                min_path = route
                    
        

        return min_cost, min_path

if __name__ == '__main__':
    
    g = GraphAlgorithms('vt.txt')
    print(g.solve())
    