# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            print(candidate)
            if knows(candidate, i): #If candidate knows i, i becomes the next candidate
                candidate = i
        
        if self.CheckIfCandidateIsCelebrity(candidate, n):
            return candidate
        return -1
        
    def CheckIfCandidateIsCelebrity(self, i, node): #Check if candidate knows anyone or any doesnt know candidate
        for j in range(node):
            if i == j:
                continue
            if knows(i, j) or not knows(j, i): #if i knows j, or j doesnt know i, he cant be celebrity
                return False
        return True
