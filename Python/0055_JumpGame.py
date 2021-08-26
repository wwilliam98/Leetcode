# BFS, Super Slow (TLE)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = [False] * len(nums)
        target = len(nums)-1
        queue = [(0, nums[0])]
        while queue:
            for i in range(len(queue)):
                index, steps = queue.pop(0)
                if index == target:
                    return True

                for step in range(1, steps + 1):
                    nxtIndex = index + step
                    if nxtIndex < len(nums) and not visited[nxtIndex]:
                        queue.append((nxtIndex, nums[nxtIndex]))
                        visited[nxtIndex] = True
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            idx = i
            if nums[i] < 0:
                continue

            while idx + nums[idx] < len(nums):
                print(idx, nums[idx], nums)
                if nums[idx] == 0:
                    break
                temp = idx
                idx += nums[idx]
                nums[temp] = -1

            if idx == len(nums)-1:
                return True

        return False
