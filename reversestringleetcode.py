class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        N = len(s)
        L = 0
        R = N - 1
        while L < R:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1
            


            # no return since we are changing the existing list so O(n) for time and O(1) for space