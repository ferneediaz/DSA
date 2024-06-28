class Solution:
    def guessNumber(self, n: int) -> int:  
        #BASED ON BINARY SEARCH
        l=1
        h=n
        while l<=h:
            mid=(l+h)//2
            pick=guess(mid)
            if pick==0:
                return mid
            if pick==-1:
                h=mid
            elif pick==1:
                l=mid+1