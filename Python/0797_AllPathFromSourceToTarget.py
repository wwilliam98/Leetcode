class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph)-1
        res = []
        
        path = [0]
        def backtrack(curr, path):
            if curr == end:
                res.append(path.copy())
                return
            
            for nextnode in graph[curr]:
                path.append(nextnode)
                backtrack(nextnode, path)
                path.pop()
        
        backtrack(0, path)
        return res
