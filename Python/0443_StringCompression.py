class Solution:
    def compress(self, chars: List[str]) -> int:
        ret = i = 0 #only one pointer
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[ret] = char
            
            if length > 1:
                len_str = str(length)
                chars[ret + 1: (ret + 1 + len(len_str))] = len_str #O(1) space, switch char to the number
                ret += len(len_str)
            ret, i = ret + 1, i + 1
        return ret
