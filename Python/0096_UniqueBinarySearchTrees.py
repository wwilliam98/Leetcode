class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        #set when there is no root/ only one root
        G[0], G[1] = 1, 1


        for i in range(2, n+1): #Find all possibilities for this number of root
            for j in range(1, i+1): #J is the current root
                G[i] += G[j-1] * G[i-j] #G[j-1] left subtree, G[i-j] right subtree
        print(G)
        return G[n]
