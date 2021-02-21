class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            s = 0
            for j in range(len(boxes[:i])):
                if boxes[j] == "1":
                    s += abs(j-i)
            for j in range(len(boxes)-1, i, -1):
                if boxes[j] == "1":
                    s += abs(j-i)
            res[i] = s
        return res
