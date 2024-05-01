class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []
        for i in nums:
            new.append(i**2)
        return sorted(new)