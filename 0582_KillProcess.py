class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = dict()
        for i, e in enumerate(ppid):
            d[e] = d.get(e, [])
            d[e].append(pid[i])
        
        stack = [kill]
        res = []
        
        while stack:
            cur = stack.pop()
            res.append(cur)
            stack.extend(d.get(cur, [])) #Stack = stack + child, if no child: stack = stack + []
        return res
