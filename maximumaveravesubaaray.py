class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        maxi = s/k
        for i in range(len(nums)-k):
            s = s-nums[i]
            s = s+nums[i+k]
            maxi = max(maxi,s/k)
        return maxi