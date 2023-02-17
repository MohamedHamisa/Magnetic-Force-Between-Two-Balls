class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(target):
            count = 1 # how many balls could be placed
            first = 0
            for i in range(1, len(position)):
                if position[i] - position[first] >= target:
                    count += 1
                    first = i
            return count
        # binary search to find the right answer
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = right - (right - left) // 2
            if helper(mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left

      


