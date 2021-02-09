#find all the intervals, merge the intervals, set the result
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        intervals = []
        
        for i in range(len(s)): #store all the intervals
            for j in range(i, len(s)):
                if s[i:j+1] in dict:
                    intervals.append([i, j])
        
        intervals.sort() #need sort to merge the intervals
        merge = []
        for interval in intervals:
            if not merge or merge[-1][1]+1 < interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1], interval[1])
                
        res, prev = "", 0 #Build the string
        for start, end in merge:
            res += s[prev:start] + '<b>' + s[start:end+1] + '</b>'
            prev = end+1
        return res + s[prev:] #dont forget the leftover at the end
