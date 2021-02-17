class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.d = collections.defaultdict(list)
        for start, end in tickets:
            self.d[start].append(end)
                
        for s, e in self.d.items():
            e.sort(reverse = True) #Lexical Order
            
        self.path = []
        self.dfs('JFK')
        
        return self.path[::-1] #we have to revese the path
    
    
    def dfs(self, start): #permutation
        Dlist = self.d[start]
        while Dlist:
            nextD = Dlist.pop()
            self.dfs(nextD)
            
        self.path.append(start) #appending from end -> start
