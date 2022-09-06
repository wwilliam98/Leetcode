class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c = Counter(secret)
        s = set(secret)
        l = len(secret)
        
        bulls = 0
        cows = 0
        for i in range(l):
            if guess[i] in s and c[guess[i]] > 0:
                cows += 1
                c[guess[i]] -= 1
            if secret[i] == guess[i]:
                bulls += 1
                cows -= 1
        
        return str(bulls) + "A" + str(cows) + "B"