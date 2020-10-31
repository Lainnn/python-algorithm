#User function Template for python3

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n, k):
    # code here
    memo = [[0 for x in range(k+1)] for x in range(n+1)] 
    for i in range(1,k+1):
        memo[1][i] = i
    for i in range(1,n+1):
        memo[i][0] = 0
        memo[i][1] = 1
    for i in range(2,n+1):
        for j in range(2,k+1):
            memo[i][j] = k
            for x in range(1,j+1):
                res = 1 + max(memo[i-1][x-1], memo[i][j-x])
                if res < memo[i][j]: 
                    memo[i][j] = res
    return memo[n][k]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        print(eggDrop(n,k))
# } Driver Code Ends