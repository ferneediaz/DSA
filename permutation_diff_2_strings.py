class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0

        for index,c in enumerate(s):
            index2 = t.index(c)

            total += abs(index2-index)

        return total