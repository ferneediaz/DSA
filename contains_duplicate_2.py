class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in hashMap and abs(hashMap[x] - i) <= k: return True
            hashMap[x] = i
        return False