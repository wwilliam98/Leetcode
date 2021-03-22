class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1
        
        freq.sort()
        
        mx_freq = freq.pop()
        cooling = (mx_freq-1) * n
        
        #find the number of idle time / cooling
        while freq and cooling > 0:
            cooling -= min(mx_freq - 1, freq.pop()) #it can only be between (number of space of idle (mx_freq-1), or freq.pop())
        cooling = max(0, cooling) #the idle can be negative but we want it to be more than 0
        print(cooling)
        return len(tasks) + cooling
