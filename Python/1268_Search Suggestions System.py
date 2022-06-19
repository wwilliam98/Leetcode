from collections import defaultdict

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() #sort by lexicographically order
        self.prefixes = defaultdict(list)
        for product in products:
            prefix = ""
            for letter in product:
                prefix += letter
                self.prefixes[prefix].append(product)    
        self.ans = []
        self.suggestion(searchWord)
        return self.ans
        
    def suggestion(self, word):
        prefix = ""
        for w in word:
            prefix += w
            if (self.prefixes[prefix] and len(self.prefixes[prefix]) >= 3):
                self.ans.append((self.prefixes[prefix])[:3])
            else:
                self.ans.append(self.prefixes[prefix])
        