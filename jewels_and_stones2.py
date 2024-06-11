<<<<<<< HEAD
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in jewels:
                count += 1
        return count
=======
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
    
        # Loop through each stone
        for stone in stones:
            # Check if the stone is also a jewel
            if stone in jewels:
                count += 1
        
        return count
>>>>>>> origin/main
