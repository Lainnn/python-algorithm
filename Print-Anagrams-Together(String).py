#User function Template for python3
def reverse(word):
    after = []
    for i in range(len(word)-1,-1,-1):
        after.append(word[i])
    final = "".join(after)
    return final

def Anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''
    
    #code here
    ret_list = []
    sorted_list = [''.join(sorted(word)) for word in words]
    dict_words = {}
    for i,e in enumerate(sorted_list):
        dict_words.setdefault(e,[]).append(i)
    for index in dict_words.values():
        ret_list.append([words[i] for i in index])
    return ret_list


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ans=Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends