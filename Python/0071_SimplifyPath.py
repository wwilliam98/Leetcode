class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for path in path.split("/"):
            if path == "..":
                if stack:
                    stack.pop()
            elif path == "." or not path:
                continue
            else:
                stack.append(path)
        
        finalPath = "/" + "/".join(stack)
        return finalPath
