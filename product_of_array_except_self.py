class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n  # Initialize the answer list with 1s
        
        # Calculate the left products
        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        
        # Calculate the right products and multiply with the left products
        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans
