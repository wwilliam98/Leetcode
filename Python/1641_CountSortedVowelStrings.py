#Math solution using combination
class Solution:
    def countVowelStrings(self, n: int) -> int:
        #Combination problem (5 takes n)
        #(k+n-1)! / (k-1)!n!    ns: k == 5
        #(5+n-1)! / (5-1)!n!
        #(n+4)! / 4!n! = (n+4)(n+3)(n+2)(n+1)/4!
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

#Backtracking solution
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        self.ans = []
        self.helper(n, "", vowels)
        return len(self.ans)
        
    def helper(self, n, temp, v):
        if len(temp) == n:
            self.ans.append(temp)
            return
        
        for i in range(len(v)):
            self.helper(n, temp + v[i], v[i:])
