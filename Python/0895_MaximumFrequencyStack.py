class FreqStack:

    def __init__(self):
        self.counter = collections.Counter()
        self.stack = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        f = self.counter[x] + 1
        self.counter[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.stack[f].append(x)
        

    def pop(self) -> int:
        mx = self.stack[self.maxfreq].pop()
        self.counter[mx] -= 1
        if not self.stack[self.maxfreq]:
            self.maxfreq -= 1
        return mx
