class Solution:
    def findLHS(self, nums: List[int]) -> int:
    # Step 1: Create a frequency dictionary
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Traverse the freq dictionary to find the longest harmonious subsequence
        max_length = 0
        for key in freq:
            # Check if key + 1 exists in the dictionary
            if key + 1 in freq:
                # Sum frequency of key and key + 1
                current_length = freq[key] + freq[key + 1]
                # Track the maximum length found
                if current_length > max_length:
                    max_length = current_length

        # Return the maximum length found
        return max_length
