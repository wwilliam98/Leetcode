# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        mostleft = cols
        for r in range(rows):
            lo, hi = 0, cols-1
            while lo < hi:
                mid = (lo + hi) //2
                if binaryMatrix.get(r, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            
            if binaryMatrix.get(r, lo) == 1:
                mostleft = min(mostleft, lo)
                  
        if mostleft == cols:
            return -1
        else:
            return mostleft
################################################
#O(RxC) not accepted
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        mostleft = float('inf')
        for r in range(rows):
            for c in range(cols):
                if binaryMatrix.get(r,c) == 1:
                    mostleft = min(mostleft, c)
                    
        if mostleft == float('inf'):
            return -1
        else:
            return mostleft
