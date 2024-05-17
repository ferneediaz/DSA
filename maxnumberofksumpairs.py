class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        L = 0
        R = len(nums) -1
        operation = 0
        while L < R:
            if nums[L] + nums[R] == k:
                operation += 1
                L +=1 
                R -=1
            elif nums[L] + nums[R] < k:
                L += 1
            else:
                R -= 1
        return operation

