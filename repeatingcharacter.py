class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		count = {}
		res = l = maxF = 0 
		for i in range(len(s)):
			count[s[i]] = 1 + count.get(s[i], 0)
			maxF = max(maxF, count[s[i]])
			while (i - l + 1) - maxF > k:
				count[s[l]] -= 1
				l += 1
			res = max(res, i - l + 1)
		return res
	