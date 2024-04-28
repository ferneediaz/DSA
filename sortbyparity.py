class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
    # Initialize L to 0
        L = 0
        # Initialize R to length of nums - 1
        R = len(nums) - 1

        # While L < R
        while L < R:
            # If nums[L] is even
            if nums[L] % 2 == 0:
                # Increment L (L is rightly placed, look for the next)
                L += 1
            else:
                # While L < R and nums[R] is odd
                while L < R and nums[R] % 2 != 0:
                    # Decrement R (R is rightly placed, look for an even number from the end)
                    R -= 1
                # If L < R (meaning a swap condition is met)
                if L < R:
                    # Swap nums[L] with nums[R]
                    nums[L], nums[R] = nums[R], nums[L]
                    # Increment L
                    L += 1
                    # Decrement R
                    R -= 1
                    
        # Return nums
        return nums