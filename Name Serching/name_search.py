'''
Lab 6 
Wynter M & Lian Xue
'''

import numpy as np 
import argparse
import collections
from collections import defaultdict
class NameSearch:

    def __init__(self, Name_List, Name_Algorithm, Name_Length):
        # Matrix of the word search puzzle 
        self.matrix = np.load("./data/matrix.npy")
        # Name of the algorithm
        self.Name_Algorithm = Name_Algorithm
        # Length of the name
        self.Name_Length = Name_Length
        # List of all potential names 
        with open("./data/names/"+Name_List+".txt", 'r') as f:
            self.names = f.read().splitlines()
        self.names = [n.upper().strip() for n in self.names]

    def match_BruteForce(self, pattern, text):
        # String matching by brute force
        # Your code goes here:
        name_char_count = 0
        for text_char in text:
            for name_char_count in range(len(pattern)):
                if pattern[name_char_count] != text_char:
                    name_char_count = name_char_count + 1
                else:
                    if name_char_count == len(pattern)-1 and len(pattern) == self.Name_Length:
                        return pattern
        return "Name not found"
        
    def ShiftTable(self,pattern):
        pattern_dic = defaultdict(lambda: len(pattern))
        for index in range(0,len(pattern)-1):
            pattern_dic[pattern[index]] = len(pattern) - 1 - index
        return pattern_dic

    def match_Horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        # Your code goes here:
        skip = []
        m = len(pattern)
        n = len(text)
        for i in range(256): skip.append(-1)
        for i in range(m): skip[ord(pattern[i])] = m
        for i in range(n + m + 1):
            skip = 0
            for j in range(m-1, -1, -1):
                if text[i+j] != pattern[j]:
                    skip = j - skip[ord(text[i+j])]
                    if skip < 1: skip = 1
                    break
            if skip == 0:
                print ("Found at {0}".format(i))
                return

            i += skip

        print("Not Found")
        return

    def search(self):
        # pattern is each name in self.names
        # text is each horizontal, vertical, and diagonal strings in self.matrix 
        if self.Name_Algorithm == "BruteForce":
            # call self.match_BruteForce(pattern, text)
            rowCount=colCount = 0
            rowNum, colNum = self.matrix.shape
            #letter = matrix[row, col]
            #row = matrix[r,:]
            #column = trix[:,c]
            for pattern in self.names:
                for rowCount in range(0,rowNum):
                    row_result = self.match_BruteForce(pattern, self.matrix[rowCount,:])
                    #print("row result: "+row_result)
                    if row_result != "Name not found":
                        return row_result
                for colCount in range(0,colNum):
                    col_result = self.match_BruteForce(pattern,self.matrix[:,colCount])
                    #print("col result: " + col_result)
                    if row_result != "Name not found":
                        return col_result
                currentX = startX = 0
                currentY = startY = 0
                charCount = 0
                dia_plus_char=[]
                dia_plus_matrix=[]
                while charCount < rowNum * colNum:
                    while currentX < colCount and currentY < rowCount:
                            dia_plus_char.append(self.matrix[currentX,currentY])
                            currentX = currentX + 1
                            currentY = currentY + 1
                    dia_plus_matrix.append(dia_plus_char)
                    if startY != 0:
                        startY = startY -1
                    else:
                        startX = startX + 1
                    charCount += 1
                for i in dia_plus_matrix:
                    dia_plus_result = self.match_BruteForce(pattern,i)
                    #print("dia plus result: "+dia_plus_result)
                    if dia_plus_result != "Name not found":
                        return dia_plus_result

                charCount = 0
                dia_min_char=[]
                dia_min_matrix=[]
                currentX = currentY = 0
                startX = colNum
                startY = rowNum
                while charCount < rowNum * colNum:
                    while currentX < colCount and currentY < rowCount:
                            dia_min_char.append(self.matrix[currentX,currentY])
                            currentX = currentX + 1
                            currentY = currentY + 1
                    dia_min_matrix.append(dia_min_char)
                    if startY != 0:
                        startY = startY + 1
                    else:
                        startX = startX - 1
                    charCount += 1
                for j in dia_min_matrix:
                    dia_min_result = self.match_BruteForce(pattern,j)
                    #print("dia min result:" + dia_min_result)
                    if dia_min_result != "Name not found":
                        return dia_min_result
            return "Name not found"

        elif self.Name_Algorithm == "Horspool":
            # call self.match_Horspool(pattern, text)
            # call self.match_BruteForce(pattern, text)
            rowCount=colCount = 0
            rowNum, colNum = self.matrix.shape
            #letter = matrix[row, col]
            #row = matrix[r,:]
            #column = trix[:,c]
            for pattern in self.names:
                for rowCount in range(0,rowNum):
                    row_result = self.match_Horspool(pattern, self.matrix[rowCount,:])
                    #print("row result: "+row_result)
                    if row_result != "Name not found":
                        return row_result
                for colCount in range(0,colNum):
                    col_result = self.match_Horspool(pattern,self.matrix[:,colCount])
                    #print("col result: " + col_result)
                    if row_result != "Name not found":
                        return col_result
                currentX = startX = 0
                currentY = startY = 0
                charCount = 0
                dia_plus_char=[]
                dia_plus_matrix=[]
                while charCount < rowNum * colNum:
                    while currentX < colCount and currentY < rowCount:
                            dia_plus_char.append(self.matrix[currentX,currentY])
                            currentX = currentX + 1
                            currentY = currentY + 1
                    dia_plus_matrix.append(dia_plus_char)
                    if startY != 0:
                        startY = startY -1
                    else:
                        startX = startX + 1
                    charCount += 1
                for i in dia_plus_matrix:
                    dia_plus_result = self.match_Horspool(pattern,i)
                    #print("dia plus result: "+dia_plus_result)
                    if dia_plus_result != "Name not found":
                        return dia_plus_result

                charCount = 0
                dia_min_char=[]
                dia_min_matrix=[]
                currentX = currentY = 0
                startX = colNum
                startY = rowNum
                while charCount < rowNum * colNum:
                    while currentX < colCount and currentY < rowCount:
                            dia_min_char.append(self.matrix[currentX,currentY])
                            currentX = currentX + 1
                            currentY = currentY + 1
                    dia_min_matrix.append(dia_min_char)
                    if startY != 0:
                        startY = startY + 1
                    else:
                        startX = startX - 1
                    charCount += 1
                for j in dia_min_matrix:
                    dia_min_result = self.match_Horspool(pattern,j)
                    #print("dia min result:" + dia_min_result)
                    if dia_min_result != "Name not found":
                        return dia_min_result       
            return "Name not found"

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Word Searching')
    parser.add_argument('-name', dest='Name_List', required = True, type = str, help='Name of name list')
    parser.add_argument('-algorithm', dest='Name_Algorithm', required = True, type = str, help='Name of algorithm')
    parser.add_argument('-length', dest='Name_Length', required = True, type = int, help='Length of the name')
    args = parser.parse_args()

    # Example:
    # python name_search.py -algorithm BruteForce -name Mexican -length 5

    obj = NameSearch(args.Name_List, args.Name_Algorithm, args.Name_Length)
    name = obj.search()
    if name: 
        print(name)


