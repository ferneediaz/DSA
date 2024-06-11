class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_len = len(s)
        if s == s[::-1]:
            return s_len

        chars = {}
        palindrome_length = 0

        for n in s:
            if chars.get(n):
                chars[n] += 1
                if chars[n] % 2 == 0:
                    palindrome_length += 2
            else:
                chars[n] = 1

        return palindrome_length + 1 if s_len - palindrome_length != 0 else palindrome_length