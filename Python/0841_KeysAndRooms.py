class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [False] * len(rooms)
        keys[0] = True
        stack = [0]
        
        while stack:
            node = stack.pop()
            for key in rooms[node]:
                if not keys[key]:
                    keys[key] = True
                    stack.append(key)
        
        for i in keys:
            if i == False:
                return False
        return True
