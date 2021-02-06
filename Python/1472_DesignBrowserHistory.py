class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = [homepage]
        self.future = []

    def visit(self, url: str) -> None:
        self.future = []
        self.prev.append(url)

    def back(self, steps: int) -> str:
        if steps >= len(self.prev):
            for i in range(len(self.prev)-1):
                self.future.append(self.prev.pop())
            return self.prev[-1]
        else:
            for i in range(steps):
                self.future.append(self.prev.pop())
            return self.prev[-1]
            
    def forward(self, steps: int) -> str:
        if not self.future or steps == 0:
            return self.prev[-1]
        elif steps >= len(self.future):
            for i in range(len(self.future)):
                self.prev.append(self.future.pop())
            return self.prev[-1]
        else:
            for i in range(steps):
                self.prev.append(self.future.pop())
            return self.prev[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

#########################################################
class BrowserHistory:
    def __init__(self, homepage: str):
        self.prev = []
        self.future = []
        self.prev.append(homepage)
        
    def visit(self, url: str) -> None:
        self.prev.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.prev) > 1:
            self.future.append(self.prev[-1])
            self.prev.pop()
            steps -= 1
        return self.prev[-1]
            
    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.prev.append(self.future[-1])
            self.future.pop()
            steps -= 1
        return self.prev[-1]
