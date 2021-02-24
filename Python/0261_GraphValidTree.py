class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        #the basic is, graph is a tree if (number of nodes - 1 == number of edges) and (number of nodes(seen) == the number of nodes(n/actual node))
        d = collections.defaultdict(list)
        seen = set()
        
        for start, end in edges:
            d[start].append(end)
            d[end].append(start)
            
        stack = [0]
        seen.add(0)
        
        while stack:
            node = stack.pop()
            for neighbor in d[node]:
                if neighbor in seen:
                    continue
                
                stack.append(neighbor)
                seen.add(neighbor)
        
        return len(seen) == n
