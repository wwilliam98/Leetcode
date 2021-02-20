class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sz = size
        self.arr = []
        self.count = 0

    def next(self, val: int) -> float:
        s = 0
        self.arr.append(val)
        self.count += 1
        if self.count < self.sz:
            for i in self.arr[:self.count]:
                s += i
            return s / self.count
        else:
            for i in self.arr[self.count-self.sz:]:
                s += i
            return s / self.sz


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
