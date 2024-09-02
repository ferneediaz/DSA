class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right = 0, 0
        c = 0
        while right < len(s):
            if(s[right] not in seen):
                seen.add(s[right])
                right += 1
                c = max(c, len(seen))
            else:
                seen.remove(s[left])
                left += 1
        return c