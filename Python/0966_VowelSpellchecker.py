class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def mask(word):
            ret = ""
            for i in word.lower():
                if i in 'aiueo':
                    ret += "*"
                else:
                    ret += i
            
            return ret
        
        d0 = set(wordlist)
        d1 = {w.lower(): w for w in wordlist[::-1]} #lowercase query
        d2 = {mask(w): w for w in wordlist[::-1]} #masked query
        
        def solve(query):
            if query in d0:
                return query
            if query.lower() in d1:
                return d1[query.lower()]
            if mask(query) in d2:
                return d2[mask(query)]
            return ""
        
        res = []
        for q in queries:
            res.append(solve(q))
        return res
