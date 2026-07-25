class Solution:
    def maxProduct(self, n: int) -> int:
        l=len(str(n))
        res=[]
        for i in range(l):
            r=n%10
            res.append(r)
            n//=10
        res.sort()
        return res[-1]*res[-2]