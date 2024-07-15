class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def pald(num):
            if num == num[::-1]:
                return True
            return False
        def pw(num,q):
            res =""
            while num > 0:
                temp = num % q
                res = str(temp) + res
                num //= q
            return res
        for i in range(2,n-1):
            one = pw(n,i)
            # print(one)
            if not pald(one):
                return False
        return True