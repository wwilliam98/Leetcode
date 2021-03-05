class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        def backtrack(start, char, length, s):
            if len(s) == length:
                self.combinations.append(s)
                return
            
            for i in range(start, len(char)):
                backtrack(i+1, char, length, s + char[i])
        backtrack(0, characters, combinationLength, "")

    def next(self) -> str:
        return self.combinations.pop(0)

    def hasNext(self) -> bool:
        return self.combinations
