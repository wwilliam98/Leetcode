class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        #reverse everything
        reverse(0, len(s)-1)

        #reverse only the word
        first_letter_index = 0
        for right in range(len(s)):
            if s[right] == " ":
                reverse(first_letter_index, right-1)
                first_letter_index = right + 1
        reverse(first_letter_index, len(s)-1)
