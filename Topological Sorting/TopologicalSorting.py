

class TopologicalSorting:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a directed graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
        # file name
        self.name = fileName
        
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

        # sorted list
        self.sortedList = []
        self.spider('A','M')
    def print_and_save(self):
        #print(self.vertices)
        #print(self.adjacencyList)
        self.sort()
        print(self.sortedList)
        with open('results-'+str(self.name), 'w') as file_handler:
            for node in self.sortedList:
                file_handler.write("{}\n".format(node)) 
        
    #return true when there's no arrow coming in for the node
    def check_arrow(self,val,dic):
        #print("val: "+str(val))
        for key in dic:
            if val in dic[key]:
                #print(dic[key])
                #print("false")
                return False
        #print("true")
        return True
            

    # Topological sorting using decrease-by-one-and-conquer. 
    def sort(self):
        # Your code goes here:
        print(self.adjacencyList)
        copy_adj_list = self.adjacencyList
        while (len(copy_adj_list) != 0):
            for key in list(copy_adj_list):
                if self.check_arrow(key,copy_adj_list):
                    self.sortedList.append(key)
                    vals = copy_adj_list.pop(key)
                    for vals_in_remove in vals:
                        if vals_in_remove not in list(copy_adj_list) and vals_in_remove not in self.sortedList and self.check_arrow(vals_in_remove,copy_adj_list):
                            self.sortedList.append(vals_in_remove)

    def find_paths(self,start,end,unVisitedVertices,path):
        unVisitedVertices.remove(start)
        path.append(start)
        if start == end or start == 'F':
            print (path)
        else:
            for i in self.adjacencyList[start]:
                if i in unVisitedVertices and i != 'F':
                    #print(self.adjacencyList[i])
                    self.find_paths(i,end,unVisitedVertices,path)
        path.pop()
        unVisitedVertices.append(start) 
    # How many different ways can the spider reach the fly by moving along the web’s lines in the directions indicated by the arrow?
    def spider(self,start,end):
        # Your code goes here:
        path = []
        unVisitedVertices = self.vertices
        self.find_paths(start,end,unVisitedVertices,path)


if __name__ == "__main__":

    #s = TopologicalSorting("graph-example.txt")
    #s.print_and_save()

    # Be careful! graph-courses.txt is incomplete. Please finish this txt file at first. 
    #s = TopologicalSorting("graph-courses.txt")
    #s.print_and_save()
    # print("vertices: "+str(s.vertices))
    # print("dictionary: "+str(s.adjacencyList))
    # print("sorted list: "+str(s.sortedList))
 
    s = TopologicalSorting("graph-spider.txt")
    #s = spider
    s.print_and_save()
